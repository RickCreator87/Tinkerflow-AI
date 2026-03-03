#!/bin/bash
set -euo pipefail

echo "----------------------------------------"
echo "🏗️ BUILD: Starting build process"
echo "----------------------------------------"

# Clean previous build
if [ -d "dist" ]; then
  echo "🧹 Cleaning existing dist/ directory"
  rm -rf dist
fi

mkdir -p dist

# Example build step — replace with your real build logic
echo "📦 Building project..."
echo "Build output generated on $(date)" > dist/build-info.txt

echo "----------------------------------------"
echo "🏗️ BUILD: Completed successfully"
echo "----------------------------------------"
exit 0
