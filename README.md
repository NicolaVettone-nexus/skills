# React + Vite + Next.js — Senior Skill (UI/UX + Performance + A11y)

A practical, senior-level **Cline Skill** for building modern web apps with **React**, **Vite**, and **Next.js App Router**—with strong defaults for **architecture**, **performance**, **accessibility**, **testing**, and **UI/UX product quality**.

This skill is designed to:
- Guide real engineering decisions (trade-offs included)
- Produce concrete outputs (patches, file changes, checklists)
- Stay current via an **official-sources sync workflow** (React/Next/Vite)

---

## What’s inside

```
skills/react-vite-next-senior/
├── SKILL.md
├── references/
│   ├── react_best_practices.md
│   ├── vite_best_practices.md
│   ├── next_app_router_best_practices.md
│   ├── performance_checklists.md
│   ├── ui_ux_playbook.md
│   ├── accessibility_playbook.md
│   ├── testing_playbook.md
│   ├── frontend_best_practices.md   (optional umbrella doc)
│   └── release_sources.md
└── scripts/
    ├── audit_frontend.sh
    └── sync_sources.py
```

### Key capabilities
- **React best practices** (component design, state, effects, performance, TypeScript)
- **Vite best practices** (build, deps, code splitting, assets, testing)
- **Next.js App Router best practices** (server-first, RSC boundaries, routing UX)
- **Performance playbook** (budgets, CWV-oriented checklists, profiling discipline)
- **UI/UX standards** (forms, feedback states, microcopy, motion, consistency)
- **Accessibility playbook** (keyboard-first, focus, dialogs, forms, testing)
- **Testing strategy** (unit → component → integration → E2E)

---

## Requirements
- VS Code
- Cline extension
- **Skills enabled** in Cline settings
- Optional (for scripts):
  - Node.js (project runtime)
  - Python 3.x (for `sync_sources.py`)
  - Bash shell (for `audit_frontend.sh`)

---

## Installation

### Option A — Project-level (recommended)
Copy the skill into your repository:

```
YOUR_REPO/
└── .cline/
    └── skills/
        └── react-vite-next-senior/
            ├── SKILL.md
            ├── references/
            └── scripts/
```

Then reload VS Code (**Developer: Reload Window**) so Cline can pick it up.

### Option B — Global install
Place it in your user skill folder:

- macOS/Linux: `~/.cline/skills/react-vite-next-senior/`
- Windows: `C:\Users\<you>\.cline\skills\react-vite-next-senior\`

---

## How to use in Cline (the important part)

### 1) Explicit invocation (best for reliability)
In your prompt, call the skill by name:

> Use the skill `react-vite-next-senior`.  
> Task: refactor `FeatureX` to improve performance and UI consistency.  
> Constraints: TypeScript, Tailwind, no new dependencies.  
> Output: patch-ready code + a11y checklist + tests.

### 2) Reference-driven usage
You can steer the model to specific docs:

- “Use `references/ui_ux_playbook.md` to redesign this form flow.”
- “Follow `references/performance_checklists.md` to optimize this route.”
- “Apply `references/next_app_router_best_practices.md` to reduce client JS.”

### 3) Verification prompt (if you want confirmation)
Ask Cline to explicitly commit to the skill context before working:

> Before you start, confirm you are using `react-vite-next-senior` and list which references you will apply.

---

## Example prompts

### Feature build (Vite + React)
> Use `react-vite-next-senior`. Build a new “Customers” feature with CRUD, a table, filtering, and accessible forms. Provide folder structure + code files + tests.

### Next.js App Router refactor (Server-first)
> Use `react-vite-next-senior`. Refactor this page to be Server-first. Minimize `"use client"` and keep client components leaf-level. Include loading/error/not-found states.

### UI/UX upgrade for a form
> Use `react-vite-next-senior`. Redesign the onboarding form flow using `ui_ux_playbook.md` and `accessibility_playbook.md`. Include empty/loading/error states and focus management.

### Performance review
> Use `react-vite-next-senior`. Run a performance-oriented code review: identify re-render hot spots, bundle risks, and CWV issues. Suggest concrete code changes.

---

## Scripts

### `scripts/audit_frontend.sh`
A quick local audit for a project directory.

Run:
```bash
bash scripts/audit_frontend.sh /path/to/project
```

What it does (depending on project scripts):
- installs deps (npm/yarn/pnpm)
- runs `lint`, `test`, `build` if available
- prints actionable suggestions

### `scripts/sync_sources.py`
Tracks changes on official React/Next/Vite pages via snapshots/hashes and generates a report.

Run:
```bash
python scripts/sync_sources.py
```

Output:
- `references/.sync/REPORT.md` with detected changes
- updated snapshots/hashes under `references/.sync/`

---

## Keeping the skill up to date
This skill includes `references/release_sources.md` as the source of truth.

Recommended approach:
- run the sync weekly (GitHub Action)
- open a PR when sources change
- update the relevant reference docs + “Upgrade Notes” sections

---

## Contributing
PRs welcome:
- Clarify rules with examples
- Add checklists for common patterns (tables, modals, dashboards)
- Improve migration guidance for major releases
- Add real-world “before/after” refactors

---

## License
Choose a license that matches your repo (MIT is a common default).
