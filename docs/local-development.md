# Local Development

Fast loop:

```bash
uv sync
just migrate
just dev
```

`just dev` starts PostgreSQL with Docker Compose and runs FastAPI natively on macOS with reload enabled.

Useful checks:

```bash
just lint
just format
just typecheck
just test
just check
```

Production container check:

```bash
just container-build
just container-run
```

Kubernetes is intentionally not part of the normal development loop.
