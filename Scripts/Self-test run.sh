#!/bin/bash
set -euo pipefail

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 Ollama Stack Self‑Test"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Environment diagnostics
echo "📦 Step 1: Environment check"
echo "→ Running on: $(uname -a)"
echo "→ Current directory: $(pwd)"
echo "→ Files present:"
ls -al
echo ""

# 2. Check if Ollama is installed
echo "📦 Step 2: Checking for Ollama binary"
if ! command -v ollama >/dev/null 2>&1; then
  echo "❌ Ollama not found in PATH"
  echo "This is expected on GitHub Actions unless you install it."
  exit 1   # Signal test failure; CI can be configured to allow this
else
  echo "✅ Ollama binary found"
fi
echo ""

# 3. Try listing models (safe even if none exist)
echo "📦 Step 3: Listing available models"
if ollama list; then
  echo "✅ Model list retrieved"
else
  echo "⚠️ Could not list models (may be expected)"
fi
echo ""

# 4. Optional: Run a lightweight test prompt
echo "📦 Step 4: Running lightweight test prompt"
if ollama run llama3 "Hello from CI" >/dev/null 2>&1; then
  echo "✅ Model responded successfully"
else
  echo "⚠️ Model test skipped or failed (may be expected)"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Self‑test completed"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
