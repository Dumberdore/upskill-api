# upskill-api

Small FastAPI reference service for a production-like homelab Kubernetes delivery model.

This repository owns application code, tests, migrations, and the production container image. Kubernetes desired state lives separately in `homelab-gitops`.

## Local Development

FastAPI runs natively on the Mac. PostgreSQL runs through Docker Compose.

```bash
uv sync
just migrate
just dev
```

Useful commands:

```bash
just sync
just test
just lint
just format
just typecheck
just check
just audit
just container-build
```

Health endpoints:

```bash
curl http://127.0.0.1:8000/health/live
curl http://127.0.0.1:8000/health/ready
curl http://127.0.0.1:8000/health/startup
```

Courses API:

```bash
curl http://127.0.0.1:8000/api/v1/courses
```

## Operating Model

Local development does not require Kubernetes. Kubernetes deployment is handled through Kustomize, GitOps, and Argo CD in the separate `homelab-gitops` repository. GitHub Actions builds/publishes immutable images and updates Git desired state; it must not use Kubernetes credentials or run `kubectl`.

Docs:

- `docs/architecture.md`
- `docs/local-development.md`
- `docs/ci.md`
- `docs/deployment.md`
- `docs/gitops.md`
- `docs/governance.md`
- `docs/migrations.md`
- `docs/operations.md`
- `docs/production-mapping.md`
