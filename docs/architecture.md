# Architecture

```mermaid
flowchart LR
  mac[Developer Mac] --> github[GitHub]
  github --> actions[GitHub Actions CI]
  actions --> ghcr[GHCR immutable image]
  actions --> gitops[homelab-gitops repo]
  argocd[Argo CD in cluster] --> gitops
  argocd --> k8s[Talos Kubernetes]
  k8s --> api[upskill-api]
  api --> pg[PostgreSQL]
```

Rules:

- Kubernetes is not publicly exposed.
- GitHub Actions never deploys directly to Kubernetes.
- Argo CD pulls desired state from GitHub using outbound connectivity.
- The app repo owns code, tests, migrations, and Dockerfile.
- The GitOps repo owns Kustomize deployment state and environment promotion.
- Images are immutable and tagged as `sha-<git-sha>`.
- The same image tag is promoted across environments.
