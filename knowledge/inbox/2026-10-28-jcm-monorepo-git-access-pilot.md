# Proposal: Record the jcm-monorepo Git access pilot

- Status: unreviewed proposal
- Source: HACLS cross-project pilot run from `/Users/thanapat/Dev/jcm-monorepo` on 2026-10-28
- Related canonical source: `knowledge/canonical/pilot-test-git-access-check.md` — “Test rule”

## Context

The pilot checked GitHub access from a consumer project using its configured `origin` remote. The workspace had existing local edits, and its `.git` directory was read-only under the active session policy.

## Evidence

- `gh auth status` reported an authenticated GitHub account.
- `git ls-remote --heads origin` returned the `dev` and `main` refs.
- Local Git metadata writes were not attempted because `.git` was read-only.
- No push or pull request was attempted from the consumer project.

## Proposed lesson

Record authentication, remote reads, local Git metadata writes, and contribution actions as separate results. Successful authentication and remote reads do not establish local write or PR capability. When local metadata writes are prohibited by the session policy, report that check as not run rather than treating it as a failed GitHub permission check.

## Scope and uncertainty

This observation applies to one Codex session and the `jcm-monorepo` checkout on 2026-10-28. The metadata-write check was not run, so it does not establish whether a different writable checkout or session could create a branch, push, or open a PR. Owner review is needed before accepting or merging this proposal.
