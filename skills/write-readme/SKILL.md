---
name: write-readme
description: Write or revise a project's README.md for human readers. Use when the user asks to create, rewrite, audit, or improve a README, repository landing page, setup guide, project overview, or contributor-facing introduction.
---

# Write README

Write the repository's front door for a human reader. Agents may use the README as context, but agent-only operating rules belong in `AGENTS.md`.

Read [references/human-first-readmes.md](references/human-first-readmes.md) before drafting or revising a README.

## Choose the mode

- Treat a request to review, explain, or suggest as read-only.
- Treat a request to create, rewrite, or improve as permission to edit the requested README.
- Preserve accurate branding, links, screenshots, acknowledgements, and contributor information.
- Keep unrelated user edits intact.

## Inspect the project

Read enough of the repository to write facts instead of guesses:

1. Read the existing README and nearby documentation.
2. Read package manifests, workspace files, CLI help, example apps, and entry points.
3. Check the project website, package metadata, release links, screenshots, license, and contribution guide when they exist.
4. Read `AGENTS.md` and contributor guidance so the README does not absorb internal operating rules.
5. Verify every command, version requirement, path, and link before publishing it.

Identify the primary reader and the decision they came to make. They may be evaluating the project, trying it for the first time, integrating a package, learning an approach, or considering a contribution. Pick one primary path. Do not make every audience equally prominent.

## Open with the point

Make the first screen answer:

- What is this?
- Who is it for?
- Why would they use it instead of the obvious alternative?
- What should they do next?

Start with a concrete sentence, not a slogan assembled from adjectives. Put the shortest working install command, example, demo link, or next step close to the top.

Use a logo, screenshot, badges, or centered HTML only when those assets help a human identify or trust the project. Do not add decorative badge walls.

## Write for the project type

Scale the document to the project.

- For a small utility, a short explanation, motivation, link, and usage command may be enough.
- For an app, explain the product, why it exists, how to try or install it, current limitations, and where support lives.
- For a library or CLI, lead with the problem solved, installation, a minimal real example, compatibility, and documentation links.
- For a guide or reference repository, state the thesis, prerequisites, scope exclusions, recommended flow, and unresolved responsibilities.
- For an SDK or monorepo, route users to the docs and map packages or examples only when that map helps them choose the right entry point.

Do not force a universal template. Add a table of contents only when the README is long enough to need navigation.

## Explain the decisions

Use plain, opinionated language when the project has an opinion. Explain the constraint that led to the decision and give a concrete inclusion or exclusion example.

Conversational headings can answer the question a skeptical reader is already asking. First-person or maintainer voice is useful when explaining motivation, tradeoffs, uncertainty, or contribution policy. Match the project's real voice. Do not impersonate another maintainer or copy their quirks.

Be candid about:

- Project maturity and known limitations
- What the project deliberately does not solve
- Maintenance expectations
- Whether contributions are welcome and in what form
- External services, accounts, or prerequisites required for the happy path

Honest boundaries build more trust than polished claims.

## Keep the README in its lane

- Link to full documentation instead of reproducing it.
- Link to `CONTRIBUTING.md` for detailed contributor setup and process.
- Keep agent behavior, destructive-action rules, and repository-specific coding instructions in `AGENTS.md`.
- Keep release history in the changelog.
- Avoid exhaustive architecture and directory tours unless they help the primary reader complete a task.

The README should remain useful to agents because its facts are accurate, not because it talks to agents.

## Audit the result

Before finishing, check:

- The opening explains the project without relying on badges or branding.
- The primary reader has an obvious next action.
- Commands and examples work against the current repository.
- Claims are concrete and supportable. Remove invented scale, speed, popularity, and compatibility claims.
- Links point to the canonical current destination.
- The README names important limits and prerequisites.
- Internal agent instructions and duplicated docs are gone.
- The voice sounds like the maintainers, not a corporate landing page or an AI summary.
- The document is the shortest version that gets the reader from curiosity to success.

After editing, summarize the reader path you optimized and any facts that still need maintainer confirmation.
