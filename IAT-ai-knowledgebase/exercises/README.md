# Exercises

Hands-on tasks, from "look around" to "build your own skill". Each one takes 15–45 minutes. The session numbers
follow the [Coding Lab curriculum](../../README.md#the-programme).

You need: this repository open in VS Code, a terminal, and Claude Code (`claude` in the terminal, started in the
repository folder). Write your answers in a notebook or a file outside `wiki/`.

## Session 1–2: understand the pattern

### 1. Explore the example wiki (15 min)

1. Open [`wiki/index.md`](../wiki/index.md). Click through to two concept pages.
2. Open [`raw/iat-nns-notebook-outline.md`](../raw/iat-nns-notebook-outline.md). It is in German. Compare it with
   [`wiki/sources/iat-nns-notebook-outline.md`](../wiki/sources/iat-nns-notebook-outline.md).
3. Answer: which layer did a human write, and which did the agent write? Where are the rules the agent follows?

### 2. Ask the wiki (15 min)

In Claude Code, ask:

```text
What does the wiki say about gradient descent? Explain it like I'm 12.
```

```text
Make a 5-question quiz about how neural networks learn, using only the wiki. Put the answers at the end.
```

Check: did the answer link to wiki pages? Then ask something the wiki doesn't cover (e.g. "What is a transformer?").
What does the agent say?

### 3. Find the contradictions (15 min)

Read [`wiki/open-questions.md`](../wiki/open-questions.md). Then run:

```bash
bash scripts/lint.sh
```

Why can the script **not** find the two open questions? What kind of check needs an LLM, and what kind
doesn't?

## Session 2: your own topic

### 4. Your first ingest (30 min)

1. Pick a school subject. Write or collect a page of notes (your own notes, a worksheet you're allowed to share, a
   Wikipedia article saved as text).
2. Save it as `raw/<date>-<subject>-<topic>.md`.
3. In Claude Code: `ingest raw/<your file>`.
4. Read every page the agent wrote. Is anything wrong or made up? Tell it and let it fix the page.
5. Run `bash scripts/lint.sh`. It should say 0 errors.

### 5. A second source that disagrees (30 min)

Find a second source on the same topic, ideally one that says something slightly different (another textbook,
your teacher's slides, a video transcript). Ingest it. Did the agent update the existing pages? Did it add an
open question?

### 6. Change the schema (20 min)

Your wiki might need a new page type, e.g. `people/` for historical persons, or `formulas/` for physics. Ask the
agent to propose a change to [`AGENTS.md`](../AGENTS.md) and a new template. Discuss it before you accept it.

## Session 3 (lab block): build on it

### 7. Write your own skill (45 min)

The curriculum asks for at least one skill of your own. Ideas:

- **`wiki-quiz`**: make a quiz from the wiki and file the result in `wiki/answers/`.
- **`wiki-cheatsheet`**: one page with every formula or date in the wiki, before a test.
- **`wiki-flashcards`**: export the concept pages as question/answer pairs (e.g. CSV for Anki).

Copy one of the skills in [`.claude/skills/`](../.claude/skills/) as a starting point. A skill is a folder with a
`SKILL.md`: a short `description` (when to use it) and the steps. Test it, then improve the description until
Claude picks it up by itself.

### 8. Bonus: a scheduled task

Think of something that should run regularly, e.g. a weekly lint, or "every Sunday, make a summary of what I added
this week". Write it down as a plan: what runs, when, and what it changes.

## Session 4: think about the architecture

- The wiki has no database and no vector search: `index.md` plus `grep`. When would that stop working?
  (Karpathy says it works up to about 100 sources and a few hundred pages.)
- The links between pages form a **graph**. Open the folder in [Obsidian](https://obsidian.md) and look at the
  graph view. Which pages are hubs? Which are orphans?
- Compare with a knowledge graph or the Open Knowledge Format from the curriculum. What would you gain? What would
  you lose?
- Big projects often record **decisions**: what was decided, why, and which other options there were. Could your
  wiki have a `decisions/` folder, for example for your lab project? What rules would it need? (Hint: should an old
  decision ever be deleted?)
