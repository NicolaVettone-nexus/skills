# React Best Practices (Senior)

This playbook applies to:

- React apps built with **Vite** (SPA)
- **Next.js Client Components** (anything under `"use client"`)

Goal: correctness, maintainability, and real performance (not micro-optimizations).

---

## 1) Architecture and boundaries

### Recommended layering

- `ui/` presentational components (mostly stateless)
- `features/` use-case orchestration (hooks + components)
- `domain/` types + pure business rules (no React imports)
- `data/` API clients, fetchers, query keys, mappers
- `shared/` cross-cutting utilities (strictly curated)

**Rule:** UI should not know networking details. Domain should not know UI details.

### Folder rules of thumb

- Put “what” near “where it’s used” (feature folders are fine).
- Extract to shared libraries only after real reuse emerges.
- Prefer **explicit imports** over deep barrel “magic” for critical modules.

---

## 2) Component design: composition over configuration

### Prefer

- small, composable components
- “headless logic” (hooks) + thin view components
- clear prop APIs with semantic naming
- one responsibility per component

### Avoid

- boolean-prop explosions (`isFoo`, `isBar`, `isBaz` combinatorics)
- “god components” doing data fetching + state + UI + effects
- passing `any` or overly generic props to “make it flexible”

### Patterns that scale

- **Controlled vs uncontrolled** inputs: be explicit.
- **Compound components** when you own both parent/child and need shared context.
- **Slot-like APIs** (`header`, `footer`, `actions`) to avoid deeply nested children.

---

## 3) State management: keep state minimal and local

### Decision order

1. Can this be derived from props/data? → **don’t store it**
2. Is it local UI state? → `useState` in the leaf component
3. Is it shared between close siblings? → lift one level
4. Is it cross-feature global? → store (Zustand/Redux), but keep small
5. Is it server state? → React Query/SWR (cache + invalidation)

### Anti-patterns

- duplicating server state in global stores
- storing derived values (`filteredList`, `computedTotals`) without strong reasons
- global state for simple UI toggles

---

## 4) Side effects: predictable and testable

### Prefer

- effects that are **event-driven** (user actions) over time-driven
- isolating effects in custom hooks (`useSomethingEffect`)
- `AbortController` for request cancellation

### Avoid

- `useEffect` that “synchronizes” lots of state (often means wrong model)
- chained effects that depend on each other in subtle ways

**Rule:** if an effect exists just to compute state, remove it and compute directly.

---

## 5) Rendering performance: fundamentals first

### Most performance wins come from:

- fewer components doing work
- smaller re-render surfaces
- stable boundaries

### Practical rules

- Avoid creating new objects/functions in hot paths if it causes prop churn.
- Push expensive computations into:
  - memoized selectors (React Query)
  - `useMemo` **only** where measured and meaningful
- Prefer splitting into smaller components over `useMemo` on a monolith.

### Memoization guidance

Use `React.memo` / `useMemo` / `useCallback` **only when**:

- you verified re-renders are the bottleneck (React DevTools Profiler)
- the computation is expensive or triggers heavy child trees
- props are stable enough to benefit

Avoid premature memoization—it often makes code worse.

---

## 6) Lists and keys

### Keys

- Use stable IDs from data.
- Never use array index as key if list can reorder/insert/remove.

### Virtualization

For large lists/tables:

- virtualize rows (e.g., react-virtual)
- paginate or server-side filter/sort
- avoid rendering off-screen content

---

## 7) Forms: treat forms as a product feature

### Best practices

- proper labels, descriptions, and error messages
- validation that is:
  - immediate for simple constraints (required/format)
  - deferred for expensive checks (server uniqueness)
- focus management (first invalid field)
- avoid “submit did nothing” states—always show feedback

### Form libraries

- Use a form library when complexity demands it (multi-step, dynamic fields).
- Keep input components accessible and consistent.

---

## 8) Error handling

### UI error strategy

- local errors for local actions (inline messages)
- global errors for global failures (toasts, banners)
- always include:
  - what happened
  - what user can do next
  - how to recover/retry

### Dev strategy

- log errors with context (route, user action, correlation id where possible)
- use error boundaries in complex UI areas

---

## 9) Accessibility essentials (React-side)

- Use semantic HTML first.
- Ensure keyboard navigation works end-to-end.
- Don’t trap focus in modals.
- Respect `prefers-reduced-motion`.
- Never rely on color alone for meaning.

(See `accessibility_playbook.md` for a full checklist.)

---

## 10) TypeScript in React

- Prefer narrow types and discriminated unions.
- Avoid `any` as “escape hatch” unless strictly justified.
- Use `satisfies` for config objects to keep inference.
- Export component prop types only when needed; keep local by default.

---

## 11) Code review checklist (React)

- Clear responsibility boundaries (UI vs data vs domain)
- No duplicated derived state
- Stable keys for lists
- Accessibility and keyboard flows
- Measured performance claims
- Tests cover behavior, not implementation

---

## Upgrade Notes (maintainers)

Keep this section updated after official releases:

- **React 19**: confirm patterns align with official guidance.
- **React 19.2**: document any changes that affect app patterns.
- **React Compiler**: document when/where to enable and what it changes in code review expectations.
