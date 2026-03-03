AI Gateway Ollama — Installation & Setup (Jekyll Markdown)

`markdown
---
layout: docs
title: "Installation & Setup"
description: "How to install, configure, and run AI Gateway Ollama locally or in production."
nav_order: 2
---

Installation & Set
AI Gateway Ollama is designed to be lightweight, modular, and easy to deploy.  
You can run it locally for development or integrate it into a production environment with authentication, rate‑limiting, and audit logging.

---

## 🧱 Prerequisites

Before installing the gateway, ensure you have:

- Ollama installed and running  
  https://ollama.com/download  
- Git  
- A Unix-like environment (macOS, Linux, WSL2 recommended)
- Optional: Docker (for containerized deployments)

To verify Ollama is running:

`bash
ollama run llama3
`

If the model loads, you're good to go.

---

📦 Clone the Repository

`bash
git clone https://github.com/gitdigital-products/aigateway-ollama
cd aigateway-ollama
`

---

# ⚙️ Basic Configuration

The gateway reads configuration from:

- config.yml  
- Environment variables  
- Optional .env file  

A minimal example:

`yaml
server:
  host: "0.0.0.0"
  port: 8080

ollama:
  host: "http://localhost:11434"

auth:
  enabled: false
`

For production, you’ll likely enable:

- API keys  
- Rate limits  
- Request logging  
- Model access rules  

These are covered in the Configuration Reference page.

---

## ▶️ Start the Gateway

`bash
./gateway start
`

Or with verbose logging:

`bash
./gateway start --debug
`

Once running, open:

`
http://localhost:8080
`

You’ll see the API dashboard and model registry.

---

### 🐳 Running with Docker

If you prefer containerized deployment:

`bash
docker build -t aigateway-ollama .
docker run -p 8080:8080 aigateway-ollama
`

To connect to a remote Ollama node, set:

`bash
docker run -p 8080:8080 \
  -e OLLAMA_HOST=http://your-node:11434 \
  aigateway-ollama
`

---

#### 🔐 Production Hardening Checklist

- Enable API key authentication  
- Configure per‑model access rules  
- Turn on structured audit logging  
- Set rate limits and quotas  
- Run behind a reverse proxy (NGINX, Caddy, Traefik)  
- Use HTTPS everywhere  
- Pin model versions for reproducibility  

---

### 🧪 Testing the Gateway

Once running, test with:

`bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "messages": [{"role": "user", "content": "Hello!"}]
      }'
`

You should receive a structured JSON response.

---

