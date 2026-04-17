---
name: awesome-design-md
description: Install and apply DESIGN.md inspirations from the Awesome Design MD collection through the getdesign CLI. Use when the user wants a project to look like a specific brand or product site, asks for a Vercel-like or Stripe-like interface, wants to add or swap a DESIGN.md file in a repo, or wants help choosing a design inspiration before generating UI.
---

# Awesome Design MD

Use this skill to bring a curated `DESIGN.md` into a project, then guide UI work against that design language.

The upstream GitHub repo now mostly points to `getdesign.md`, so the reliable workflow is CLI-first: list available brands, install the chosen design into the target repo, then tell Codex to use `DESIGN.md` for all UI work.

## Quick Start

1. Confirm the target brand or shortlist. If the user is undecided, read [references/brand-catalog.md](references/brand-catalog.md) or run:

```bash
python scripts/design_md.py list
```

2. Add the chosen design to the target project root, or to a specific output path:

```bash
python scripts/design_md.py add vercel
python scripts/design_md.py add stripe --out ./docs/DESIGN.md
```

3. Once the file exists, treat it as a hard design brief. Keep your implementation aligned to its palette, spacing, typography, component styling, and responsive rules.

## Workflow

### Choose the right source

- If the user names a brand directly, install that brand.
- If the user describes a vibe like "make it feel like Vercel, Stripe, Linear, or Notion", map that to the nearest design in [references/brand-catalog.md](references/brand-catalog.md).
- If the user wants a few options first, suggest 3 brands with one-line rationale, then proceed with the chosen one.

### Install the design

- Prefer the bundled helper script:

```bash
python scripts/design_md.py add <brand>
```

- The helper wraps:

```bash
npx getdesign@latest add <brand>
```

- Run from the repo root unless the user explicitly wants a different output path.
- Use `--force` only when replacing an existing `DESIGN.md` is clearly intended.

### Apply the design during implementation

- Read the generated `DESIGN.md` before writing UI code.
- Mirror its brand cues, but still respect the existing product structure and user goals.
- If the repo already has a strong design system, use the imported `DESIGN.md` as inspiration only where it does not conflict.
- When the user asks for a clone of a well-known brand, keep it "inspired by" rather than claiming official parity.

## Practical Rules

- Prefer one active `DESIGN.md` in the project root for the current design direction.
- If comparing multiple brands, install alternates into separate paths like `docs/designs/vercel.md` rather than overwriting the active file repeatedly.
- Preserve the user's existing UI architecture and component model; the design file should change presentation more than app structure.
- If `node` or `npx` is missing, pause and ask the user to install Node.js first.

## Good Fits

- "Make this landing page feel like Vercel."
- "Install a Stripe-inspired `DESIGN.md` in this repo."
- "Give me three good inspirations for a developer tools homepage."
- "Swap our current design brief to Linear and rebuild the hero section."

## Resources

- Brand catalog and selection notes: [references/brand-catalog.md](references/brand-catalog.md)
- CLI helper for listing and installing designs: [scripts/design_md.py](scripts/design_md.py)
