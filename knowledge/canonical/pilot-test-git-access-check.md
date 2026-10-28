# Pilot fixture: check Git access in separate layers

> **Test fixture only.** This synthetic entry exists to test cross-project retrieval and application. Do not treat it as accepted HACLS guidance or merge it into the canonical collection after the pilot without owner review.

- Status: pilot-test-fixture
- Scope: Codex local workspace sessions using GitHub over HTTPS
- Evidence: In the 2026-10-28 HACLS pilot setup, `gh auth status` succeeded and `git ls-remote --heads origin` returned a branch, while ordinary workspace-write commands could not write `.git`. A separately approved Git operation created a branch in the managed worktree.
- Uncertainty: Permissions can differ by session, managed policy, and worktree. Recheck in the target project; do not infer write access from successful authentication or remote reads.
- Retrieval marker: `SEPARATE-THE-CHECKS`

## Test rule

When diagnosing whether an agent can contribute to a GitHub repository, report these checks separately:

1. **Authentication:** Does `gh auth status` show a valid GitHub login? Never include credentials in the report.
2. **Remote read and network:** Does `git ls-remote --heads origin` return refs?
3. **Local Git metadata write:** Can the agent perform a controlled Git metadata change, such as creating a branch in the intended checkout, under the active permission policy?
4. **Contribution path:** Can the agent commit and push, and, if requested, open a reviewable PR?

Passing an earlier check does not establish that a later one will pass. Record the exact failing check and a redacted error instead of reporting only “GitHub works” or “GitHub is blocked.”

## Pilot application prompt

Ask the consumer-project agent to diagnose GitHub contribution readiness. A successful retrieval must cite this file and mention `SEPARATE-THE-CHECKS`. A successful application must report authentication, remote read, metadata write, and contribution path as distinct results.
