# CI

PR CI runs:

- `uv sync --locked`
- Ruff lint
- Ruff format check
- mypy
- `pip-audit`
- pytest with PostgreSQL integration tests
- Docker build validation

Release CI on `main`:

- Re-runs validation
- Builds the container once
- Pushes `ghcr.io/<owner>/upskill-api:sha-<short-sha>`
- Checks out `homelab-gitops`
- Updates the DEV Kustomize image tag
- Commits and pushes the GitOps change to `main`

GitHub Actions does not need kubeconfig, Kubernetes API access, or `kubectl`.

Minimum permissions:

- App repo `GITHUB_TOKEN`: `contents: read`, `packages: write`
- `GITOPS_DEPLOY_KEY`: write deploy key scoped only to `homelab-gitops`
