# GROK.md

Use this file when Grok works inside `skills-library`.

## Ground Truth

`C:\Users\iwana\OneDrive\Documents\skills-library` is the master repo.

## Rules

- Edit here first.
- Keep changes targeted.
- Preserve existing skill names and directory layout.
- Treat `C:\Users\iwana\.codex\skills` as a synced output, not the source.
- Do not freestyle a new structure unless the user explicitly asks.

## Good Behavior

- Read the current skill before editing it.
- Update the smallest number of files needed.
- Keep instructions direct and executable.
- Use the sync script only when the user wants live Codex updated.

## Sync Command

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-codex-skills.ps1
```

