AI Gateway Ollama — Usage Examples (Jekyll Markdown)

`markdown
---
layout: docs
title: "Usage Examples"
description: "Practical examples for using AI Gateway Ollama with curl, JavaScript, Python, and automation workflows."
nav_order: 6
---

Usage Examples

This page provides practical examples for interacting with AI Gateway Ollama using common tools and languages.  
All examples assume the gateway is running at:

`
http://localhost:8080
`

If authentication is enabled, include:

`
Authorization: Bearer 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
`

---

🧪 Basic Chat Completion (curl)

`bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "messages": [
          {"role": "user", "content": "Explain quantum computing simply."}
        ]
      }'
`

---

🧵 Streaming Responses (curl)

`bash
curl -N -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "stream": true,
        "messages": [
          {"role": "user", "content": "Tell me a story about a robot."}
        ]
      }'
`

---

🧠 Embeddings (curl)

`bash
curl -X POST http://localhost:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "input": "The quick brown fox jumps over the lazy dog."
      }'
`

---

🟦 JavaScript Example (Node.js / Browser)

`javascript
const response = await fetch("http://localhost:8080/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "llama3",
    messages: [
      { role: "user", content: "Write a haiku about mountains." }
    ]
  })
});

const data = await response.json();
console.log(data.choices[0].message.content);
`

---

🐍 Python Example

`python
import requests

payload = {
    "model": "llama3",
    "messages": [
        {"role": "user", "content": "Summarize the concept of entropy."}
    ]
}

res = requests.post(
    "http://localhost:8080/v1/chat/completions",
    json=payload
)

print(res.json()["choices"][0]["message"]["content"])
`

---

⚙️ Using the Gateway in GitHub Actions

Useful for CI tasks, automated documentation, or internal bots.

`yaml
jobs:
  ai_task:
    runs-on: ubuntu-latest
    steps:
      - name: Query AI Gateway
        run: |
          curl -X POST http://gateway:8080/v1/chat/completions \
            -H "Content-Type: application/json" \
            -d '{
                  "model": "llama3",
                  "messages": [
                    {"role": "user", "content": "Generate release notes for version 1.2.0."}
                  ]
                }'
`

---

🧰 Using Environment Variables

`bash
export GATEWAY_URL=http://localhost:8080
export MODEL=llama3

curl -X POST $GATEWAY_URL/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d "{
        \"model\": \"$MODEL\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hello!\"}]
      }"
`

---

🧩 Using the Gateway with Frontend Apps

Because the gateway supports CORS, you can call it directly from:

- React  
- Vue  
- Svelte  
- Next.js  
- Mobile apps  

Example (React):

`javascript
async function ask() {
  const res = await fetch("http://localhost:8080/v1/chat/completions", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      model: "llama3",
      messages: [{ role: "user", content: "Give me a productivity tip." }]
    })
  });

  const data = await res.json();
  console.log(data.choices[0].message.content);
}
`

---

🛠️ Advanced Example: System Prompts

`bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "llama3",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant that speaks like a pirate."},
          {"role": "user", "content": "How do I tie a knot?"}
        ]
      }'
`

---

🎯 Next Steps

Continue to:

- Troubleshooting & FAQ
`

---

If you want, I’ll continue immediately with:

7. Troubleshooting & FAQ

8. Sidebar Navigation Structure

Just say continue and I’ll deliver the next page.
