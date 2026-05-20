#!/usr/bin/env bash
set -e

# Configure git
git config --local user.email "github-actions[bot]@users.noreply.github.com"
git config --local user.name "github-actions[bot]"

# Stage the auto-generated files
git add index.md README.md assets/richard_samela_cv.pdf

# Only commit and push if there are actual modifications staged
if git diff --cached --quiet; then
  echo "No changes to commit"
else
  git commit -m "docs: auto-generate index.md, README.md, and CV PDF [skip ci]"
  git push origin main
fi
