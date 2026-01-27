# UI/UX Playbook (Senior)

This is a pragmatic UI/UX standard for product-grade web apps.

---

## 1) Design system fundamentals

### Consistency rules

- spacing scale (e.g., 4/8 system)
- typography scale (few sizes, consistent line-height)
- color tokens (semantic: primary/success/warn/danger)
- component states (default/hover/active/disabled/focus)

### Component library strategy

- Prefer a small set of primitives (Button, Input, Modal, Table)
- Build complex components by composing primitives
- Document usage + do/don’t examples

---

## 2) Interaction design: states matter

### Always design:

- Loading state
- Empty state
- Error state
- Success/confirmation state

### Loading

- Use skeletons when layout is known (perceived performance)
- Use spinners when structure is unknown or action is short
- Prevent layout shifts

### Empty states

- Explain why it’s empty
- Offer a clear next action (“Create”, “Import”, “Learn more”)

### Errors

- Use plain language
- Explain recovery steps
- Offer retry
- Don’t blame the user

---

## 3) Forms: high-leverage UX area

- Clear labels (not placeholders as labels)
- Inline validation with helpful messages
- Preserve user input on errors
- Focus the first invalid field on submit
- Support keyboard-only completion
- Don’t show destructive actions as primary

---

## 4) Navigation and information architecture

- Keep navigation stable and predictable
- Prefer shallow hierarchies
- Use breadcrumbs only if genuinely helpful
- Avoid hiding core actions behind 3+ layers

---

## 5) Microcopy and feedback

- Action labels should describe the outcome (“Save changes”)
- Confirm destructive actions with clear warnings
- Use toasts for non-blocking feedback
- Use modals sparingly (they interrupt flow)

---

## 6) Motion and polish

- Motion must communicate state change, not decoration
- Respect reduced-motion
- Keep durations consistent and subtle

---

## 7) Accessibility UX overlap

- Focus rings visible
- Color contrast compliant
- Keyboard navigation is not optional
- Error messages tied to fields (programmatically)

(See `accessibility_playbook.md`.)
