# QWEN.md

Use this file when Qwen works inside `skills-library`.

## Purpose

Protect the local skill library from accidental drift or duplication.

## Instructions

- Treat this repo as the canonical editable library.
- Read `shared\\model-guides\\COWORK.md` first.
- Keep edits minimal and structured.
- Prefer extending an existing skill over creating a duplicate.
- Do not write changes directly into `C:\Users\iwana\.codex\skills` unless the user explicitly asks for live deployment.

## Deployment Rule

Only sync to live Codex when asked:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

