---
name: hacls-cross-project-pilot
description: Run a cross-project HACLS pilot. Use when an agent needs to check access to HACLS, find and apply canonical knowledge to a real task, or return a reviewable learning proposal.
---

# HACLS cross-project pilot

Use this skill to find out whether an agent in another project can retrieve HACLS knowledge, apply it to work, and report a useful learning back.

## Run the pilot

1. **Locate HACLS.** Use the path or remote the user provides. If neither is available, ask for one. Do not guess a URL, change credentials, or ask the user to paste a token. If access fails, record the exact command and error with secrets removed, then stop the access-dependent steps.
2. **Read the entry points.** Read HACLS `README.md` and `docs/00-project-charter.md`. Find relevant files under `knowledge/` and read only those needed for the task.
3. **Retrieve an authoritative source.** Search `knowledge/canonical/` first. Cite each source by repository-relative path and heading. Treat `knowledge/validated/` as reviewed but not canonical, and label it as such. Treat `knowledge/inbox/` as unreviewed proposals, not operating guidance. If no canonical source is relevant or the directory is empty, report retrieval as failed; do not fill the gap with a guess.
4. **Apply the source.** Continue the user's task in the current project using the retrieved guidance when it applies. State which decision or change it affected. If it does not apply, explain why and do not force it into the work.
5. **Capture a possible contribution.** Identify a reusable lesson only when the task produced evidence for it. Return a short draft suitable for `knowledge/inbox/` with its source, context, evidence, scope, and uncertainty. Keep it clearly marked as a proposal. Do not edit HACLS, push a branch, or open a PR unless the user asks for that contribution path.
6. **Report the result** using the template below. Mark each check `pass`, `fail`, or `not run`, and distinguish observed results from assumptions.

## Result template

```markdown
# HACLS cross-project pilot

- Consumer project:
- HACLS location and revision:
- Access: pass | fail
- Canonical retrieval: pass | fail
- Application: pass | fail | not run
- Contribution proposal: drafted | none found | not run
- PR path: pass | fail | not run

## Sources read
- `path/to/file.md` — heading; what it informed

## Work affected
- Task decision or change, with a brief explanation

## Contribution proposal
[Draft with source, context, evidence, scope, and uncertainty, or explain why none was produced.]

## Blockers and evidence
- Commands or observations that support each result. Remove credentials and other secrets.
```

## Pass criteria

- **Access passes** when the agent can read the intended HACLS revision.
- **Canonical retrieval passes** when the agent finds and cites a relevant file under `knowledge/canonical/`. An empty directory or no relevant entry is a failure, not a successful search.
- **Application passes** when the cited knowledge changes or confirms a concrete decision in the consumer task. If no task was supplied, mark it `not run`.
- **Contribution proposal passes** when a reusable lesson is backed by task evidence and clearly labeled for owner review. If no evidence supports a lesson, report `none found` instead of inventing one.
- **PR path** is `not run` unless the user asked to exercise it. When requested, report the branch and PR outcome separately from retrieval and application.

Keep credentials out of the report. Do not promote a proposal to `validated` or `canonical`; the HACLS owner decides its status.

## Example invocation

> Run the HACLS cross-project pilot for this task. HACLS is available at `/path/to/hacls`. Find relevant canonical guidance, apply it, and return the pilot report with any evidence-backed inbox proposal.
