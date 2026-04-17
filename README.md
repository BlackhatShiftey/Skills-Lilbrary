# skills-library

Personal source-of-truth repo for reusable agent skills and shared instructions.

## Canonical Rule

This repository is the canonical source-of-truth for your custom skills.

- Edit skills here first: `C:\Users\iwana\OneDrive\Documents\skills-library`
- Treat `C:\Users\iwana\.codex\skills` as a deployed runtime copy for Codex
- Do not use the live Codex install as the master copy
- Sync changes into the live Codex install only when you want deployment

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
- That live install is a deployment target, not the source-of-truth.
- This repo does not affect the live install until you run the sync script.
- Keep project-specific truth in each project repo with files like `AGENTS.md`, `DESIGN.md`, and `docs\*.md`.
