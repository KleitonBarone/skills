---
name: code-review
description: Review a diff, commit range, pull request, or specified code for actionable correctness issues and regressions. Use when asked for code review or when an authorized delivery reaches its planned code review gate. Report findings by default.
---

# Review code changes

Find defects that matter to the requested behavior. Choose review depth by risk, affected contracts, and realistic exposure. A small diff can warrant deep review.

## Establish scope and authority

Use the user's named PR, commit range, diff, or code scope. Otherwise inspect current worktree changes and task context. For PR and commit reviews, resolve the base and head revisions. For worktree reviews, include staged, unstaged, and relevant untracked changes against the chosen base. Record the exact reviewed scope. Ask only if the target remains materially ambiguous.

Read applicable repository guidance, the intended behavior, and relevant verification results. Preserve intentional differences between root and nested instructions.

Report findings by default. Editing source or posting review comments requires authorization from the task. An authorized implementer can handle fixes separately. State whether the review is independent or performed by the implementer; loading this skill alone does not establish independence.

## Follow the affected behavior

Read the full changed functions and enough callers, consumers, configuration, and tests to understand their contracts. Compare behavior before and after the change. Trace across affected clients and shared interfaces when a local change can break another entry point.

Prioritize incorrect results, missing requirements, compatibility breaks, data loss, and relevant failure or concurrency paths. Check migrations, retries, cancellation, and partial failures when the change involves them. Report security defects encountered during code review; a separate security review can examine those boundaries in greater depth.

Inspect changed hot paths for unbounded work, repeated database or network calls, and resource leaks. Tie findings to realistic workloads and concrete impact.

When validation, authorization checks, or unusual workarounds change, inspect relevant Git history to understand their purpose and detect regressions.

For a diff review, focus on defects introduced or newly exposed by the change. Keep unrelated existing issues outside the findings unless the user requested a broader review. Style preferences and speculative refactors need a concrete contract or enforced convention to justify a finding.

## Verify suspected findings

Identify a triggering input or state, trace the failure, and establish its impact. Check callers, guards, types, and tests for controls that invalidate the concern. Verify bot or earlier reviewer claims against the current source before repeating them.

Use focused existing checks or disposable local reproductions when they resolve uncertainty. Run only relevant checks within authorized local or test environments. Source evidence may be sufficient; distinguish inspected behavior from executed checks. Missing setup or unavailable checks belong in review limitations.

## Report actionable findings

Use the repository's severity scheme, or critical, high, medium, and low based on impact and realistic likelihood. For each finding, include:

- Severity and a short title.
- Location, using a file and line or a named section.
- Triggering scenario and impact.
- Supporting evidence and material assumptions.
- A focused fix direction when useful.

Order findings by severity and consolidate reports of the same root cause. Separate unresolved questions from supported defects. Return no findings when none are supported; do not invent issues to fill a quota.

Finish with the reviewed scope, reviewer independence, checks performed, and material gaps. If reviewing fixes, inspect the fixes and affected paths. Broaden the review only when new changes or evidence justify it.
