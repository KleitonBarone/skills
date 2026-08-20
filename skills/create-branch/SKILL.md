---
name: create-branch
description: Create and switch to a new local Git branch named for work already in progress. Use when the user asks to create, start, or make a branch for the current changes or task.
---

# Create branch

Create one local branch for the current work. A branch request authorizes creating and switching to that branch. It does not authorize committing, pushing, rebasing, updating the base branch, or opening a PR.

## Read the request

- Treat "what should we call the branch?" and other questions as read-only.
- Use an explicit branch name or base when the user provides one, after validating it against repository rules. If the name conflicts with a clear convention, explain the conflict before changing it.
- Infer the work from the user's request, the current conversation, and the worktree diff.
- If the current branch already matches the task, do not stack another branch without confirming that the user wants a second branch.

## Inspect the repository

Before creating anything:

1. Find the repository root and current branch.
2. Run `git status --short` and keep the result for comparison after the switch.
3. Check for an active merge, rebase, cherry-pick, revert, or bisect. Stop if one is in progress.
4. Read `AGENTS.md`, contributor docs, templates, and other repository guidance for branch rules.
5. Inspect several recent local and remote branch names already available in the checkout.
6. Check whether the current branch has commits that the new branch would inherit.

Do not fetch, pull, rebase, stash, reset, or clean the worktree just to create a branch. The default base is the current `HEAD`, which preserves the work already underway.

If the current branch contains unrelated commits beyond the intended base, ask before creating a branch from it. A good name cannot fix the wrong history.

## Determine the convention

Use this priority order:

1. Explicit branch rules in repository guidance
2. A stable pattern shared by several recent human-created branches
3. User-provided ticket or naming requirements that do not conflict with repository rules
4. The fallback format below

Do not infer a convention from one branch. Ignore bot branches, dependency updates, release automation, generated branches, forks, and obvious one-offs. Look for repeated choices in prefix, separators, casing, ticket placement, username namespaces, and description length.

If written guidance and current branch history disagree, follow the written rule unless it is clearly stale. When the evidence is mixed and the difference would materially change the name, ask instead of inventing a hybrid convention.

## Name the branch

Match the established convention exactly. Preserve its prefix vocabulary, casing, separators, ticket format, and namespace order. Do not normalize a repository's branches to personal preferences.

Only when no stable convention exists, use:

```text
<type>/<short-kebab-summary>
```

Choose the type from the work, usually `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, or `perf`.

Name the resulting behavior or goal rather than the implementation detail.

Weak:

> `fix/update-draft-store`

Better:

> `fix/keep-drafts-when-switching-repos`

For the fallback, keep the name lowercase, short, and readable. Prefer ASCII letters, digits, hyphens, and one meaningful slash. Do not add dates, usernames, issue numbers, or numeric suffixes unless the repository uses them.

Validate the candidate with `git check-ref-format --branch <name>`. Check local and known remote refs for collisions. If an existing branch has the same name, inspect it before switching or choosing a different name. Never overwrite or reset it.

## Create and verify

Create the branch from the confirmed base with `git switch -c <name>`. Use `git checkout -b <name>` only when the installed Git version does not support `switch`.

If creation output is uncertain, inspect the current branch before retrying. Do not create a second branch because terminal output was interrupted.

After creation:

1. Confirm the current branch name.
2. Record the base commit with `git rev-parse --short HEAD`.
3. Run `git status --short` again.
4. Confirm the same staged, unstaged, and untracked work remains.

Do not set an upstream or push the branch unless the user separately asks.

## Report

Return:

- The branch name
- The previous branch and base commit
- Whether uncommitted work remains
- That the branch is local and has not been pushed
