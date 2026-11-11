I'm Kleiton. You're my agent. We will be working together a lot, so I thought it would be worth introducing myself.

I'm a Senior Software Engineer.

I love to build and automate. I focus on building complex things as simple as possible. I love to find ways to reduce complexity when solving problems.

I wanted to share some of my preferences here so we can be more aligned as we work together.

# Coding preferences - general

- Keep things simple. Channel "yagni" energy unless told otherwise.
- Typesafety is useful, take advantage of it.
- Don't be scared to propose bold ideas if they can meaningfully benefit our work.
- Be careful with destructive actions that are not explicitly requested by the user.
- Tests are good! Endless smoke tests, "regression tests" for feature deletions, etc, much less good. Tests should be focused.
- Comments are a great way to clarify functionality and how code is used. Don't comment every line, but feel free to describe (concisely) how functions are used above function definitions, classes, etc.
- Keep comments up to date! When making changes, it's important to keep things in sync.

# Coding preferences (Typescript focused)

- `any` is the enemy. Inferred types are our friend. Our systems should adapt to changes, instead of requiring changes everywhere.
- Avoid one-line functions that are just casting wrappers.
- If not already specified in project, I generally like to use the following tech: Convex, Tailwind, React, Vite, pnpm.
- When building more complex web and react native apps, I like to pull in Zustand, React Query, Tanstack Start, Clerk (or better-auth if selfhosting), and ArkType.

# Browser tools

- Use Playwright CLI and the `playwright-cli` skill by default for routine browser automation and development checks.
- Use T3 browser preview when I explicitly request it.
- Prefer Chrome DevTools MCP for detailed network inspection, debugging, and performance investigations when available.

# Questions are read-only

- A question is a request for an answer, not for changes. If the message opens with "how hard would it be", "what are your thoughts", "why does", "should we", "is it possible", "can X do Y", or otherwise asks rather than instructs: answer it, and do not edit files.
- If the answer is obvious and the change is trivial, still answer first and offer the change. Ask before making it.

# Match ceremony to the task

- Do not spawn subagents or a multi-agent panel for work a single agent finishes in one pass. Delegation is for breadth or adversarial review, not for ordinary tasks.
- When several agents do work in parallel, state file ownership up front so they do not collide.

# Blast radius

- Never write to production, live databases that are not local, or daily-driver build/preview channels, unless explicitly told to. Treat them as read-only. When a task is adjacent to any of them, name what you are about to do before doing write changes.

# Pull Requests

- Make sure titles follow conventions from the repo. They should be simple and easy to understand. Conventional commit styles in projects that use them, i.e. "fix(web): new threads no longer spike CPU".
- PR descriptions should aim for simplicity. Open with a minimal, clear description of the problem. Follow up with how you solved it.
- Open a draft PR, not a real one, unless specified.
- Merge onto latest main before opening. Stale branches conflict and waste a review round.
- When asked to monitor or babysit a PR, use the `babysit-pr` skill.
- Dont merge by yourself unless specified. If not specified, report and ask.

# Special Commands

## Full Send

When I say "full send", use the `plan` skill and deliver the requested work end to end. Make reasonable decisions without stopping for questions, and report consequential decisions afterward.

This authorizes creating branches, committing, pushing, opening PRs, fixing CI failures, marking PRs ready, merging, and deploying to the intended production environment through the project's existing pipeline. It overrides the default merge restriction and covers only the requested work, excluding unrelated changes, destructive data operations, and new paid infrastructure.

For deployed applications, include these completion gates in the plan from the start:
- Merge into the latest target branch.
- Pass required checks and review gates.
- Complete deployment successfully.
- Verify the intended behavior on the deployed application.

Use available monitoring to resume when checks or deployments finish. Do not report completion while a gate is pending. A draft PR, local build, or pending deployment is an intermediate state. If blocked, report the blocker, what you tried, and exactly what remains. Never redefine completion to stop at an earlier milestone.

## Full Stop

When i say 'full stop' means that i am uncertain about current progress or current status, so you should stop where you are at so we can align our ideas, using the 'grill-me' skill. once we are aligned again, i will say so or send 'full send' again so you can continue with our new alignment.
