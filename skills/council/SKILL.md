---
name: council
description: Trigger this if the user says 'council'. Run three GPT-6.1 Sol delegates.
---

# Council

Before an audit, address outstanding PR comments, fix known issues, and run
relevant checks. Give council the updated implementation; do not defer known
fixes until reviews return. If the user wants to discard the implementation
and explore new ideas, skip fixes to code being replaced.

Bring in three delegates to help with the user's request, usually for review
or feedback. All three must use GPT-6.1 Sol, model ID `gpt-6.1-sol`, at high
reasoning effort. Do not use other models or providers as substitutes.
Give each delegate a distinct angle, such as correctness, implementation and
testing, or risks and edge cases, while keeping their investigations independent.

Use the harness's native subagent tools when they support the required model
and reasoning effort. In T3 Code, if native tools cannot provide the requested
settings, use `orchestrator_capabilities` to resolve GPT-6.1 Sol on the Codex
provider, then `delegate_task` to start three delegates in parallel with high
reasoning effort in `target.options`. If GPT-6.1 Sol or the required settings
are unavailable, report it instead of substituting.

Give each delegate the request and relevant context. For review or feedback,
keep their work read-only. Collect their responses and summarize the useful
findings, disagreements, and recommended next steps.

Do not wait idle. When a result arrives, check its findings against the code
at once and decide what to fix while the other delegates run. Do not edit
files while a delegate still reviews the same checkout. If the user's
instructions mark a delegate as non-blocking, do not wait for it; treat a
late result as feedback and do not record its score.

For a code review, ask each delegate for a score out of 10.
Count each full review pass as one round.
A fresh review after fixes starts a new round.

Put this section after council is done:

```markdown
## Council review

Rounds: 2

| Delegate | Round 1 | Round 2 |
| --- | --- | --- |
| GPT-6.1 Sol 1 | 7/10 | 9/10 |
| GPT-6.1 Sol 2 | 8/10 | 10/10 |
| GPT-6.1 Sol 3 | 7/10 | 9/10 |
```

Put the results in the final reply only.

If you agree with their recommendations, make the changes and request a fresh
review after. Continue this process until all delegates are satisfied with the
outcome.

Do not let repeated reviews result in scope creep. It is your job to fight to
keep scope limited.
