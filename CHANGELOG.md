# Changelog

All notable changes to the `dialogic-reading` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow [SemVer](https://semver.org/).

## [1.0.0] — 2026-07-15

First public release.

### Added
- **Skill core** (`SKILL.md`): the six-step workflow — ingest the book, design the plan, run a session (one compact prompt: location + excerpt + vocabulary + focuses + one question), give feedback, capture verbatim notes, stage review.
- **Explicit decomposition procedure** (`references/planning-patterns.md`): map structure → measure load (minutes-per-page by genre) → compute days → assign sections → answer-based "done" → pre-cut chunks; concrete chunk-size numbers, a worked example, and mid-read re-planning rules.
- **Feedback playbook** (`references/feedback-playbook.md`): four fixed moves after every answer (mirror → check against the text → one deepening move → close/follow-up), a calibration table by answer quality, and hard limits (≤120 words, verbatim quotes, one correction max).
- **Question playbook** (`references/question-playbook.md`): five question types — comprehension, application, falsification, writing-material, decision — with picking heuristics.
- **Deterministic scaffolder** (`scripts/init_reading.py`): creates each book's notes folder from templates; safe to re-run, never overwrites.
- **Templates**: reading plan, reading progress, entrance note, day record, stage summary.

[1.0.0]: https://github.com/bellaleng/dialogic-reading-skill/releases/tag/v1.0.0
