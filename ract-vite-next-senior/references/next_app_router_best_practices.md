# Next.js App Router Best Practices (Senior)

This document assumes:

- Next.js **App Router**
- Server Components by default
- Client Components only where needed

---

## 1) Server-first mindset

### Rule

Default everything to **Server Components** and only opt into `"use client"` when required.

### Why

- Smaller client JS
- Better LCP potential
- Better caching opportunities
- Cleaner data access patterns

---

## 2) Server vs Client boundary

### Put on the server:

- data fetching
- reading cookies/headers (where appropriate)
- formatting + mapping raw API data into view models
- rendering static-ish content

### Put on the client:

- interactions (onClick, drag, text input state)
- browser APIs (localStorage, geolocation)
- client-only libraries (charts, maps, WYSIWYG editors)

### Architecture pattern

- Server component: fetch + map + layout
- Client leaf components: small interactive pieces
- Avoid turning whole pages into client components.

---

## 3) Data fetching and caching (conceptual)

- Understand the framework’s caching model.
- Keep data boundaries explicit:
  - what is cached
  - for how long
  - how invalidation happens

### Practical guidance

- Prefer route-level loading states (`loading.tsx`) for streaming UX.
- Avoid duplicating fetches across nested components—centralize where sensible.
- When you mutate data:
  - decide on optimistic vs pessimistic UX
  - ensure UI state matches cache invalidation strategy

---

## 4) Routing, layouts, and UX

- Keep layouts small and stable.
- Use nested routes for:
  - complex sections
  - shared navigation + shared data
- Provide good:
  - loading states
  - error states (`error.tsx`)
  - not-found states (`not-found.tsx`)

---

## 5) Images, fonts, and core web vitals

- Use Next image optimization where appropriate.
- Prefer system fonts or optimized font loading patterns.
- Avoid layout shifts (define sizes, stable containers).

---

## 6) Client state and server state

- Server state belongs in:
  - the server (rendered output)
  - or a client cache (React Query) if fully client-driven
- Avoid mixing “server truth” into global client stores unless you have a clear sync story.

---

## 7) Security

- Never expose secrets to the client.
- Validate inputs on server actions / API routes.
- Treat auth as a first-class feature: consistent redirects and error handling.

---

## 8) Code review checklist (Next App Router)

- Are we server-first by default?
- Is `"use client"` minimal and justified?
- Are loading/error/not-found states present?
- Is caching/invalidation intentional and documented?
- Are we shipping unnecessary client JS?

---

## Upgrade Notes (maintainers)

Update this section when Next releases introduce:

- caching model changes
- server/client boundary changes
- routing/layout conventions updates
