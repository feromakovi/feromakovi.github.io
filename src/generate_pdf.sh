#!/usr/bin/env bash
set -e

# Generate PDF from markdown using md-to-pdf
npx md-to-pdf assets/cv.md --launch-options '{"args": ["--no-sandbox", "--disable-setuid-sandbox"]}' --stylesheet src/pdf-style.css
mv assets/cv.pdf assets/richard_samela_cv.pdf
