---
name: wiki-lint
description: >
  Health-check the LLM wiki: run scripts/lint.sh (broken links, pages missing from the index, orphans, missing
  front matter, raw files never ingested), then look for contradictions, claims without a source, missing concept
  pages and old "To verify" marks. Reports findings and fixes only what the user approves. Use when the user says
  "lint the wiki", "check the wiki", "find broken links", "what's missing?", or as regular upkeep.
allowed-tools: Read, Write, Edit, Bash
---

# wiki-lint

Follow [AGENTS.md → Lint](../../../AGENTS.md#lint--health-check).

## Steps

1. **Run the script** from the repository root:
   ```bash
   bash scripts/lint.sh
   ```
2. **Judgement checks** (the script can't do these):
   - **Contradictions:** two pages that say opposite things. Is each one already in `wiki/open-questions.md`?
   - **No source:** sentences that are not from a source and not marked *(general knowledge)*.
   - **Missing pages:** a term that appears on several pages but has no concept page of its own.
   - **To verify:** marks and open questions that a newer source may answer now.
3. **Report** in three groups: **Errors** (from the script), **Warnings** (script and judgement), **Suggestions**
   (pages to write, sources to look for). For each: what, where (file), what to do.
4. **Fix only with approval.** After fixing, run the script again. Append
   `## [YYYY-MM-DD] lint | <summary>` to `wiki/log.md` and propose `wiki(lint): <summary>`.

## Guardrails

- Read-only until the user approves a fix.
- Never edit `raw/` to fix a problem. The wiki follows the sources, not the other way round.
- Report what you find. Never invent findings.
