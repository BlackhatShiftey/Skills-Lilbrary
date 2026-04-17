# GEMINI.md

Use this file when Gemini works inside `skills-library`.

## Primary Rule

This repo is the canonical library. The live Codex skills folder is only a deployed copy.

## Operating Instructions

- Read `shared\\model-guides\\COWORK.md` before changing files.
- Prefer precise edits over broad rewrites.
- Keep markdown simple and easy for other agents to parse.
- Keep model-neutral references in `shared\`.
- Keep Codex skill definitions in `codex\`.

## Avoid

- Avoid moving folders unless the user explicitly asks.
- Avoid editing both the library and the live install unless the user wants a sync.
- Avoid adding unnecessary docs that duplicate existing instructions.

## Deployment

If the user wants the Codex install updated, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

