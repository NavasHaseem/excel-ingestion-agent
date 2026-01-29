#!/bin/bash
# Excel Ingestion Agent - GitHub Push Script
# This script initializes git and pushes to GitHub

set -e

echo "=========================================="
echo "Excel Ingestion Agent - GitHub Setup"
echo "=========================================="

REPO_URL="https://github.com/NavasHaseem/excel-ingestion-agent.git"
PROJECT_DIR="."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed!"
    echo "Please install Git from https://git-scm.com/download"
    exit 1
fi

echo "✓ Git found: $(git --version)"

# Configure git (if not already configured)
echo ""
echo "Configuring git..."
git config --global user.name "Navas Haseem" || true
git config --global user.email "your-email@example.com" || true

# Initialize git repository
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

# Add all files
echo ""
echo "Adding files to git..."
git add .

# Create initial commit
echo "Creating initial commit..."
git commit -m "Initial commit: Excel Ingestion Agent

- Flask web application with REST API (/upload, /health, /template, /info)
- Excel parser supporting .xlsx and .xls formats
- Test case normalizer to canonical JSON format
- Standalone CLI tools (agent.py, agent_cli.py)
- Web UI for file uploads (upload.html)
- AWS EC2 deployment configuration and guides
- Complete test suite
- Comprehensive documentation

Features:
- Parses Excel files with customizable column mapping
- Normalizes test cases with priority and status fields
- Generates metadata-rich JSON output
- CORS-enabled REST API
- Production-ready systemd service configuration" || echo "Nothing to commit"

# Add remote origin
echo ""
echo "Adding remote repository..."
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"
echo "✓ Remote added: $REPO_URL"

# Rename main branch to main (if needed)
echo ""
echo "Setting up main branch..."
git branch -M main

# Push to GitHub
echo ""
echo "Pushing to GitHub..."
echo "NOTE: If using HTTPS, you may be prompted for credentials"
echo "NOTE: If using SSH, ensure SSH keys are configured"
echo ""

git push -u origin main

echo ""
echo "=========================================="
echo "✓ SUCCESS! Repository pushed to GitHub"
echo "=========================================="
echo ""
echo "Repository URL:"
echo "  https://github.com/NavasHaseem/excel-ingestion-agent"
echo ""
echo "Next steps:"
echo "1. Visit the repository on GitHub"
echo "2. Configure repository settings (README, description, topics)"
echo "3. Add collaborators if needed"
echo "4. Set up branch protection rules for main branch"
echo ""
