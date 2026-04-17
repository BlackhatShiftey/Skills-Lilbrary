# skills-library

Personal source-of-truth repo for reusable agent skills and shared instructions.

## Layout

- `codex/`: Codex skill folders that can be synced into `~/.codex/skills`
- `shared/`: vendor-neutral notes, templates, and references for multiple agents
- `scripts/`: helper scripts for syncing or maintaining installed skills

## Current workflow

1. Edit custom Codex skills in this repo.
2. Sync them into the live Codex install with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

3. Restart Codex after changing installed skills.

## Notes

- The live Codex install remains in `C:\Users\iwana\.codex\skills`.
- This repo does not affect the live install until you run the sync script.
- Keep project-specific truth in each project repo with files like `AGENTS.md`, `DESIGN.md`, and `docs\*.md`.

