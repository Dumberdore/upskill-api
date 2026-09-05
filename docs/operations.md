# Operations

Health semantics:

- `/health/live`: process is alive; does not check PostgreSQL.
- `/health/ready`: app can serve traffic; checks PostgreSQL.
- `/health/startup`: startup completed.

Local checks:

```bash
curl http://127.0.0.1:8000/health/live
curl http://127.0.0.1:8000/health/ready
curl http://127.0.0.1:8000/health/startup
```

Kubernetes checks live in `homelab-gitops` docs because cluster operations are platform-owned.

Application logs are structured JSON to stdout for future integration with centralized logging.
