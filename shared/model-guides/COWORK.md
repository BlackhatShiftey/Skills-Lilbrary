# COWORK.md

You are working inside the local skill library repo at:
`C:\Users\iwana\OneDrive\Documents\skills-library`

## Mission

Treat this repo as the source-of-truth for reusable agent skills and shared agent instructions.

## Hard Rules

- Edit skills in this repo, not in `C:\Users\iwana\.codex\skills`, unless the user explicitly asks you to patch the live install.
- Assume `C:\Users\iwana\.codex\skills` is a deployment target, not the master copy.
- Do not delete or overwrite the whole `codex/` folder.
- Do not rename skill folders casually. Stable names matter.
- Do not remove `SKILL.md`, `agents/openai.yaml`, `references/`, or `scripts/` from a skill unless the user explicitly asks.
- Do not create duplicate copies of the same skill under multiple names.
- Preserve Windows-friendly paths and PowerShell examples.

## Workflow

1. Inspect the existing skill or shared file first.
2. Make the smallest useful change.
3. Keep shared guidance vendor-neutral when possible.
4. If the change is Codex-specific, put it under `codex/`.
5. If the change is useful across multiple agents, put it under `shared/`.
6. Only sync to `C:\Users\iwana\.codex\skills` when the user wants the live install updated.

## Safety

- Never treat this repo as disposable scratch space.
- Never run destructive git commands without explicit user approval.
- Never move the library folder without explicit approval.
- Never rewrite unrelated files while editing one skill.

## Codex Sync

To deploy updated Codex skills into the live install:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

To sync one skill only:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1 -SkillName seam-runtime
```

