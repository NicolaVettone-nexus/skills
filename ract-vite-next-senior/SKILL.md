---
name: react-vite-next-senior
description: Senior-level best practices for building modern, performant web apps with React + Vite and Next.js (App Router). Includes architecture, state, data-fetching, performance, accessibility, UI/UX, testing, and an always-up-to-date protocol driven by official release sources.
---

# React + Vite + Next.js — Senior Skill (UI/UX + Performance)

## When to use this skill

Use this skill when:

- building features with React (Vite SPA) or Next.js App Router
- deciding SSR/SSG/ISR/RSC boundaries
- optimizing Core Web Vitals, bundle size, rendering performance
- establishing a design system and UI/UX best practices
- code review, refactors, migrations, and upgrades
- setting up testing, a11y, linting, conventions

## Operating principles (non-negotiables)

1. **Correctness > micro-optimizations**. Measure before optimizing.
2. **Minimize client JS** (especially in Next.js): keep components Server-first unless interaction is required.
3. **Stable architecture**: clear boundaries: UI / domain / data access.
4. **Accessibility is a feature**: keyboard-first, semantic HTML, WCAG-minded.
5. **Design system mindset**: consistency beats novelty.

## Decision guide: Vite vs Next.js

- Choose **Vite** when: SPA, heavy client interactivity, pure CSR, microfrontends, dashboards behind auth, you control caching with API + CDN.
- Choose **Next.js** when: SEO, SSR/SSG/ISR, streaming, RSC, route-level data loading, edge/runtime needs.

## Next.js App Router: Server/Client boundary

- Default: Server Components.
- Add `"use client"` ONLY for:
  - stateful UI (forms, local state)
  - event handlers
  - browser-only APIs
  - client-only libs (charts, maps, etc.)
- Keep client components leaf-level: “thin interactive wrapper, thick server data”.

## React 19+ patterns

- Prefer modern patterns and concurrency-friendly flows (transitions, optimistic UI).
- Avoid premature memoization; rely on clean component boundaries.
- For async UI, prefer framework conventions (Next route/loading) and idiomatic patterns.

## Performance playbook (quick checklist)

- Set budgets: route JS, LCP, INP, CLS.
- Split by route + component-level lazy only where it helps UX.
- Eliminate re-renders: stable props, avoid inline object/func props in hot paths.
- Analyze bundles regularly (see scripts/audit_frontend.sh).

## UI/UX best practices (baseline)

- Layout: 8px spacing system, consistent typographic scale.
- Forms: inline validation + clear error states + good focus management.
- Motion: subtle, purposeful, respects reduced-motion.
- Loading: skeletons where content structure is known; spinners only as last resort.
- Empty states: explain, offer next action.
- A11y: semantic first, ARIA only when needed, keyboard flows tested.

## References

- React: `references/react_best_practices.md`
- Vite: `references/vite_best_practices.md`
- Next: `references/next_app_router_best_practices.md`
- Perf checklists: `references/performance_checklists.md`
- UI/UX playbook: `references/ui_ux_playbook.md`
- Testing: `references/testing_playbook.md`
- A11y: `references/accessibility_playbook.md`

## Always-up-to-date protocol (mandatory for maintainers)

1. Use ONLY official release sources (listed in `references/release_sources.md`).
2. Run `python scripts/sync_sources.py` weekly (or via GitHub Action).
3. If new releases/docs changes detected:
   - update the relevant reference docs
   - update “Upgrade Notes” section in each reference
   - open PR with changelog summary and migration impact

## Scripts

- `bash scripts/audit_frontend.sh` — quick local audit (lint/test/build/analyze hooks)
- `python scripts/sync_sources.py` — pulls/compares official release sources and generates a TODO report
