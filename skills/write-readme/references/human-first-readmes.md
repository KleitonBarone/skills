# Human-first README patterns

These notes come from public repositories associated with Theo Browne. Use them to understand the editorial choices. Do not copy product claims, jokes, profanity, branding, or personal voice into another project.

## Source set

Research checked on 2026-08-20:

- [T3 Code README](https://github.com/pingdotgg/t3code/blob/main/README.md)
- [Lawn README](https://github.com/pingdotgg/lawn/blob/main/README.md)
- [create-t3-app README](https://github.com/t3-oss/create-t3-app/blob/main/README.md)
- [UploadThing README](https://github.com/pingdotgg/uploadthing/blob/main/README.md)
- [Stripe recommendations README](https://github.com/t3dotgg/stripe-recommendations/blob/main/README.md)
- [QuickPic README](https://github.com/t3dotgg/quickpic/blob/main/README.md)

Theo has edited the README in each of these repositories. Several are maintained by teams, so treat their current text as collaborative rather than exclusively his.

## What stays consistent

The README speaks to a person with a practical question. It does not begin with repository internals.

The opening usually establishes a concrete identity quickly. T3 Code says what kind of product it is and which tools it controls. Lawn says it is a video review platform. QuickPic needs only a few sentences because the project is small.

Motivation appears early. The reader learns what frustrated the maintainer, which alternative fell short, or which workflow the project simplifies. This makes the project easier to understand than a feature inventory would.

The prose anticipates skepticism. Conversational headings answer questions such as what the product really is, whether it is a template, or why it exists. The headings work because they name a question the reader already has.

The documents are candid. They state when a project is early, when contributions are restricted, what remains the reader's problem, and where the recommended approach stops working. That honesty is part of the technical content.

The next action is concrete. Product and CLI repositories give an install command or link. Guide repositories give prerequisites and an ordered flow. Repositories with full documentation point readers there instead of duplicating it.

## How the examples differ

### T3 Code

The README routes several human audiences in order. It defines the product, addresses the obvious commercial question, gives the easiest trial command, lists installation choices, states project maturity, then routes users and contributors to separate documentation.

The main lesson is prioritization. A curious user sees product and installation information before contributor tooling or architecture.

### Lawn

The README is short and personal. It gives a one-line product description, puts the unusual contribution policy near the top, explains the motivation, admits uncertainty, and links to three focused docs.

The main lesson is that a small README can be complete when it is honest and well-routed.

### create-t3-app

This README has a polished project identity, a one-command start, a definition of the stack, an answer to the obvious template question, and a set of axioms. Each axiom uses concrete examples to show which choices fit the project and which do not.

The main lesson is to explain opinionated decisions through examples. Values such as modularity and type safety matter because the README shows how they affect inclusion and exclusion.

### UploadThing

The README leaves product usage to the documentation site. It identifies the project, links to the main destinations, maps packages and examples, and provides contributor steps.

The main lesson is to respect an existing docs system. The repository README should route readers, not compete with the canonical docs.

### Stripe recommendations

This repository is itself a long technical guide. The README states the maintainer's experience and frustration, defines what it will not cover, lists prerequisites, explains the core failure mode, gives the full flow before details, then supports the recommendation with code and caveats.

The main lesson is to establish scope and thesis before code. Readers can decide whether the approach fits before committing to the full implementation.

### QuickPic

The README is one paragraph. It says what the utility does, why it was built, and why it is free and open source.

The main lesson is restraint. A tiny project does not earn enterprise README sections.

## Human and agent boundaries

A good README remains valuable to agents because it contains accurate product intent, setup commands, supported paths, and documentation links. It should still address humans.

Move these details elsewhere:

- Agent authority and approval rules
- Destructive commands and live-data restrictions
- Instructions for staging, committing, or opening PRs
- Detailed coding preferences
- Internal completeness checklists
- Agent-specific verification behavior

Put that material in `AGENTS.md` or contributor documentation. Do not make a new developer read an agent contract before learning what the project does.

## Editorial test

Ask these questions while revising:

- What does the reader understand after ten seconds?
- Can they tell whether the project is meant for them?
- Is the fastest valid next action visible?
- Does the README explain the project's real opinion or merely list technology?
- Are limitations as easy to find as benefits?
- Can a detailed section become one sentence and a link?

Keep the answer concrete. The strongest pattern across these repositories is not a layout. It is respect for the reader's time.
