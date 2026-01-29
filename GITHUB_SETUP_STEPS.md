# GitHub Repository Setup Guide

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Enter repository name: `excel-ingestion-agent`
3. Add description: "Excel ingestion agent that parses and normalizes test cases to canonical JSON format"
4. Select: **Public** repository
5. Check **Add a README file** (optional - we'll replace it)
6. Check **Add .gitignore** and select **Python**
7. Check **Add a license** and select **MIT License**
8. Click **Create repository**

## Step 2: Prepare GitHub Credentials

### Option A: Using HTTPS (Simpler for first-time users)

1. Go to https://github.com/settings/personal-access-tokens/new
2. Create a new Personal Access Token:
   - Select **Tokens (classic)** 
   - Give it a name: "Excel Agent Push"
   - Select scope: **repo** (full control of private repositories)
   - Click **Generate token**
3. Copy the token (you'll need it for authentication)
4. Keep this token safe - you'll use it as your password when prompted

### Option B: Using SSH (Recommended for regular use)

1. Generate SSH key (if you don't have one):
   ```powershell
   ssh-keygen -t ed25519 -C "your-email@example.com"
   ```
2. Accept default location by pressing Enter
3. Enter a passphrase (or press Enter for no passphrase)
4. Go to https://github.com/settings/ssh/new
5. Title: "Excel Agent Machine"
6. Key type: **Authentication Key**
7. Paste your public key (from `~/.ssh/id_ed25519.pub`)
8. Click **Add SSH key**

## Step 3: Execute Git Push

### Option A: Using PowerShell (Windows)

```powershell
# Navigate to project directory
cd "C:\Users\Navas.Hasheem\OneDrive - Apexon\vsprojects\Excel Ingestion Agent"

# Run the push script
.\push-to-github.ps1
```

When prompted for credentials:
- **Username**: Your GitHub username (NavasHaseem)
- **Password**: Your Personal Access Token (from Step 2, Option A) OR empty if using SSH

### Option B: Manual Git Commands

```powershell
# Navigate to project directory
cd "C:\Users\Navas.Hasheem\OneDrive - Apexon\vsprojects\Excel Ingestion Agent"

# Configure git
git config --global user.name "Navas Haseem"
git config --global user.email "your-email@example.com"

# Initialize repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Excel Ingestion Agent with Flask API, parser, normalizer, and deployment configs"

# Add remote
git remote add origin https://github.com/NavasHaseem/excel-ingestion-agent.git

# Rename and push
git branch -M main
git push -u origin main
```

## Step 4: Verify Upload

1. Go to https://github.com/NavasHaseem/excel-ingestion-agent
2. Verify you see your project files:
   - `/src` folder with parser.py, normalizer.py, agent.py, models.py
   - `app.py` (Flask application)
   - `upload.html` (Web UI)
   - `requirements.txt`
   - `config.py`
   - Other supporting files
3. Check the commit history shows your initial commit

## Step 5: (Optional) Update Repository Settings

1. Go to repository Settings
2. Add topics: `excel`, `test-cases`, `python`, `flask`, `json`
3. Add description and website URL if desired
4. Enable GitHub Pages if you want to host documentation
5. Configure branch protection for `main` branch for production-grade security

## Troubleshooting

### "Git is not installed"
- Download from https://git-scm.com/download/win
- Run installer with default settings
- Restart PowerShell/terminal after installation

### "fatal: 'origin' does not appear to be a 'git' repository"
- Run: `git init` first
- Then: `git remote add origin https://github.com/NavasHaseem/excel-ingestion-agent.git`

### "Authentication failed"
- If using HTTPS: Check your Personal Access Token has `repo` scope
- If using SSH: Verify SSH key is added to GitHub (https://github.com/settings/keys)
- Try: `git config --global credential.helper store` to save credentials

### "Repository already exists on remote"
- Go to https://github.com/NavasHaseem/excel-ingestion-agent/settings
- Click "Delete this repository" (if starting fresh)
- OR reset local git: `rm -r .git` then start over

## Next Steps After Upload

1. **Clone repository on EC2**:
   ```bash
   git clone https://github.com/NavasHaseem/excel-ingestion-agent.git
   cd excel-ingestion-agent
   ```

2. **Update deployment script** with your EC2 details

3. **Share repository**: Send link to https://github.com/NavasHaseem/excel-ingestion-agent

4. **Add collaborators**: Settings → Collaborators → Add people

5. **Create releases**: For version tracking and distribution

---

**Questions?** Review the README_GITHUB.md in your project for detailed documentation.
