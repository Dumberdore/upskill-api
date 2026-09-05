# Production Mapping

Homelab to AWS mapping:

- Talos Kubernetes -> AWS EKS
- GHCR -> ECR
- Kubernetes PostgreSQL -> RDS PostgreSQL
- Local ingress -> AWS Load Balancer Controller or managed ingress
- Kubernetes Secrets -> AWS Secrets Manager plus External Secrets Operator
- Kubernetes ServiceAccount -> EKS Pod Identity
- local-path persistent storage -> EBS or EFS where appropriate
- Argo CD in homelab -> Argo CD for EKS
- GitHub Actions -> same CI model

The homelab reproduces the operating model, not production high availability. The single-node cluster cannot provide real infrastructure isolation, multi-AZ failover, or production-grade durability.
