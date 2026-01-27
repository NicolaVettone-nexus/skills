# Accessibility Playbook (Senior)

Accessibility is part of product quality, not a checklist at the end.

---

## 1) Baseline rules

- Use semantic HTML first.
- Every interactive element must be reachable by keyboard.
- Focus must always be visible.
- Never rely on color alone for meaning.

---

## 2) Keyboard navigation

- Tab order must follow visual order
- No focus traps (unless intentional modal trap)
- Escape closes dialogs
- Enter/Space activates buttons

---

## 3) Forms

- Labels are required (explicit `<label for=...>`)
- Errors must be associated with inputs
- Use `aria-invalid` when appropriate
- Provide clear instructions and examples

---

## 4) Dialogs and menus

- Dialogs must:
  - trap focus while open
  - restore focus to the opener on close
  - be closable via ESC
- Menus must be navigable by keyboard

---

## 5) Images and icons

- Decorative icons: `aria-hidden="true"`
- Meaningful icons: provide accessible name
- Images: meaningful `alt`, otherwise empty `alt=""`

---

## 6) Contrast and motion

- Ensure sufficient contrast for text and UI controls
- Respect `prefers-reduced-motion` (reduce/disable animations)

---

## 7) Testing process

- Keyboard-only smoke test (all critical journeys)
- Screen reader spot checks on key flows
- Automated checks (eslint-jsx-a11y, axe) are helpful but not enough

---

## A11y code review checklist

- Semantics: correct elements (`button` vs `div`)
- Focus management is correct
- Labels and errors are accessible
- No unreachable or hidden focus targets
- Visual contrast and motion respected
