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

Current repository controls:

- Repository visibility is public.
- `main` requires pull requests.
- CODEOWNERS review is required.
- The `check` status check is required.
- Force pushes and branch deletion are blocked.
- `@Dumberdore` may bypass only through pull requests for single-owner operability.

GitHub Environments:

- `dev`: unrestricted; used for automation-friendly development deployment.
- `staging`: required reviewer is `@Dumberdore`.
- `prod`: required reviewer is `@Dumberdore`.
