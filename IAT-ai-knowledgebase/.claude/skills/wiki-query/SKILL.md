---
name: wiki-query
description: >
  Answer a question from the LLM wiki in wiki/, with links to the pages used, and say clearly when the wiki has no
  answer. Can file a good answer back as wiki/answers/<slug>.md. Use when the user asks "what does the wiki say
  about X?", "explain X", "compare X and Y", "quiz me on X", "make a summary / cheat sheet of X", or any question
  about the topic of the wiki.
allowed-tools: Read, Write, Edit, Bash
---

# wiki-query

Follow [AGENTS.md → Query](../../../AGENTS.md#query--answer-a-question).

## Steps

1. **Start at the index.** Read `wiki/index.md`. Pick the pages that match the question.
2. **Search** if the index is not enough: `grep -ril -e "<word1>" -e "<word2>" wiki/`.
3. **Read** the pages. Follow their links one step further if needed. Check `wiki/open-questions.md`: is the
   question (or part of it) still open?
4. **Answer** in simple words, answer first. Link every page you used, e.g.
   `([gradient descent](wiki/concepts/gradient-descent.md))`. If pages disagree, show both. If the wiki has no
   answer, say "The wiki doesn't cover this yet" and suggest a source to ingest. Don't fill the gap from memory
   without saying so.
5. **Any format works:** a table, a quiz with answers at the end, a cheat sheet, a Mermaid diagram.
6. **File it (optional).** If the answer is worth keeping, ask. On yes: write `wiki/answers/<slug>.md` from
   `templates/answer.md`, add it to `wiki/index.md`, link it from the concept pages it uses, append
   `## [YYYY-MM-DD] query | <question>` to `wiki/log.md`, and propose `wiki(answer): <question>`.
   An answer that is not filed changes no files.

## Guardrails

- Read-only unless the user agrees to file the answer.
- Never present general knowledge as if the wiki said it.
