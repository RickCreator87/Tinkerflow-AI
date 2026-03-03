You got it — I’ll deliver all remaining Jekyll documentation pages, one by one, clean, production‑read
AI Gateway Ollama — Model Management (Jekyll Markdown)

`markdown
---
layout: docs
title: "Model Management"
description: "How to register, configure, version, and manage models in AI Gateway Ollama."
nav_order: 5
---

Model Management

AI Gateway Ollama provides a clean, governance‑aligned way to expose Ollama models as stable services.  
This page explains how to register models, version them, and control access.

---

📁 Defining Models in config.yml

Models are declared under the models: section:

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

Each entry creates a named service accessible through the API.

---

🔖 Model Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| model | string | yes | Name of the Ollama model |
| version | string | no | Version tag or alias |
| max_tokens | number | no | Hard limit per request |

---

🧩 Why Use Named Services?

Instead of exposing raw Ollama model names, the gateway lets you:

- Create stable service names (llama3, coder)  
- Swap backend models without breaking clients  
- Pin versions for reproducibility  
- Apply per‑model access rules  
- Enforce per‑model token limits  

This is essential for governance and long‑term maintainability.

---

🔄 Updating Models

To update a model:

1. Pull or create the new model in Ollama  
2. Update the gateway config  
3. Restart the gateway

Example:

`yaml
models:
  llama3:
    model: "llama3"
    version: "8b"
`

Clients continue using:

`
model: "llama3"
`

…without needing to change anything.

---

🧪 Testing a Model

`bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "messages": [{"role": "user", "content": "Test"}]
      }'
`

---

🔐 Per‑Model Access Control

If authentication is enabled, you can restrict models by scope:

`yaml
auth:
  enabled: true
  keys:
    - id: "developer"
      key: "DEV_KEY"
      scopes: ["chat:write", "models:llama3"]
`

This ensures sensitive or expensive models are protected.

---

🧱 Model Version Pinning

For reproducibility:

`yaml
models:
  llama3:
    model: "llama3"
    version: "3.1.0"
`

This prevents accidental upgrades.

---

🧰 Model Aliasing

Expose multiple names for the same backend model:

`yaml
models:
  general:
    model: "llama3"
  creative:
    model: "llama3"
    temperature: 1.2
`

Useful for UX‑focused or persona‑based endpoints.

---

🧮 Token Limits

Override per‑model limits:

`yaml
models:
  coder:
    model: "codellama"
    max_tokens: 16384
`

The gateway enforces this even if Ollama does not.

---

