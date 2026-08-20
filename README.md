# Skills

Personal repository for global agent skills and Codex instructions.

## Layout

- `skills/` contains global agent skills. Each skill lives in its own directory and includes a required `SKILL.md` file.
- `AGENTS.md` is the versioned source for global Codex instructions.
- `.gitignore` excludes common operating-system artifacts and temporary files.

## Local paths

This repository is cloned at `C:\Users\admin\.agents`.

Codex discovers global skills from `C:\Users\admin\.agents\skills`. The versioned `AGENTS.md` in this repository is the intended target for the local `C:\Users\admin\.codex\AGENTS.md` symbolic link.

## Updating skills

Add each real skill under `skills/<skill-name>/` with a required `SKILL.md`. Review all changes before committing them.
