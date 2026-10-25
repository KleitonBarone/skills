---
name: docker-wsl
description: Run Docker and Compose on Kleiton's Windows machine through WSL Ubuntu, with cleanup of task-owned temporary resources. Use whenever a task on this machine needs Docker, including when the Windows docker command is missing.
---

# Docker through WSL

## Machine context

Docker Engine and Docker Compose run inside the WSL 2 distribution `Ubuntu`. A missing Windows `docker` executable does not mean Docker is unavailable. The verified local Docker endpoint is `unix:///var/run/docker.sock`.

From PowerShell, check the Linux installation before declaring Docker unavailable:

```powershell
wsl -d Ubuntu --exec docker version
wsl -d Ubuntu --exec docker compose version
wsl -d Ubuntu --exec docker context inspect default --format '{{.Endpoints.docker.Host}}'
```

Use `wsl --list --verbose` if the distro cannot be reached. If Docker fails, inspect the actual error. Do not install Docker Desktop, change Docker contexts, start a different daemon, or alter WSL configuration without task authorization.

Run repository commands in the corresponding Linux path. For example, `C:\Users\admin\repos\feature-rollout-service` maps to `/mnt/c/Users/admin/repos/feature-rollout-service`:

```powershell
wsl -d Ubuntu --cd /mnt/c/Users/admin/repos/feature-rollout-service --exec docker compose -f compose.release.yaml config --quiet
```

PowerShell environment variables are not automatically available to Linux commands. Pass only the task's required variables deliberately, and do not print secrets through command arguments or rendered Compose configuration. Use one shell for Linux pipelines and redirection. Save binary backups inside WSL or use binary-preserving tools.

## Temporary work must be cleaned up

Always clean up resources created for verification, builds, and experiments when the task ends, including after failures or interruption. Leave resources running only when the user requested a persistent result. This is not permission to remove pre-existing resources or application data.

Before creating anything:

- Identify the Docker endpoint and any existing containers, images, volumes, and builders relevant to the task. Treat existing resources as user-owned.
- Use a unique Compose project such as `codex-frs-<run-id>`. Pass the same explicit `-p` and Compose files to every operation. Avoid the repository's default project and fixed container names for temporary verification.
- Record exact task-owned project names, resource IDs, image tags, builders, and temporary paths. Choose ephemeral host ports where possible.
- Plan cleanup in `try/finally` or a shell trap before launching resources. Capture useful failure logs before teardown. Read-only diagnostics need no resource creation or cleanup.

For image builds, prefer an explicitly selected, disposable `docker-container` Buildx builder so its cache can be removed without pruning shared caches. Do not change the machine's default builder with `--use`. Remove the exact task builder afterward with `docker buildx rm`, without `--keep-state` or `--keep-daemon`. Track any images pulled for the builder as well.

At completion:

- Stop and remove task-owned containers and networks. For a new, isolated Compose project, use `down --volumes --remove-orphans` with the original project name and Compose files. Remove volumes only when they were created as disposable task data.
- Remove exact temporary image tags created by the task and any newly pulled images that are no longer needed or used elsewhere. Do not force removal. Remove the disposable builder and confirm its container and cache volume are gone.
- Remove only validated task-owned temporary files and directories. Preserve bind-mounted source, backups, persistent databases, external volumes, and pre-existing images or caches.
- Check for remaining task-labeled resources and inspect `docker system df` when builds or large pulls were involved. Report any resources intentionally retained or cleanup that failed, with the reason.

Never use global `docker system prune`, `docker volume prune`, `docker image prune -a`, or shared-builder cache pruning as routine cleanup. Do not stop unrelated containers, run `wsl --shutdown`, or compact the WSL disk as cleanup. WSL disk compaction is separate machine maintenance and requires explicit authorization.
