---
name: wiki-ingest
description: >
  Add one new source from raw/ to the LLM wiki: write a summary page in wiki/sources/, create or update the
  concept pages it touches, record contradictions in wiki/open-questions.md, update wiki/index.md and append to
  wiki/log.md. Use when the user says "ingest raw/<file>", "add this source", "process my notes", "put this
  into the wiki", or adds a new file to raw/.
allowed-tools: Read, Write, Edit, Bash
---

# wiki-ingest

Follow [AGENTS.md → Ingest](../../../AGENTS.md#ingest--add-a-new-source). The rules for pages, links and the log are
in AGENTS.md. Don't repeat or change them here.

## Steps

1. **Pick the source.** If the user didn't name a file, run `bash scripts/lint.sh` and list the raw files that are
   "not ingested yet". Ask which one. Ingest **one** source at a time.
   If the user pasted text instead of a file, offer to save it as `raw/<date>-<slug>.md` first.
2. **Read it, then talk.** Tell the user the 3–5 key points in simple words. Ask: "Anything to focus on, or
   anything I got wrong?" Wait for the answer.
3. **Check what exists.** Read `wiki/index.md`. For each key point, search for an existing page:
   `grep -ril "<term>" wiki/`. Update an existing page rather than creating a duplicate.
4. **Draft the changes** and show the list before writing:
   - new `wiki/sources/<slug>.md` (from `templates/source.md`)
   - new or updated `wiki/concepts/<slug>.md` (from `templates/concept.md`)
   - contradictions with existing pages → a new entry in `wiki/open-questions.md`
5. **Write** after the user says yes. Then add every new page to `wiki/index.md` and append a log entry:
   `## [YYYY-MM-DD] ingest | <source title>` with Added / Updated / Open lines.
6. **Check:** run `bash scripts/lint.sh` and fix any ERROR you caused.
7. **Summarize:** list the files changed and propose the commit message `wiki(ingest): <source title>`. Don't commit
   unless the user asks.

## Guardrails

- Never edit, rename or delete files in `raw/`.
- Only facts from the source. Mark explanations you add with *(general knowledge)*. Don't guess names or dates.
- Never put private data about real people (phone numbers, addresses, grades) into the wiki.
