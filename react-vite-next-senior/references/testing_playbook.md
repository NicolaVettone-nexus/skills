# Testing Playbook (Senior)

Test behavior, not implementation details.

---

## 1) Testing pyramid (practical)

- Unit tests: pure functions, domain rules
- Component tests: user-facing behavior (Testing Library)
- Integration tests: key flows across components
- E2E tests: critical journeys (Playwright)

---

## 2) Unit tests (domain)

- Keep domain logic framework-free
- Use table-driven tests for edge cases
- Assert invariants and error handling

---

## 3) Component tests

- Test user outcomes:
  - what user sees
  - what user can do
- Avoid testing internal hooks or component structure
- Mock network at boundary (MSW recommended)

---

## 4) Integration tests

- Cover:
  - form submission flows
  - auth + permissions
  - error + retry flows
- Ensure tests are deterministic and fast enough for CI

---

## 5) E2E tests

- Pick “money flows”
- Keep them stable:
  - seed data
  - predictable selectors
- Avoid testing every UI detail in E2E

---

## 6) What to test by default

- Rendering correctness for common states
- Loading/empty/error states
- Accessibility basics for forms and dialogs
- Permissions and conditional UI

---

## Code review checklist (tests)

- Tests read like user stories
- Good coverage of failure states
- Minimal mocking (mock boundaries, not internals)
- Fast enough to run on every PR
