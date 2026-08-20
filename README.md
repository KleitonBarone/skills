# Skills

Personal repository for global agent skills and instructions.

## Layout

- `skills/` contains global agent skills. Each skill lives in its own directory and includes a required `SKILL.md` file.
- `AGENTS.md` is the versioned source for global instructions.

## Local paths

This repository is cloned at `C:\Users\<user>\.agents`.

Agents discovers global skills from `C:\Users\<user>\.agents\skills`. The versioned `AGENTS.md` in this repository is the intended target for the local `C:\Users\admin\.codex\AGENTS.md` symbolic link (or another dot file if not using codex, or multiple if using multiple). 

## Updating skills

Add each real skill under `skills/<skill-name>/` with a required `SKILL.md`.
