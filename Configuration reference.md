Absolutely — moving forward with the next major documentation page.  
Since we’ve already completed:

1. Landing Page  
2. Installation & Setup

…the natural next page in a professional docs flow is the Configuration Reference. This is the backbone of any gateway product, and it aligns perfectly with your governance‑first philosophy.

Below is a clean, production‑ready Jekyll Markdown file you can drop directly into your docs.

---

AI Gateway Ollama — Configuration Reference (Jekyll Markdown)

`markdown
---
layout: docs
title: "Configuration Reference"
description: "Full reference for all AI Gateway Ollama configuration options, including server, auth, logging, and model routing."
nav_order: 3
---

Configuration Reference

AI Gateway Ollama is configured using a single YAML file (config.yml) plus optional environment variables.  
This page documents every available setting, grouped by category.

All fields are optional unless marked required.

---

🖥️ Server Configuration

Controls how the gateway listens for incoming requests.

`yaml
server:
  host: "0.0.0.0"
  port: 8080
  request_timeout: 120
  maxrequestsize: "10mb"
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| host | string | Bind address for the HTTP server |
| port | number | Port to expose the gateway |
| request_timeout | number | Max seconds before a request is terminated |
| maxrequestsize | string | Maximum allowed payload size |

---

🤖 Ollama Backend

Defines how the gateway communicates with Ollama.

`yaml
ollama:
  host: "http://localhost:11434"
  timeout: 60
  healthcheck_interval: 10
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| host | string | URL of the Ollama instance |
| timeout | number | Max seconds to wait for Ollama responses |
| healthcheck_interval | number | Seconds between backend health checks |

Supports remote nodes, clusters, and load‑balanced setups.

---

🔐 Authentication

Enable API key–based access control.

`yaml
auth:
  enabled: true
  keys:
    - id: "admin"
      key: "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"
      scopes: ["*"]
    - id: "readonly"
      key: "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"
      scopes: ["chat:read"]
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| enabled | boolean | Turn authentication on/off |
| keys | list | List of API keys with scopes |

Scopes Examples

- * — full access  
- chat:read — read‑only  
- chat:write — send messages  
- models:list — list available models  

---

📊 Rate Limiting

Protects your gateway from abuse or runaway workloads.

`yaml
rate_limit:
  enabled: true
  requestsperminute: 60
  tokensperminute: 20000
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| enabled | boolean | Enable rate limiting |
| requestsperminute | number | Max requests per minute |
| tokensperminute | number | Max tokens generated per minute |

---

🧩 Model Routing

Map friendly service names to Ollama models.

`yaml
models:
  llama3:
    model: "llama3"
    version: "latest"
    max_tokens: 4096
  coder:
    model: "codellama"
    version: "13b"
    max_tokens: 8192
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| model | string | Name of the Ollama model |
| version | string | Version tag (optional) |
| max_tokens | number | Hard limit per request |

This allows you to expose:

- /v1/chat/completions?model=llama3  
- /v1/chat/completions?model=coder

…even if your backend model names differ.

---

📝 Logging & Audit Trails

Structured logs for governance, debugging, and compliance.

`yaml
logging:
  level: "info"
  format: "json"
  file: "logs/gateway.log"
  audit:
    enabled: true
    file: "logs/audit.log"
`

Fields

| Key | Type | Description |
|-----|------|-------------|
| level | string | debug, info, warn, error |
| format | string | text or json |
| file | string | Path to main log file |
| audit.enabled | boolean | Enable audit logging |
| audit.file | string | Path to audit log |

Audit logs include:

- Actor identity  
- Model used  
- Input/output metadata  
- Token counts  
- Timestamps  

---

🌐 CORS

`yaml
cors:
  enabled: true
  origins:
    - "https://gitdigital-products/github.io"
`

---

🔄 Environment Variables

Every config option can be overridden via environment variables.

Examples:

`bash
export SERVER_PORT=9090
export OLLAMA_HOST=http://remote-node:11434
export AUTH_ENABLED=true
`

Environment variables always override config.yml.

---

🧪 Validate Your Configuration

Run:

`bash
./gateway validate
`

This checks:

- YAML syntax  
- Missing required fields  
- Invalid types  
- Broken model mappings  

---
