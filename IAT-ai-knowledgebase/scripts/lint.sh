#!/usr/bin/env bash
# Health check for the wiki. Run from the repository root:
#
#   bash scripts/lint.sh
#
# ERROR (exit code 1):
#   - a relative link in wiki/ or AGENTS.md points to a file that does not exist
#   - a page in wiki/sources, wiki/concepts or wiki/answers is not listed in wiki/index.md
# WARN (exit code 0):
#   - a page has no front matter (title, type, sources, updated)
#   - a concept or answer page that no other page links to (an "orphan"; index.md and log.md don't count)
#   - a file in raw/ that no source page links to (it was never ingested)
#
# Works with the bash on macOS (3.2) and Linux. No other tools needed.
set -euo pipefail

if [[ ! -f wiki/index.md ]]; then
  echo "ERROR: run this from the repository root (wiki/index.md not found)" >&2
  exit 2
fi

ERRORS=0
WARNINGS=0
error() { echo "ERROR: $*"; ERRORS=$((ERRORS + 1)); }
warn()  { echo "WARN:  $*"; WARNINGS=$((WARNINGS + 1)); }

# Relative link targets in a Markdown file, one per line, without "#anchor".
# Ignores code blocks and `inline code` (examples there are not real links) and web links.
link_targets() {
  awk '/^```/ { code = !code; next } !code { gsub(/`[^`]*`/, ""); print }' "$1" \
    | { grep -o '\]([^)]*)' || true; } \
    | sed -e 's/^](//' -e 's/)$//' -e 's/#.*$//' \
    | { grep -v -E '^(https?:|mailto:|$)' || true; }
}

# Wiki pages that must be in the index.
content_pages() {
  find wiki/sources wiki/concepts wiki/answers -name '*.md' 2>/dev/null | sort
}

# 1. Broken links.
while read -r file; do
  dir=$(dirname "$file")
  while read -r target; do
    [[ -z "$target" ]] && continue
    if [[ ! -e "$dir/$target" ]]; then
      error "broken link in $file -> $target"
    fi
  done < <(link_targets "$file")
done < <({ find wiki -name '*.md'; echo AGENTS.md; } | sort)

# 2. Every page is in the index. 3. Front matter.
while read -r page; do
  rel=${page#wiki/}
  if ! grep -qF "]($rel)" wiki/index.md; then
    error "$page is not listed in wiki/index.md"
  fi
  if [[ "$(head -1 "$page")" != "---" ]]; then
    warn "$page has no front matter (see AGENTS.md -> Page rules)"
  else
    for key in title type sources updated; do
      if ! sed -n '2,/^---$/p' "$page" | grep -q "^$key:"; then
        warn "$page: front matter has no '$key:'"
      fi
    done
  fi
done < <(content_pages)

# 4. Orphans: concept and answer pages that no other page links to.
while read -r page; do
  name=$(basename "$page")
  found=0
  while read -r other; do
    [[ "$other" == "$page" || "$other" == wiki/index.md || "$other" == wiki/log.md ]] && continue
    if link_targets "$other" | grep -q "\(^\|/\)$name\$"; then
      found=1
      break
    fi
  done < <(find wiki -name '*.md' | sort)
  if [[ $found -eq 0 ]]; then
    warn "orphan: $page (no other page links to it)"
  fi
done < <(find wiki/concepts wiki/answers -name '*.md' 2>/dev/null | sort)

# 5. Raw files that were never ingested.
while read -r raw; do
  name=${raw#raw/}
  if ! grep -rqF "raw/$name" wiki/sources 2>/dev/null; then
    warn "not ingested yet: $raw (no page in wiki/sources links to it)"
  fi
done < <(find raw -type f ! -name 'README.md' ! -name '.*' ! -path 'raw/assets/*' | sort)

echo
echo "Pages: $(content_pages | grep -c . || true) | raw files: $(find raw -type f ! -name 'README.md' ! -name '.*' ! -path 'raw/assets/*' | grep -c . || true)"
echo "Result: $ERRORS error(s), $WARNINGS warning(s)"
[[ $ERRORS -eq 0 ]]
