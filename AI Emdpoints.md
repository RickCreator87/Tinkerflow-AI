
---

AI Gateway Ollama — API Endpoints (Jekyll Markdown)

`markdown
---
layout: docs
title: "API Endpoints"
description: "Complete reference for all AI Gateway Ollama API endpoints, including chat, embeddings, models, and system routes."
nav_order: 4
---

API Endpoints

AI Gateway Ollama exposes a stable, versioned API designed for consistency, governance, and compatibility with common AI client libraries.

All endpoints are prefixed with:

`
/v1/
`

Authentication (if enabled) requires:

`
Authorization: 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
`

---

🗨️ Chat Completions

Generate chat-style responses from any configured model.

POST /v1/chat/completions

`bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "messages": [
          {"role": "user", "content": "Hello!"}
        ]
      }'
`

Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| model | string | yes | Name of the model (as defined in config.yml) |
| messages | array | yes | Chat history |
| max_tokens | number | no | Override model token limit |
| temperature | number | no | Creativity level |
| stream | boolean | no | Enable server‑sent streaming |

Response

`json
{
  "id": "chatcmpl-123",
  "model": "llama3",
  "choices": [
    {
      "index": 0,
      "message": {"role": "assistant", "content": "Hello! How can I help?"},
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 12,
    "total_tokens": 17
  }
}
`

---

🧠 Embeddings

Generate vector embeddings for text.

POST /v1/embeddings

`bash
curl -X POST http://localhost:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "input": "The quick brown fox"
      }'
`

Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| model | string | yes | Model to use |
| input | string/array | yes | Text to embed |

---

📚 Models

GET /v1/models

List all available models.

`bash
curl http://localhost:8080/v1/models
`

Response

`json
{
  "data": [
    {"id": "llama3", "version": "latest"},
    {"id": "coder", "version": "13b"}
  ]
}
`

---

🔍 Model Info

GET /v1/models/{model}

Retrieve metadata for a specific model.

`bash
curl http://localhost:8080/v1/models/llama3
`

---

🧪 Health & System Endpoints

GET /v1/health

Check gateway and backend status.

`bash
curl http://localhost:8080/v1/health
`

Response Example

`json
{
  "gateway": "ok",
  "ollama": "ok",
  "uptime_seconds": 1240
}
`

---

📜 Audit Logs (If Enabled)

GET /v1/audit/logs

Retrieve structured audit entries.

Supports filters:

`
/v1/audit/logs?actor=admin&model=llama3
`

---

🧵 Streaming Responses

Enable streaming by setting "stream": true in chat requests.

Example:

`bash
curl -N -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "stream": true,
        "messages": [{"role": "user", "content": "Tell me a story"}]
      }'
`

The server returns text/event-stream chunks until completion.

---

🛑 Error Responses

All errors follow a consistent structure:

`json
{
  "error": {
    "type": "invalid_request",
    "message": "Model not found"
  }
}
`

Common error types:

- invalid_request  
- unauthorized  
- rate_limited  
- backend_unavailable  
- internal_error  

---

