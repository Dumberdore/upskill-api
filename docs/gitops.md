# GitOps

`homelab-gitops` is the source of truth for Kubernetes desired state.

The app repo does not contain cluster manifests, except CI knowledge of which GitOps overlay to update on release.

Argo CD responsibilities:

- Pull Git desired state
- Render Kustomize
- Apply drift correction
- Run PreSync migration jobs
- Report sync and health status

Argo CD does not build images.

The initial GitOps repo uses explicit Argo CD `Application` resources rather than `ApplicationSet`. That is intentional while there is only one app, one database dependency, and three logical environments. ApplicationSet is the documented next step when more services, clusters, or generated environments make the repetition painful.
