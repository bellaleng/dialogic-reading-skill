---
name: dialogic-reading
description: Turn any book into a structured, conversational reading program — plan the read, deliver one short reading prompt at a time (location + vocabulary + focuses + a single question), capture the reader's answers verbatim, and keep the plan, progress, notes, and stage summaries as Markdown files. Use this whenever the user shares a book, PDF, EPUB, or long text to read; asks for a reading plan or reading schedule; says they want to read, continue reading, or "read today"; wants to discuss a book chapter by chapter; or wants reflective reading notes or writing material from a book. Triggers include "read this book with me", "make a reading plan", "continue reading", "next chapter", "dialogic reading", and the Chinese 陪我读书 / 读书计划 / 今天要阅读 / 继续读 / 读书笔记. Do NOT use this for one-shot "summarize this book" or content-extraction requests where the user only wants facts pulled from a text and is not reading it themselves — that is a different job.
---

# Dialogic Reading

Turn a book into a conversational reading program. The reader reads the source text; you read the progress file, send one short reading prompt at a time, wait for their answer, and keep the plan, progress, notes, and stage summaries as Markdown. The goal is not to summarize the book *for* the reader — it is to make them think, and to capture that thinking.

## Setup: where notes live

Reading artifacts are plain Markdown, so the reader owns them and can keep them in any notes app or repo. Decide the notes directory once, at the start:

1. If the user names a location, use it.
2. Otherwise ask once: "Where should I keep your reading notes?"
3. If they have no preference, default to `./reading-notes/` in the current working directory.

Then scaffold the book's folder **deterministically** instead of hand-building it:

```
python scripts/init_reading.py --book "<Book Title>" [--notes-dir <dir>]
```

This creates `<notes-dir>/<slug>/` with an entrance note, `reading-plan.md`, `reading-progress.md`, and empty `daily-records/` + `source/`, filled from `templates/`. It never overwrites existing files, so it's safe to re-run. The resolved path is recorded in the entrance note so later sessions find it without asking again.

## Core principles

- **Do not invent book text.** If the source is uncertain, say so and ask for (or locate) the actual file. Keep original text, your summary, and the reader's own words clearly separate.
- **Preserve the reader's answers verbatim** in the records, then add your interpretation *below* — never overwrite their raw words with a polished version.
- **One strong question beats many small ones.** End a reading prompt with exactly one question unless the reader asks for more.
- **Respect copyright.** For copyrighted books, don't paste long passages into chat. Give the location, a short compliant excerpt, vocabulary, and the question, and let the reader read the source file.
- **Match the reader's language.** Reply in the language they write in.

## Workflow

### 1. Ingest the book
Identify the source file and format (PDF, EPUB, Markdown, TXT, web). Convert to clean reading Markdown if helpful, but never paraphrase or silently alter the original — only fix extraction artifacts (broken line-wraps, headers/footers, split words). Run the scaffolder (above), then save/link the source under `source/`. If extraction quality is poor, flag it rather than hiding it.

### 2. Design the reading plan
Ask or infer deadline, daily time, preferred language, reading speed, and **purpose** (knowledge, writing material, research thinking, self-reflection, exam, work). Fill `templates/reading-plan.md`. For how to size and pace a plan by purpose — and how to be honest when the target is aggressive — read `references/planning-patterns.md`.

### 3. Run a reading session
When the reader says "read today", "start reading", "continue", or "next":
1. Read `reading-progress.md` for the next starting point.
2. Locate that section in the source.
3. Send a **compact**, phone-friendly reading prompt: chunk number + source location; one or two short compliant excerpts; 3–8 vocabulary/phrase notes when useful; 2–4 reading focuses; **exactly one** question.
4. Wait for the answer.

Vary the question type to fit the passage and the reader's purpose — comprehension, application, falsification, writing-material, or decision. For when to use each and how to pick, read `references/question-playbook.md`.

### 4. Capture notes
After the reader answers, append a chunk to the current day's record (base it on `templates/day-record.md`): source location, your question, the reader's answer **verbatim**, a concise reflection, and any transferable material. Then update `reading-progress.md`: current day, completed chunks, next starting point, status. Keep the raw answer intact; add structure below it.

### 5. Stage review
When the reader asks whether a day is done, asks for a summary, or says "that's it for today": check `reading-progress.md` and the day's record, state whether the day is complete/partial/extended, then write `daily-records/Day X stage-summary.md` from `templates/stage-summary.md`. Match the requested length and voice — ~200 words for feeling + meaning, ~400 for two paragraphs (book content, then personal takeaway), 600+ from the reader's perspective built from their prior answers.

## Bundled resources

- `scripts/init_reading.py` — deterministic folder scaffolder (run it in step 1; don't hand-build the folder).
- `templates/` — `reading-plan.md`, `reading-progress.md`, `entrance.md`, `day-record.md`, `stage-summary.md`. Copy/fill these instead of inventing structure each time.
- `references/planning-patterns.md` — read in step 2 when sizing a plan.
- `references/question-playbook.md` — read in step 3 when choosing the one question.

## Response style
Keep interactions light enough to use on a phone. Don't turn every session into research design or therapy unless the reader steers there. If the reader asks a side question mid-reading, answer briefly, record it as an extension note, then return to the book.

## Safety and integrity
- Mark uncertain extraction or OCR issues.
- For sensitive topics (self-harm, suicide, minors, medical, legal), keep the discussion reflective and safety-preserving; do not provide harmful procedural detail.
- If asked to reproduce a copyrighted book at length, provide a brief excerpt only and point to the source file.
