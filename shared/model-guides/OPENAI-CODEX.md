# OPENAI-CODEX.md

Use this file when Codex or another OpenAI coding agent works inside `skills-library`.

## Contract

This repo is the editable source-of-truth for custom skills.

- Source library: `C:\Users\iwana\OneDrive\Documents\skills-library`
- Live Codex install: `C:\Users\iwana\.codex\skills`

## Rules

- Make skill changes here first.
- Do not hand-edit the live install as the main workflow.
- Sync to the live install only when explicitly requested or when the task clearly includes deployment.
- Preserve existing skill metadata and resource layout unless there is a clear reason to change them.
- Keep reusable guidance in `shared\` and Codex deployment artifacts in `codex\`.

## Deploy To Live Codex

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

## Single Skill Deploy

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1 -SkillName awesome-design-md
```
