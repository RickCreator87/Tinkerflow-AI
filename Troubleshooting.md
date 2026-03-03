🛠️ Troubleshootingl

❗ Gateway Won’t Start

1. Port already in use
Error example:

`
Error: Port 8080 is already in use
`

Fix:  
Change the port in config.yml:

`yaml
server:
  port: 9090
`

---

2. Invalid YAML
If the gateway fails immediately, check for YAML formatting issues.

Fix:  
Run:

`bash
./gateway validate
`

---

3. Missing or unreadable config file

Ensure config.yml exists and is readable.

`bash
ls -l config.yml
`

---

❗ Gateway Can’t Reach Ollama

1. Ollama not running

Test:

`bash
curl http://localhost:11434/api/tags
`

If it fails, start Ollama:

`bash
ollama serve
`

---

2. Wrong Ollama host

Check your config:

`yaml
ollama:
  host: "http://localhost:11434"
`

If using Docker, you may need:

`
http://host.docker.internal:11434
`

---

❗ “Model not found”

This means the model name in your request doesn’t match your config.yml.

Example request:

`json
{ "model": "llama3" }
`

Check:

`yaml
models:
  llama3:
    model: "llama3"
`

---

❗ Authentication Errors

“Unauthorized” or “Missing API key”

If auth is enabled:

`yaml
auth:
  enabled: true
`

You must include:

`
Authorization: Bearer YOURAPIKEY
`

---

“Invalid scope”

Your key may not have permission for the model.

Check:

`yaml
scopes: ["models:llama3"]
`

---

❗ Rate Limit Errors

“Rate limit exceeded”

Increase limits:

`yaml
rate_limit:
  requestsperminute: 200
  tokensperminute: 50000
`

Or upgrade your hardware if Ollama is the bottleneck.

---

❗ Slow Responses

Possible causes:

- Model too large for your hardware  
- High concurrency  
- Streaming disabled  
- Backend timeout too low  

Try:

`yaml
ollama:
  timeout: 120
`

---

❗ Gateway Crashes Under Load

Check:

- maxrequestsize  
- request_timeout  
- System memory  
- Ollama logs  

Enable debug mode:

`bash
./gateway start --debug
`

---

❓ FAQ

Do I need Docker?
No. Docker is optional.  
You can run the gateway directly on macOS, Linux, or WSL2.

---

Does the gateway replace Ollama?
No — it wraps Ollama with:

- Governance  
- Logging  
- Rate limiting  
- Authentication  
- API stability  

---

Can I run multiple Ollama nodes?
Yes.  
You can point the gateway at a load balancer or custom router.

---

Can I expose custom model names?
Yes — that’s the purpose of the models: section.

---

Does the gateway support streaming?
Yes.  
Set "stream": true in chat requests.

---

Can I use this in production?
Yes — the gateway is designed for:

- Multi‑user environments  
- Internal teams  
- CI/CD automation  
- Governance‑aligned orgs  

---

Where are logs stored?

By default:

`
logs/gateway.log
logs/audit.log
`

You can change this in config.yml.

---

How do I contribute?
Open a PR or start a discussion in the repository.

---

