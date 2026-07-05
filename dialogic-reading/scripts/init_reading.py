#!/usr/bin/env python3
"""Scaffold a dialogic-reading notes folder for one book.

Deterministic setup so the model doesn't hand-build the same folder each time.

Usage:
    python scripts/init_reading.py --book "The Book of Elon"
    python scripts/init_reading.py --book "Deep Work" --notes-dir ~/reading-notes
    python scripts/init_reading.py --book "Thinking, Fast and Slow" --slug tfs

Creates <notes-dir>/<slug>/ with an entrance note, reading-plan, reading-progress,
and empty daily-records/ + source/ folders, filled from ../templates/.
Never overwrites an existing file. Stdlib only.
"""
import argparse
import datetime
import re
from pathlib import Path


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "book"


def main() -> None:
    ap = argparse.ArgumentParser(description="Scaffold a dialogic-reading notes folder for one book.")
    ap.add_argument("--book", required=True, help="Book title (used in files and as the folder name)")
    ap.add_argument("--notes-dir", default="./reading-notes", help="Base notes directory (default: ./reading-notes)")
    ap.add_argument("--slug", help="Folder name (default: slugified title)")
    args = ap.parse_args()

    script_dir = Path(__file__).resolve().parent
    templates = script_dir.parent / "templates"
    slug = args.slug or slugify(args.book)
    date = datetime.date.today().isoformat()
    book_dir = (Path(args.notes_dir).expanduser() / slug).resolve()

    subst = {
        "{{BOOK_TITLE}}": args.book,
        "{{DATE}}": date,
        "{{SLUG}}": slug,
        "{{NOTES_PATH}}": str(book_dir),
    }

    (book_dir / "daily-records").mkdir(parents=True, exist_ok=True)
    (book_dir / "source").mkdir(parents=True, exist_ok=True)

    # template file -> output filename in the book folder
    to_render = {
        "entrance.md": "README - entrance.md",
        "reading-plan.md": "reading-plan.md",
        "reading-progress.md": "reading-progress.md",
    }

    created, skipped = [], []
    for tpl_name, out_name in to_render.items():
        dest = book_dir / out_name
        if dest.exists():
            skipped.append(out_name)
            continue
        text = (templates / tpl_name).read_text(encoding="utf-8")
        for key, val in subst.items():
            text = text.replace(key, val)
        dest.write_text(text, encoding="utf-8")
        created.append(out_name)

    print(f"Reading folder: {book_dir}")
    for name in created:
        print(f"  created  {name}")
    for name in skipped:
        print(f"  skipped  {name} (already exists)")
    print('\nNext: drop the book file in source/ (optional), then start a session — say "continue".')


if __name__ == "__main__":
    main()
