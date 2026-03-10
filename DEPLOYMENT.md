DEPLOYMENT.md

```markdown
# Deployment Guide

Tinkerflow-AI can be deployed as a self-hosted service or run in our cloud.

## Self-Hosted (Docker)

### Prerequisites

- Docker and Docker Compose
- GitHub App credentials (see [Creating a GitHub App](https://docs.github.com/en/developers/apps/creating-a-github-app))

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/tinkerflow/tinkerflow-ai.git
   cd tinkerflow-ai
```

1. Copy environment template:
   ```bash
   cp .env.example .env
   # Edit .env with your GitHub App credentials
   ```
2. Build and run:
   ```bash
   docker-compose up -d
   ```
3. The service will be available at http://localhost:8080. Configure your GitHub App webhook URL to point to https://your-domain.com/webhooks/github.

Kubernetes

Helm charts are available in the helm/ directory.

Cloud (Managed)

Visit tinkerflow.ai to sign up for the managed service. We handle scaling, updates, and monitoring.

Configuration

See Configuration Reference for all environment variables and config files.

```
