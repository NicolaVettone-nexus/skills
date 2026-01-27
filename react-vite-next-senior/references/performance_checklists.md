# Performance Checklists (Senior)

Performance is a product feature. Measure with real metrics.

---

## A) Metrics and budgets

### Core Web Vitals (high-level)

- LCP: fast meaningful content
- INP: responsiveness
- CLS: stability

### Budgets

Define per route:

- max JS shipped
- max number of requests
- max image weight
- max time-to-interactive target (context-dependent)

---

## B) Quick wins checklist

- Remove unused dependencies
- Reduce client JS:
  - Next: server-first, client leaf-only
  - Vite: route-level splitting, avoid heavy libs
- Avoid re-render storms:
  - split components
  - reduce prop churn
- Optimize assets:
  - compress images
  - lazy-load offscreen
- Avoid layout shifts:
  - fixed dimensions
  - predictable skeletons

---

## C) React-specific checklist

- Stable keys
- Avoid derived state duplication
- Avoid expensive work in render
- Profile before memoizing
- Virtualize large lists

---

## D) Next-specific checklist

- Confirm server/client boundary is minimal
- Ensure route-level loading states exist
- Avoid forcing client rendering for whole pages
- Ensure caching strategy is intentional

---

## E) Runtime checklist

- Remove debug logs and dev-only toggles in prod
- Ensure error logging has context
- Monitor in production (RUM if possible)

---

## F) How to run performance reviews

1. Choose a representative user journey
2. Measure baseline (DevTools + profiler + lighthouse)
3. Apply one change at a time
4. Measure again
5. Document impact and trade-offs
