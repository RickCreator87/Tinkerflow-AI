#!/bin/bash
set -euo pipefail

echo "🔧 Building project..."

# Ensure dist directory exists
mkdir -p dist

# Example build output
echo "Build artifact" > dist/output.txt

echo "✅ Build complete."
