# Deployment

Deployment state lives in `homelab-gitops` and is rendered with Kustomize.

Flow:

```mermaid
sequenceDiagram
  participant Dev as Developer
  participant GH as GitHub
  participant CI as GitHub Actions
  participant GHCR as GHCR
  participant GO as homelab-gitops
  participant Argo as Argo CD
  participant K8s as Kubernetes

  Dev->>GH: Push to main
  GH->>CI: Trigger release workflow
  CI->>GHCR: Push sha-tagged image
  CI->>GO: Update DEV Kustomize image
  Argo->>GO: Pull desired state
  Argo->>K8s: Reconcile manifests
```

DEV deploys automatically from `main`. STAGING and PROD promote the same image tag by editing the GitOps overlays. No rebuild occurs between environments.
