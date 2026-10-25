---
name: plan-project
description: Create or update a start-to-finish software delivery plan from repository and handoff context, including milestones, proposed commits and PRs, reliable testing, cleanup, and completion gates. Use for planning implementation or recovering an unfinished delivery plan.
---

# Plan a project through delivery

Create a plan another engineer can execute and resume without rediscovering the project's decisions. Match its depth to the work. Choose useful delivery boundaries instead of imposing a fixed number of phases, commits, or PRs.

## Establish the requested outcome

Determine what this turn should deliver from the request and prior conversation: an answer, a saved plan, a documentation delivery, or implementation. Creating a plan does not authorize executing its implementation steps. Delivering and merging a documentation PR does not authorize building the application.

Carry forward authorization already given for commits, pushes, merges, or deployment within its original scope. Do not ask for the same permission again. Ask only about unresolved decisions that materially change the outcome, cost, architecture, or allowed actions. Continue independent planning while those answers are pending; label reversible assumptions.

## Recover the actual starting point

Read the existing plan, handoff, README, repository guidance, relevant code and manifests, and the conversation's accepted decisions. Inspect Git status and history. Check linked PRs and CI when needed to establish what has actually shipped.

Distinguish implemented, verified, merged, and merely proposed work. For a resumed task, identify the last verified step and remaining gates before adding more work. Preserve completed milestones and user changes. Avoid duplicate plans, PRs, or repeated verification without a reason.

State the current capabilities, important gaps, constraints, and dependencies. For a repository containing only documents, say so. Mark proposed commands and unverified prerequisites as planned, rather than implying they already work.

## Define completion and the contracts that matter

Describe the intended users, problem, primary journey, observable result, and explicit exclusions. Give completion a verifiable meaning. Separate local operation, merged code, release, and public deployment when applicable.

Use the existing architecture and user preferences. Explain consequential choices and unresolved risks before scheduling work around them. Define the business or technical rules that prevent expensive rework, such as ownership, state transitions, retries, consistency, and retained-data compatibility. Select only rules relevant to this project.

List owner decisions still needed, such as licensing or paid-service access. Keep optional integrations and speculative infrastructure outside the required path unless they are part of the user's objective.

## Sequence reviewable deliveries

Prefer milestones that produce usable behavior, with foundational setup early enough to test the first feature. Reuse foundations that already exist. Order dependencies so a later delivery starts from a usable base; introduce stacks or parallel work only when justified.

For each substantial delivery, record:

- The behavior or capability it delivers and its bounded scope.
- Dependencies, affected components, and relevant contracts.
- Proposed commit subjects and, for PR workflows, the title, branch, and target following repository conventions.
- Acceptance gates, concrete verification, and a short demonstration path.
- Data migration, rollback, or cleanup work where the change needs it.

Keep commits cohesive and PRs reviewable. Leave room for fixes supported by actual failures or review findings. Planning labels such as D1 or PR A are proposed sequence labels, not real host-assigned PR numbers. Never invent commits, URLs, results, or merge timestamps.

A planning-document delivery can be its own first milestone when the user requested it. Use documentation checks for that delivery; application checks belong to the milestones that introduce runnable code.

## Make reliable testing part of the foundation

Specify a clean-checkout setup path, required runtimes and services, configuration and secret handling, migration and seed behavior, startup, readiness, and useful diagnostics. Verify version and platform assumptions before presenting them as facts. For mixed Windows/WSL setups, choose where application tools run and verify the actual service transport.

Separate retained development data from disposable test fixtures. Use unique run identities, isolated backing services, assigned ports where appropriate, and readiness checks that identify the intended service. State any required external accounts or test environments explicitly.

Plan focused checks around important boundaries and failure modes. Exercise the primary journey through the real components it uses, including persistence and service interfaces where relevant. For stateful systems, include meaningful restart, interrupted-operation, and upgrade scenarios alongside fresh-state tests. Simulated integrations prove the simulator contract, not a real provider's behavior.

Keep local and CI verification aligned. Use reproducible fixtures and controlled clocks when dates affect behavior. Include a practical way to inspect the isolated application while diagnosing failures. Avoid placeholder tests, repeated smoke suites, and retries that conceal unexplained failures.

## Plan cleanup before creating resources

For the environment the project actually needs, define ownership, startup, shutdown, reset, and interrupted-run recovery. For multi-service runs, record enough resource and process identity to recover partial startup safely. Register cleanup before launching resources and cover success, failure, timeout, and cancellation.

Separate stopping services from deleting retained data. Preserve existing services, developer progress, source, promoted evidence, and reusable caches. Identify exactly which disposable processes, browser profiles, containers, networks, volumes, checkouts, and downloads each run will remove. Verify removal and report intentional retention. Avoid global pruning and machine-wide cleanup.

Bound logs and diagnostics instead of accumulating artifacts per run. Prefer an indexed screenshot walkthrough for useful visual handoff evidence unless the user requests another format. Account for caches and image/build storage when they materially affect disk use.

Scale this work to the project. A small static site does not need a general environment-management system.

## Close the Git delivery loop

For a PR workflow, plan the complete sequence: synchronize with the latest target, make the scoped commits, push, open a draft PR, run checks on its latest head, handle review findings, mark it ready, and merge when authorized and its gates pass. Respect repository review rules and available host monitoring. Honor a user-selected direct-main workflow instead of forcing PRs.

When actual merging is in scope, opening a PR or enabling auto-merge is insufficient. Verify the host reports it merged and the target contains the resulting merge or squash commit. Plan appropriate verification of the resulting target SHA. Deployment is a separate step with its own scope and authorization.

## Leave a usable plan and handoff

Use the repository's existing planning document, or a conventional PLAN.md if none exists and a file was requested. Keep the current status, decisions, next step, and unresolved gates easy to find. Separate proposed work from an execution ledger containing actual commits, PR URLs, check results, and merges.

Review the plan for missing dependencies, test prerequisites, unsafe resource reuse, retained-data upgrades, merge verification, and handoff gaps. Include a clean-checkout rehearsal when independent setup is part of completion.

Route human setup and current operation to the README or handoff when those documents are in scope. Preserve historical evidence with the source it actually verified. Update status as work proceeds without turning the plan into a transcript or duplicating operating instructions across files.

Report the plan's location, delivery sequence, material assumptions, and any genuinely unresolved decisions. State what is ready to execute and what remains outside the current authorization.
