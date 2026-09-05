# Migrations

Alembic migrations are application-owned but deployment-executed.

Local:

```bash
just migrate
```

Kubernetes:

- A Kustomize-managed Kubernetes Job runs `alembic upgrade head`.
- Argo CD runs the Job as a PreSync hook.
- App pods do not run migrations during startup.

Backward-compatible pattern:

- Expand: add nullable columns/tables/indexes first.
- Migrate: backfill or dual-write where needed.
- Contract: remove old fields only after old app versions are gone.

If a migration fails, the rollout should stop and the previous app version should continue serving where possible.
