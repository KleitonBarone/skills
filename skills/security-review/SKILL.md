---
name: security-review
description: "Use when asked to review the security of a design or code, or when a planned security review gate is reached."
---

# Review security boundaries

Find realistic abuse paths in the specified design or implementation. Choose review depth by risk to affected assets and boundaries rather than diff size.

## Establish scope and mode

Identify the target, applicable repository guidance, and security requirements. For changed code, resolve the comparison base and head revision. Include staged, unstaged, and relevant untracked changes only when the worktree is part of the requested scope. Review enough surrounding code and configuration to understand the affected controls. Expand to a repository-wide audit only when that scope is requested.

For diff reviews, report vulnerabilities introduced or newly exposed by the change. Investigate surrounding code as needed; clearly separate incidental pre-existing issues from findings about the change.

Choose the mode from the request and available artifacts:

- Design review examines proposed actors, data flows, trust assumptions, and required controls before implementation.
- Implementation review traces actual code and configuration to determine whether a realistic abuse path exists.

Label design risks as design risks. Separate missing design decisions and unknown deployment settings from verified implementation flaws. State whether the review is independent or performed by the implementer; loading this skill alone does not establish independence.

## Trace relevant abuse paths

Identify who can act, what they control, which assets matter, and where trust or privilege changes. Include authenticated users acting outside their permitted resources or tenant, where relevant.

Ground attacker capabilities and severity in the actual deployment and exposure. Use an existing threat model when available; state material assumptions when the context is unknown.

Follow attacker-controlled input to sensitive operations or exposed data. Inspect the server-side checks, ownership decisions, validation, transformations, and execution context along that path. Verify whether existing controls prevent the suspected abuse before reporting it.

When validation, authorization checks, or unusual workarounds change, inspect relevant Git history to understand their purpose and detect regressions.

Select checks that match the change. These may involve authentication and session handling, authorization and tenant isolation, injection, file or network access, sensitive-data handling, resource exhaustion, or privileged CI and deployment workflows. For agent features, include untrusted instructions reaching tools or private data. Avoid applying an unrelated checklist to every project.

When alleging a dependency vulnerability, verify the resolved version against a current authoritative advisory and check the relevant configuration and reachability. Treat scanner output as evidence to investigate, not a confirmed exploit.

## Validate within the authorized environment

Use source inspection and safe reproductions in local or explicitly authorized test environments. A review request does not authorize probing production, accessing real users' data, or executing destructive payloads. Keep secrets and private data out of findings and reproductions.

Report findings by default. Editing source or posting external comments requires authorization from the task. An authorized implementer can handle fixes separately. Distinguish executed checks from source analysis and state what remains unverified.

## Report actionable findings

Use the repository's severity scheme, or critical, high, medium, and low based on impact and realistic likelihood. For each finding, include:

- Severity and a short title.
- Location, using a file and line or a named section.
- Triggering scenario and impact.
- Supporting evidence and material assumptions.
- A focused fix direction when useful.

For a security finding, the scenario must explain the actor's required access, what they control, and how the affected boundary fails. Preserve uncertainty about unverified conditions. Keep design risks, confirmed flaws, and unresolved questions distinct, and consolidate duplicate root causes with other review findings.

Return no findings when none are supported. Finish with the reviewed scope and mode, reviewer independence, checks performed, and material gaps. Describe the result within that scope rather than certifying the application as secure. Recheck fixes and affected boundaries; broaden only when new changes or evidence justify it.

## Consult deeper guidance when needed

- For detailed code-path and control analysis, use the [OWASP Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html).
- For a design that needs deeper threat analysis, use [OWASP threat modeling guidance](https://devguide.owasp.org/en/04-design/01-threat-modeling/07-practical-threat-modeling/).
