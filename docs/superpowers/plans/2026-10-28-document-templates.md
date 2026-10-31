# Document Templates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Thai-first template catalog for document types that already exist in HACLS, with a central index of type codes and practical usage guidance.

**Architecture:** Keep copyable Markdown templates under `templates/`, grouped by existing repository area (`docs`, `research`, and `knowledge`). `templates/index.md` maps each type code to its template and destination; `templates/README.md` explains how to select, copy, and adapt a template.

**Tech Stack:** Markdown and Git only; no scripts or dependencies.

**Spec:** [2026-10-28-document-templates-design.md](../specs/2026-10-28-document-templates-design.md)

## Global Constraints

- Follow the repository's existing plain Markdown and Thai-first conventions.
- Keep templates as copyable Markdown files; do not require front matter or tooling that the repository does not currently use.
- Include guidance to record sources and distinguish unreviewed knowledge from validated or canonical knowledge.
- Reuse existing status vocabulary from the project charter.
- Type codes identify document types, not individual documents.
- Cover only the project documents, research reports, and Event Storming knowledge files present in the repository today.

## Review Focus

- Each catalog code is unique and maps to exactly one template path.
- Every path in the catalog exists, and each template has a matching catalog entry.
- Usage instructions distinguish copying a template from moving knowledge through review states.
- Knowledge templates prompt for sources and make inbox status visible.
- Templates contain prompts rather than fabricated project or Event Storming facts.

---

### Task 1: Add the template usage guide, catalog, and Markdown templates

**Files:**
- Create: `templates/README.md` — how to use the templates and extend the catalog.
- Create: `templates/index.md` — type-code registry, purpose, template path, and target location.
- Create: `templates/docs/project-document.md` — general project document template.
- Create: `templates/research/report.md` — research question, method, findings, limitations, and sources template.
- Create: `templates/knowledge/topic-index.md` — topic navigation and status template.
- Create: `templates/knowledge/overview.md` — synthesized overview template.
- Create: `templates/knowledge/note.md` — single-idea note template with links and supporting sources.
- Create: `templates/knowledge/references.md` — source list with bibliographic and verification prompts.

- [x] **Step 1: Create the catalog and usage guide**

Document the following codes in `templates/index.md` and link each to its template and intended destination:

| Code | Type | Template | Destination |
|---|---|---|---|
| `DOC` | Project document | `docs/project-document.md` | `docs/` |
| `RES` | Research report | `research/report.md` | `research/` |
| `KIDX` | Knowledge topic index | `knowledge/topic-index.md` | `knowledge/{inbox,validated,canonical}/<topic>/index.md` |
| `KOV` | Knowledge overview | `knowledge/overview.md` | `knowledge/{inbox,validated,canonical}/<topic>/overview.md` |
| `KNOTE` | Individual knowledge note | `knowledge/note.md` | `knowledge/{inbox,validated,canonical}/<topic>/notes/<slug>.md` |
| `KREF` | Knowledge references list | `knowledge/references.md` | `knowledge/{inbox,validated,canonical}/<topic>/references.md` |

Explain in `templates/README.md` how to choose a code, copy the matching file, replace prompts, retain the type code as a catalog reference, and update the index when adding a new template. Clarify that using a template does not approve or promote knowledge.

- [x] **Step 2: Create project and research templates**

Use concise Thai prompts. The project document template should cover purpose, scope, decisions, and related documents. The research report should cover question, sources/method, findings, limitations, and references, with prompts to separate source evidence from interpretation.

- [x] **Step 3: Create knowledge templates**

The topic index should link overview, references, and notes and show the knowledge state. The overview should synthesize the current understanding, scope, linked notes, and open questions. The individual note should express one main idea and include supporting sources and related-note links. The references list should capture title, author/publisher, URL, publication/access dates when known, relevance, and verification state.

- [x] **Step 4: Manually review the catalog and templates**

Check that all six codes are unique, every index link resolves to a created file, every template appears in the index, the paths agree with the design, and the templates contain no invented facts. No automated tests are needed for this Markdown-only change.

- [x] **Step 5: Review the final diff**

Run `git diff --check` and inspect the new Markdown files and `git status --short`. Confirm unrelated pre-existing changes are untouched.
