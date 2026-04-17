---
name: seam-runtime
description: Work on the local SEAM runtime project at C:\Users\iwana\OneDrive\Documents\Codex. Use when editing MIRL compilation, runtime orchestration, retrieval, storage, symbol promotion, vector adapters, CLI behavior, tests, or repo-specific documentation for the SEAM codebase.
---

# Seam Runtime

Use this skill when a task touches the SEAM repository or asks about MIRL, PACK, retrieval, symbol promotion, or the `seam.py` CLI.

This skill is repo-aware. Start from the shared project docs in the repo, then inspect the relevant runtime modules before editing.

## Start Here

1. Read `C:\Users\iwana\OneDrive\Documents\Codex\AGENTS.md`
2. Read `C:\Users\iwana\OneDrive\Documents\Codex\docs\PROJECT_MAP.md`
3. Read `C:\Users\iwana\OneDrive\Documents\Codex\docs\COMMANDS.md`
4. Read `C:\Users\iwana\OneDrive\Documents\Codex\docs\CONVENTIONS.md`

Use [references/project-paths.md](references/project-paths.md) for the exact local paths and related deep-dive docs.

## Routing

- CLI behavior: inspect `seam.py` and `seam_runtime/cli.py`
- Runtime composition: inspect `seam_runtime/runtime.py`
- MIRL schema or IR verification: inspect `seam_runtime/mirl.py`, `seam_runtime/verify.py`, `docs/MIRL_V1.md`
- Retrieval or ranking changes: inspect `seam_runtime/retrieval.py`, `seam_runtime/vector.py`, `seam_runtime/vector_adapters.py`, `docs/RETRIEVAL_EVAL_V1.md`
- Symbol compaction and export: inspect `seam_runtime/symbols.py`, `docs/SYMBOL_NURSERY.md`
- Embeddings and providers: inspect `seam_runtime/models.py`, `docs/SOP_MODEL_INTEGRATION.md`
- Persistence and trace behavior: inspect `seam_runtime/storage.py`

## Working Rules

- Keep terminology stable: `SEAM`, `MIRL`, `PACK`, symbol nursery
- Prefer small changes over broad rewrites
- Avoid editing checked-in `.db` files unless explicitly asked
- Preserve CLI verbs and machine-readable output shapes unless a task explicitly requires breaking changes
- When changing behavior, run the smallest relevant verification command first, then expand only if needed

## Verification

- Default test run:

```bash
python -m unittest test_seam.py
```

- CLI sanity check:

```bash
python seam.py --help
```

- If already inside `seam_runtime`, run:

```bash
python ..\seam.py --help
```

## Resources

- Repo paths and reference docs: [references/project-paths.md](references/project-paths.md)
