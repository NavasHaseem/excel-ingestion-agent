# Excel Ingestion Agent - GitHub Push Script (PowerShell)
# This script initializes git and pushes to GitHub

$RepoURL = "https://github.com/NavasHaseem/excel-ingestion-agent.git"
$ProjectDir = Get-Location

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Excel Ingestion Agent - GitHub Setup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "✓ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/download" -ForegroundColor Yellow
    exit 1
}

# Configure git
Write-Host ""
Write-Host "Configuring git..." -ForegroundColor Yellow
git config --global user.name "Navas Haseem" 2>$null
git config --global user.email "your-email@example.com" 2>$null

# Initialize git repository
if (-not (Test-Path .\.git)) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "✓ Git repository already exists" -ForegroundColor Green
}

# Add all files
Write-Host ""
Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .

# Create initial commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
$commitMessage = @"
Initial commit: Excel Ingestion Agent

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
- Production-ready systemd service configuration
"@

try {
    git commit -m $commitMessage
} catch {
    Write-Host "Nothing to commit" -ForegroundColor Yellow
}

# Add remote origin
Write-Host ""
Write-Host "Adding remote repository..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin $RepoURL
Write-Host "✓ Remote added: $RepoURL" -ForegroundColor Green

# Rename main branch
Write-Host ""
Write-Host "Setting up main branch..." -ForegroundColor Yellow
git branch -M main

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "NOTE: If using HTTPS, you may be prompted for credentials" -ForegroundColor Cyan
Write-Host "NOTE: If using SSH, ensure SSH keys are configured" -ForegroundColor Cyan
Write-Host ""

git push -u origin main

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "✓ SUCCESS! Repository pushed to GitHub" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Repository URL:" -ForegroundColor Cyan
Write-Host "  https://github.com/NavasHaseem/excel-ingestion-agent" -ForegroundColor Yellow
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Visit the repository on GitHub" -ForegroundColor White
Write-Host "2. Configure repository settings (README, description, topics)" -ForegroundColor White
Write-Host "3. Add collaborators if needed" -ForegroundColor White
Write-Host "4. Set up branch protection rules for main branch" -ForegroundColor White
Write-Host ""
