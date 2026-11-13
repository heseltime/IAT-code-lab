# Log

Append-only. Newest entry at the bottom. Format: `## [YYYY-MM-DD] <ingest|query|lint|schema> | <title>`.
Show the last five entries with:

```bash
grep "^## \[" wiki/log.md | tail -5
```

## [2026-11-13] schema | Set up the wiki

- Added: AGENTS.md, templates/, scripts/lint.sh, the three skills in .claude/skills/

## [2026-11-13] ingest | IAT neural networks notebook outline

- Added: sources/iat-nns-notebook-outline.md, concepts/linear-regression.md, concepts/loss-function.md,
  concepts/gradient-descent.md, concepts/computation-graph.md, concepts/neural-network.md
- Updated: index.md
- Open: Q1 (residuals or squared residuals?), Q2 (where is the MNIST script?) in open-questions.md

## [2026-11-13] ingest | IAT neural networks README

- Added: sources/iat-nns-readme.md
- Updated: all five concept pages (README as a second source), index.md
- Open: Q2 got a second, contradicting path from the README

## [2026-11-13] lint | First check

- `bash scripts/lint.sh`: 0 errors, 0 warnings
- Judgement checks: the two contradictions are recorded as Q1 and Q2. No fixes needed.
