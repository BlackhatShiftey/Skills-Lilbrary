# CLAUDE.md

Use this file when Claude works inside `skills-library`.

## Role

Treat `skills-library` as the master library for reusable skills and agent instructions.

## Do

- Read `shared\\model-guides\\COWORK.md` first.
- Edit files in this repo as the canonical source.
- Keep changes clean, small, and reviewable.
- Put Codex-only skills under `codex\`.
- Put cross-agent guidance under `shared\`.
- Preserve folder structure inside each skill.

## Do Not

- Do not treat `C:\Users\iwana\.codex\skills` as the source-of-truth.
- Do not silently sync live Codex skills unless asked.
- Do not replace a whole skill when only one file needs editing.
- Do not create duplicate skills with nearly identical names.

## If Asked To Update Live Codex Skills

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

## Preferred Behavior

When unsure, ask whether the user wants:
- library-only changes
- live Codex sync too
- both

