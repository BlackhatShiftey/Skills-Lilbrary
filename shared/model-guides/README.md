# Model Guides

Use these files as copy-paste or reference instructions for different coding agents that may touch `skills-library`.

## Core Rule

`skills-library` is the source-of-truth library.

- Edit skills here: `C:\Users\iwana\OneDrive\Documents\skills-library`
- Do not treat `C:\Users\iwana\.codex\skills` as the source-of-truth
- Only sync to the live Codex install on purpose with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

## Included Guides

- `CLAUDE.md`
- `GEMINI.md`
- `GROK.md`
- `OPENAI-CODEX.md`
- `QWEN.md`
- `COWORK.md`

