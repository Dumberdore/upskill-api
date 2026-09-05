# Governance

Initial ownership uses `@Dumberdore` as the sole CODEOWNER.

Intended production shape:

- Application team owns FastAPI code, tests, migrations, Dockerfile, and runtime behavior.
- Platform team owns CI/CD conventions, release guardrails, and deployment paved road.
- Humans change `main` through pull requests.
- Automation may update DEV GitOps state directly after a successful release build.
- STAGING and PROD promotion should require explicit approval.

Current limitation:

- The initial DEV automation uses an SSH deploy key to update `homelab-gitops`.
- A GitHub App or service account would provide better audit identity in a larger platform.
