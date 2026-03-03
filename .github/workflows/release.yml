#!/bin/bash
set -euo pipefail

echo "----------------------------------------"
echo "🚀 RELEASE: Preparing release metadata"
echo "----------------------------------------"

# Generate version
VERSION="v$(date +'%Y.%m.%d.%H%M')"
echo "📌 Version: $VERSION"

# Generate changelog entry
CHANGELOG=$(git log -1 --pretty=format:"%h %s")
echo "📝 Changelog: $CHANGELOG"

# Write metadata to file for GitHub Actions to consume
mkdir -p .release
echo "$VERSION" > .release/version.txt
echo "$CHANGELOG" > .release/changelog.txt

echo "----------------------------------------"
echo "🚀 RELEASE: Metadata generated"
echo "----------------------------------------"
exit 0
