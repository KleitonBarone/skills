---
name: write-agents-md
description: Write or revise a repository's AGENTS.md as a concise, project-specific operating guide. Use when the user asks to create, audit, rewrite, or improve AGENTS.md, agent instructions, repository guidance, or coding-agent rules.
---

# Write AGENTS.md

Create a compact operating guide for agents working in a specific repository. Derive it from the repository instead of pasting a generic ruleset or copying another project's file.

## Choose the mode

- Treat a request to review, explain, or suggest as read-only. Report findings and offer changes.
- Treat a request to create, rewrite, or improve as permission to edit the requested `AGENTS.md` scope.
- Preserve unrelated work and existing instructions. Resolve whether root and nested guidance files have different scopes before editing.

## Inspect before writing

Build a small evidence set from the repository:

1. Read existing `AGENTS.md`, `CLAUDE.md`, editor rules, contributor docs, and nested instruction files.
2. Read the README, package manifests, workspace configuration, CI workflows, and scripts that define real commands.
3. Map the product's main clients, package boundaries, shared contracts, generated code, live data, and deployment paths.
4. Identify recurring or expensive mistakes from tests, issues, docs, comments, and the code itself.
5. Check the worktree before editing. Do not overwrite user changes or normalize unrelated prose.

Verify every path and command against the current repository. Never invent a command because a similar project probably has it.

## Find the useful rules

Keep instructions that change an agent's decision. Prefer evidence in this order:

1. Safety and blast-radius constraints
2. Product behavior that must not regress
3. Architectural boundaries and cross-client completeness
4. The smallest valid build, test, typecheck, lint, and formatting workflow
5. Repository-specific taste that resolves real implementation tradeoffs
6. PR or release rules that the repository enforces

Turn vague values into observable behavior. Replace "care about performance" with the known hot paths, prohibited patterns, or measurement that proves the change is safe.

Drop advice a capable coding agent already knows. "Write clean code", "follow best practices", and broad security reminders consume attention without changing behavior.

## Draft from the project outward

Use only the sections the repository earns. A useful order is:

1. Project name and a two-sentence orientation
2. Product principles or non-negotiables
3. A short maintainer philosophy note
4. Terms that are genuinely ambiguous
5. Concrete ways an agent can damage the project
6. A completeness checklist across clients, entry points, providers, contracts, or modes
7. Local development and test data
8. Focused verification
9. PR and release boundaries
10. Architecture map and coding taste

Do not force this outline. A small app may need only product priorities, commands, and two sharp warnings. A mature multi-client system may justify more.

Write in direct, plain language. Use memorable headings when they name a real problem. Explain the consequence behind a hard prohibition. Use "we" for maintainer intent and address the agent as "you" only when that makes an instruction clearer.

## Apply the decision rules

- Favor the smallest model that makes correct behavior unsurprising.
- Understand the constraint before adding machinery.
- Treat rules as good defaults unless safety, data integrity, or an enforced workflow makes them non-negotiable.
- Make performance, good defaults, and user convenience concrete for this product.
- Put complexity at a boundary when that keeps the core easy to reason about.
- Prefer focused proof over ceremonial full-suite testing.
- Fight scope creep. Do not turn `AGENTS.md` into a second README or architecture handbook.

Keep product-specific claims product-specific. Do not transplant framework preferences, package-manager commands, product vocabulary, or personal coding taste into a repository that does not support them.

## Audit the result

Before finishing, check:

- Every command, path, package name, and product client exists.
- Each absolute rule has a concrete failure or enforced convention behind it.
- The file distinguishes user requests from actions the agent may take autonomously.
- Verification matches the change's scope and cost.
- The document has no contradictions with nested guidance or contributor docs.
- Generic advice, duplicated README material, stale history, and speculative architecture are gone.
- The file is the shortest version that would still prevent the repository's expensive mistakes.

After an edit, show the file changed and summarize the few decisions encoded.
