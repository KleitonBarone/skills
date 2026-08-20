---
name: commit
description: Create a focused local Git commit from the changes that belong to the user's request. Use when the user asks to commit, make a commit, save changes in Git, or prepare a commit.
---

# Commit

Create one clean local commit for the work the user asked to save. A commit request authorizes staging and committing that work. It does not authorize pushing, opening a PR, amending history, rebasing, or changing branches.

## Read the request

- Treat "should we commit?" and other questions as read-only.
- Follow any file scope or commit message the user provided.
- Keep one concern per commit. Do not split tightly coupled work into ceremonial commits.
- If unrelated changes are mixed into the worktree and cannot be isolated safely, ask which changes belong.

## Inspect before staging

1. Run `git status --short`.
2. Read both unstaged and staged diffs. Never assume existing staged changes belong to this task.
3. Read repository guidance and recent commit subjects to learn the local message convention.
4. Identify the exact paths that implement the requested change.
5. Check whether generated files, lockfiles, migrations, snapshots, or docs must move with those paths.
6. Note the verification already completed during the task.

Preserve unrelated user work. Do not clean the worktree, restore files, or rewrite changes to make staging easier.

## Stage deliberately

- Stage only confirmed paths with `git add -- <paths>`.
- Never use `git add .`, `git add -A`, or `git add --all`.
- Preserve pre-existing staged changes. If they do not belong in the same commit, stop and ask instead of unstaging them without permission.
- Use patch staging only when hunks can be separated without editing or discarding the user's work.
- After staging, inspect `git diff --cached --stat` and the full `git diff --cached`.
- Check for secrets, debug output, accidental binaries, and unrelated formatting churn.

The staged diff is the commit. Do not proceed until it matches the user's request.

## Write the message

Follow the repository's established format. Use Conventional Commits only when the repository uses them.

Prefer a short subject that names the resulting behavior or reason for the change. Avoid implementation inventories and vague subjects.

Bad:

> `fix: update draft state logic`

Better:

> `fix(web): keep typed prompts when switching repos`

For repository maintenance, plain subjects such as `chore: add commit skill` are often enough.

Use a body only when the reason, compatibility impact, migration, or non-obvious tradeoff will help the next reader. Explain why the change exists. Do not repeat the diff as a list of files.

Do not add model attribution, generated-by text, emojis, or issue references unless the repository requires them.

## Verify and commit

Run the smallest relevant check required by the repository and the staged change unless current evidence from the task already covers it. Do not start a full test suite as commit ceremony.

Create the commit once. Do not bypass hooks with `--no-verify`.

If a hook fails:

1. Read the failure instead of retrying blindly.
2. Inspect any files the hook modified.
3. Stage only intended hook changes.
4. Rerun the narrow failing check, then commit again.

If the command result is uncertain, inspect `git log -1` and `git status` before another attempt. Never create a duplicate commit because output was interrupted.

After success, inspect the final commit and worktree. Confirm the commit contains the intended files and report any changes left uncommitted.

## Report

Return:

- The short commit hash and subject
- The verification or hooks that ran
- Any remaining staged or unstaged changes

Do not push unless the user separately asks for it.
