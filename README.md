
---


README.md

This keeps future-you sane.

# AI Gateway (Ollama)

This repo runs a simple AI gateway in front of Ollama.

## How it works
- Clients send requests to `/v1/chat/completions`
- API key determines model + behavior
- Gateway forwards request to Ollama

## Run locally
1. Copy `.env.example` → `.env`
2. `docker compose up --build`
3. Call API on `http://localhost:8000`

## API Example
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Authorization: Bearer dev-key-123" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Review this function"}
    ]
  }'
```

# AIGateway-Ollama
