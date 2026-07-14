# Dialogic Reading — a Claude skill

Turn any book into a structured, **conversational** reading program.

You read the source text; Claude reads your progress file, sends you one short reading prompt at a time (location + vocabulary + focuses + **one** question), waits for your answer, and keeps the plan, progress, notes, and stage summaries as plain Markdown files you own.

It's built for reading that changes how you think — not for having a book summarized *at* you.

> 中文：把任何一本书变成「对话式」阅读计划。你读原文，Claude 按进度每次只给你一小段阅读提示（定位＋词汇＋阅读焦点＋一个问题），等你作答，并把阅读计划、进度、笔记、阶段总结都存成你自己的 Markdown 文件。

> **How it's different:** tools like [book-to-skill](https://github.com/virgiliojr94/book-to-skill) turn a book's *contents* into a reference the agent can query. This does the opposite side — it runs the *process* of reading, so **you** read and reflect and keep your own notes. The two are complementary.

## Why you'll like it

**You read the book. Claude runs the conversation.** One short prompt at a time, one question, notes you keep forever.

- 🗺️ **A plan that fits you** — built around your deadline, daily minutes, and *why* you're reading: knowledge, writing, research, reflection, or an exam.
- 📖 **One chunk at a time** — each session gives you location + vocabulary + focuses + a **single** question. Short enough to do on your phone.
- 🧠 **Questions that make you think** — application, falsification, and decision prompts pull the book into your own life and work, so what you read actually sticks.
- 💬 **Feedback that engages your answer** — every reply gets checked against the text: what you got right, what the passage adds, and one push deeper. Misreadings get corrected with the actual line, not waved through.
- ✍️ **Your words, kept verbatim** — answers saved exactly as you wrote them, with interpretation added below, ready to become essays, threads, or posts.
- 🔁 **Stage reviews** — per-day summaries: what the book says, what it changed in your thinking, and the reusable writing material you surfaced.
- 📂 **Plain Markdown you own** — works with Obsidian, a plain folder, or a git repo. Nothing leaves your machine.
- ⚙️ **Deterministic setup** — one script scaffolds each book's folder: no hand-building, no drift, safe to re-run.

## Install

The skill is the `dialogic-reading/` folder (a `SKILL.md` plus bundled scripts, templates, and references).

### Claude Code
Copy the folder into your skills directory:

```bash
# personal (all projects)
cp -r dialogic-reading ~/.claude/skills/

# or per-project
cp -r dialogic-reading /path/to/project/.claude/skills/
```

Start a new session. Then say things like *"read this book with me"*, *"make a reading plan for <file>"*, or *"continue reading"*.

### Claude.ai / Claude Desktop
Upload the `dialogic-reading` folder as a custom skill (Settings → Skills / Capabilities), or paste `SKILL.md` into a project's instructions.

## How to use

1. Give Claude a book file (PDF / EPUB / Markdown / text) and say you want to read it.
2. Answer its setup questions (deadline, daily time, purpose) — it builds a plan.
3. Each session: say *"continue"*, read the chunk it points you to, answer the one question.
4. Say *"that's it for today"* to get a stage summary.

On first use it asks **where to keep your notes** (any folder). If you don't care, it defaults to `./reading-notes/`.

## Example walkthrough

A 3-day read of *The Book of Elon*, for writing material, ~30 min/day. This shows **what Claude asks and produces** — the reading prompts, the files it keeps, the summaries. Your own answers are yours; they live as local Markdown and are not shown here.

**You:** I've got `The Book of Elon.pdf` in `~/Downloads`. Read it with me over 3 days — I want writing material, about 30 minutes a day.

**Claude** *(ingests the PDF, asks about purpose and pace, then writes a plan):*
> Plan saved. 3 days — **Day 1** Part I (Purpose) · **Day 2** Part II (Execution) · **Day 3** Parts III–IV (Companies + Future). A "session" = one part; "done" = you've answered its chunks. Notes will live in `./reading-notes/the-book-of-elon/`. Say **"continue"** when you're ready.

**You:** continue

**Claude** — a compact, phone-friendly reading prompt, always ending in one question:
> 📖 **Day 2 · Chunk 1** — Part II / *Take Responsibility* (p. 87)
> Short excerpt: *"What you actually get as CEO is a distillation of the worst things going on in the company."*
> **Vocabulary:** *distillation* — the concentrated essence of something; *pernicious* — quietly harmful.
> **Focus:** (1) how he redefines what leadership actually *gives* you; (2) the rule "spend time only on things that are going wrong — the ones others can't fix."
> **One question:** Where in your own work do you spend time on things that are already *going right*, instead of the hard thing only you can do?

*(You answer in your own words. Claude first responds to your answer — names what's strong in it, checks it against the passage, pushes one step deeper — then saves it verbatim with a short reflection in `daily-records/Day 2 record.md` and advances `reading-progress.md` to the next chunk.)*

**You:** that's it for today

**Claude** *(writes `daily-records/Day 2 stage-summary.md`):*
> **Day 2 — Execution.** Part II's throughline: execution is the bottleneck, not ideas. The summary captures what the read portion argues, how your answers connected it to your own work, and reusable writing hooks. Next start: Day 3, Part III.

You end up with a folder of Markdown you own — plan, progress, your verbatim answers, and per-day summaries you can later turn into essays or posts.

> 中文：以《The Book of Elon》为例，3 天读完、每天约 30 分钟。示例只体现**Claude 会问什么、产出什么**：你说「继续」，它给你一小段（定位＋摘录＋词汇＋阅读焦点＋一个问题）；你用自己的话作答（答案只在你本地，不在示例里展示），它把你的原话和解读记进当天记录并推进进度；你说「今天到这」，它写出当天的阶段总结。

## What's in the skill

```
dialogic-reading/
├── SKILL.md                     # the workflow Claude follows
├── scripts/
│   └── init_reading.py          # scaffolds a book's notes folder (deterministic, no overwrite)
├── templates/                   # reading-plan / progress / entrance / day-record / stage-summary
└── references/
    ├── planning-patterns.md     # decomposition procedure: book → days → chunks, with re-planning rules
    ├── question-playbook.md     # the five question types and when to use each
    └── feedback-playbook.md     # the four feedback moves after every answer, calibrated to answer quality
```

Progressive disclosure keeps it light: Claude sees only the name + description until the skill triggers, loads `SKILL.md` when it does, and reads a reference file only when it needs it.

## Files it creates

```
<notes-dir>/<book-name>/
├── README - entrance.md
├── reading-plan.md
├── reading-progress.md        # "where am I" — single source of truth
├── daily-records/
│   ├── Day 1 record.md         # your answers, verbatim + interpretation
│   └── Day 1 stage-summary.md
└── source/                     # optional: the book file / cleaned Markdown
```

## Privacy

All reading artifacts are local Markdown files. The skill contains no personal data and no hardcoded paths — it asks you where notes should go.

## License

MIT — see [LICENSE](./LICENSE).
