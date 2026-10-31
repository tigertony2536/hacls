# Document templates and type index

## Intent

Create a small, discoverable set of Markdown templates for document types already present in HACLS. The templates should help the owner and agents create consistent documents without treating inbox material as approved guidance.

## Goals

- Provide one central index of document type codes, template paths, purpose, and when to use each template.
- Provide a short usage guide for copying and adapting templates.
- Cover current project documents, research reports, and the Event Storming knowledge files: topic index, overview, individual note, and references.
- Use Thai for explanatory text, consistent with the repository's current convention.

## Non-goals

- Assign a unique identifier to every document; the codes identify document types only.
- Add templates for capabilities, skills, experiments, or decisions until examples of those document types exist in the repository.
- Migrate existing documents to templates or add automation to validate template use.

## Approaches

1. **One template per document type (chosen):** a central index maps short type codes directly to templates. This matches the request for per-file templates and makes lookup direct.
2. **Templates grouped into workflow bundles:** users first choose a project, research, or knowledge bundle and then choose a file within it. This adds an extra navigation step for a small catalog.

## Structure and type codes

Create `templates/README.md` for usage instructions and `templates/index.md` as the catalog. Store templates under `templates/docs/`, `templates/research/`, and `templates/knowledge/`.

Initial type codes:

| Code | Document type |
|---|---|
| `DOC` | General project document for `docs/` |
| `RES` | Research report for `research/` |
| `KIDX` | Knowledge topic index |
| `KOV` | Knowledge topic overview |
| `KNOTE` | Individual knowledge note |
| `KREF` | Knowledge references list |

The index will map each code to its template path, purpose, and target location. These codes are catalog references, not per-document IDs.

## Constraints and calls

- Follow the repository's existing plain Markdown and Thai-first conventions.
- Keep templates as copyable Markdown files; do not require front matter or tooling that the repository does not currently use.
- Include guidance to record sources and distinguish unreviewed knowledge from validated or canonical knowledge.
- Reuse existing status vocabulary from the project charter.

## Left to the builder

Choose concise section prompts for each template, based on the existing documents and Event Storming scaffold. Keep optional sections visibly optional and avoid inventing factual content.
