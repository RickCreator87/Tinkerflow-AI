#!/usr/bin/env bash

echo "🔧 Workflow Repair & Diagnostics Tool"
echo "-------------------------------------"

WORKFLOW_DIR=".github/workflows"

echo "📁 Checking workflow directory: $WORKFLOW_DIR"
if [ ! -d "$WORKFLOW_DIR" ]; then
  echo "❌ No workflows directory found."
  exit 1
fi

echo "🔍 Validating YAML syntax..."
for file in $WORKFLOW_DIR/*.yml; do
  echo "Checking $file"
  yamllint "$file"
done

echo "🔍 Checking for unpinned actions..."
grep -R "uses: .*@" -n $WORKFLOW_DIR | grep "@master\|@main"
if [ $? -eq 0 ]; then
  echo "❌ Found unpinned actions."
else
  echo "✔️ All actions pinned."
fi

echo "🔍 Checking permissions blocks..."
for file in $WORKFLOW_DIR/*.yml; do
  if ! grep -q "permissions:" "$file"; then
    echo "⚠️ Missing permissions block in $file"
  fi
done

echo "🔍 Checking for referenced secrets..."
grep -R "secrets." -n $WORKFLOW_DIR || echo "✔️ No secrets referenced."

echo "🧩 Diagnostics complete."
echo "Check output above for warnings or errors."
