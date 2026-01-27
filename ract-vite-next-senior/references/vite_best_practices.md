# Vite Best Practices (Senior)

This document is about building React apps with Vite as the bundler/dev server.

---

## 1) Project setup

### Recommended baseline

- TypeScript enabled
- ESLint + Prettier
- Vitest + Testing Library
- Playwright for E2E (optional but recommended)
- Environment separation via `.env` files

### Environment variables

- Use `import.meta.env` (Vite standard).
- Never ship secrets to the browser.
- Use typed env accessors to avoid stringly-typed bugs.

---

## 2) Build and performance

### Bundle discipline

- Establish a **bundle budget**:
  - route JS size
  - initial chunk size
  - third-party deps limits
- Avoid importing “kitchen sink” libraries.
- Prefer modular imports and lightweight alternatives.

### Code splitting

- Split by route (router-level lazy).
- Use component-level dynamic import only for heavy rarely-used UI.
- Avoid “split everything”: too many chunks can hurt.

### Dependency optimization

- If dev server is slow, review deps and Vite optimize behavior.
- Keep dependencies up to date; major upgrades often include perf improvements.

---

## 3) Asset strategy

- Use modern formats (SVG for icons, WebP/AVIF for images).
- Use a consistent icon system.
- Avoid huge unoptimized images in the repo.

---

## 4) CSS strategy (Tailwind or otherwise)

- If Tailwind:
  - keep design tokens consistent (spacing, typography, colors)
  - avoid inline style duplication
  - build reusable components for repeated patterns
- If CSS Modules:
  - avoid global leakage
  - name by component responsibility

---

## 5) Testing strategy for Vite apps

- Unit + component tests with Vitest
- Integration tests for critical flows
- E2E tests for business-critical user journeys

(See `testing_playbook.md`.)

---

## 6) Security basics (frontend)

- Never trust client input—validate server-side.
- Use strict CSP if applicable.
- Avoid unsafe HTML injection (XSS risk).
- Keep dependencies updated; audit regularly.

---

## 7) Common pitfalls

- Shipping debug flags and dev-only logs
- Large polyfills for modern-only environments (review browser support)
- Overusing `useEffect` “sync” patterns

---

## Upgrade Notes (maintainers)

- Track major Vite releases and migration notes.
- Update this doc when:
  - default behavior changes (dev server, build output)
  - recommended plugin patterns change
  - migration steps become required
