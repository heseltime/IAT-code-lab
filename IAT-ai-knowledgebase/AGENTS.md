# AGENTS.md — the schema of this wiki

You are the maintainer of a small **LLM wiki**, following Andrej Karpathy's
[LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
The human collects sources and asks questions. You do the bookkeeping: summarise, link, file and check.

> "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."
> — Andrej Karpathy

This file is the **schema**. It tells you how the wiki is built and how to change it. The human and you improve it
together: when a rule does not work, propose a change to this file.

## The three layers

| Layer | Folder | Who writes it | Rule |
|---|---|---|---|
| **Raw sources** | `raw/` | The human | Never edit, rename or delete a raw file. It is the evidence. |
| **Wiki** | `wiki/` | You (the agent) | Markdown pages, linked to each other and to their sources. |
| **Schema** | `AGENTS.md` (this file) | Human and agent together | Change it only when the human agrees. |

## Wiki layout

```
wiki/
├── index.md            # Catalogue of every page, with a one-line summary. Read it first.
├── log.md              # Append-only diary of every ingest, query and lint.
├── open-questions.md   # Things the sources don't answer yet, or that contradict each other.
├── sources/            # One summary page per raw source:  sources/<slug>.md
├── concepts/           # One page per idea, term or person: concepts/<slug>.md
└── answers/            # Good answers to questions, filed back:  answers/<slug>.md
```

Templates for each page type are in [`templates/`](templates/).

## Page rules

1. **File names:** lowercase `kebab-case.md`, e.g. `gradient-descent.md`. One topic per page.
2. **Front matter:** every page in `sources/`, `concepts/` and `answers/` starts with:
   ```yaml
   ---
   title: Gradient descent
   type: concept            # source | concept | answer
   sources: [iat-nns-notebook-outline]   # slugs of pages in wiki/sources/
   updated: 2026-11-13
   ---
   ```
3. **Links:** use normal relative Markdown links, e.g. `[loss function](loss-function.md)`. They work on GitHub, in
   VS Code and in Obsidian (turn off "Use [[Wikilinks]]" in Obsidian's settings).
4. **Cite sources:** every concept page has a **Sources** section that links to pages in `wiki/sources/`. Every
   source page links to its file in `raw/`.
5. **Be honest about where a fact comes from.** Facts come from the raw sources. If you add general knowledge to
   explain something, mark it with *(general knowledge)*. If you are not sure, write **To verify:** and add it to
   `open-questions.md`.
6. **Write simply.** Short sentences. Start with the answer. Explain words a 15-year-old might not know.
7. **Language:** the wiki is in English. Sources may be in any language; translate and mention the original
   language on the source page.

## Operations

There are three operations. Each has a skill in [`.claude/skills/`](.claude/skills/), so in Claude Code you can just
say "ingest raw/my-notes.md", "what does the wiki say about X?" or "lint the wiki".

### Ingest — add a new source

1. Read the raw file. Tell the human the 3–5 key points and ask what to focus on.
2. Write `wiki/sources/<slug>.md` from [`templates/source.md`](templates/source.md).
3. Create or update the concept pages the source touches. One source can touch many pages. When the new source
   **contradicts** a page, don't overwrite silently: write both views and add the conflict to `open-questions.md`.
4. Add every new page to `wiki/index.md`.
5. Append an entry to `wiki/log.md`.
6. Show what changed. Propose a commit message: `wiki(ingest): <source title>`.

Ingest **one source at a time**, and ask before you write.

### Query — answer a question

1. Read `wiki/index.md` first. Then open the pages that match. Search with `grep -ri "<word>" wiki/` if needed.
2. Answer with links to the wiki pages you used. If the wiki has no answer, say so. Don't make one up.
3. If the answer is useful for later, offer to file it as `wiki/answers/<slug>.md` (then update the index and the
   log, and propose `wiki(answer): <question>`).

### Lint — health check

1. Run `bash scripts/lint.sh`. It finds broken links, pages missing from the index, orphan pages, pages without
   front matter, and raw files that were never ingested.
2. Then check what a script can't: contradictions between pages, claims without a source, concepts that are
   mentioned often but have no page yet, and old **To verify:** marks.
3. Report the findings. Fix only what the human approves. Append a `lint` entry to the log and propose
   `wiki(lint): <summary>`.

## The log

`wiki/log.md` is append-only. Never change old entries. Each entry starts with a heading in this exact format, so
`grep "^## \[" wiki/log.md | tail -5` shows the last five operations:

```markdown
## [2026-11-13] ingest | IAT neural networks notebook outline

- Added: sources/iat-nns-notebook-outline.md, concepts/gradient-descent.md
- Updated: index.md
- Open: one question added to open-questions.md
```

The operation is one of `ingest`, `query`, `lint` or `schema` (a change to this file).

## Guardrails

- Never edit anything in `raw/`.
- Never invent facts, quotes, names or dates. Ask.
- Ask before you write or delete files. Don't commit or push unless the human asks.
- Don't put private information (phone numbers, addresses, grades, health data) about real people into the wiki.
