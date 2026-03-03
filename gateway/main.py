
---




This is the gateway brain.

from fastapi import FastAPI, Header, HTTPException
import requests
from policies import POLICIES

app = FastAPI()

OLLAMA_URL = "http://ollama:11434/api/chat"

@app.post("/v1/chat/completions")
def chat(payload: dict, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing API key")

    key = authorization.replace("Bearer ", "")
    policy = POLICIES.get(key)

    if not policy:
        raise HTTPException(status_code=403, detail="Invalid API key")

    ollama_payload = {
        "model": policy["model"],
        "messages": [
            {"role": "system", "content": policy["system_prompt"]},
            *payload.get("messages", [])
        ],
        "options": {
            "temperature": policy["temperature"]
        }
    }

    r = requests.post(OLLAMA_URL, json=ollama_payload)
    return r.json()
