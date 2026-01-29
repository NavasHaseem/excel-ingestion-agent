# Pushing to GitHub

## Step 1: Create a Repository on GitHub

1. Go to [GitHub.com](https://github.com)
2. Click **New** (or go to your profile → Repositories → New)
3. Repository name: `excel-ingestion-agent`
4. Description: `Python agent for parsing Excel and normalizing test cases to JSON`
5. Choose: Public or Private
6. Click **Create repository**

## Step 2: Copy Your Repository URL

GitHub will show you options. Copy the **SSH** or **HTTPS** URL:
- SSH: `git@github.com:your-username/excel-ingestion-agent.git`
- HTTPS: `https://github.com/your-username/excel-ingestion-agent.git`

## Step 3: Push from Your Local Machine

### If you have Git installed locally:

```bash
# Navigate to your project
cd "c:\Users\Navas.Hasheem\OneDrive - Apexon\vsprojects\Excel Ingestion Agent"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Excel Ingestion Agent

- Flask web application for Excel parsing
- Standalone CLI and Python API
- Canonical test case JSON normalization
- AWS EC2 deployment configuration
- Complete test suite"

# Add remote repository
git remote add origin git@github.com:your-username/excel-ingestion-agent.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### If you don't have Git installed:

**Option A: Install Git**
- Download from [git-scm.com](https://git-scm.com)
- Follow installation instructions
- Then run the commands above

**Option B: Upload via GitHub Web Interface**
1. Go to your new repository on GitHub
2. Click **Upload files**
3. Select all files from your project folder
4. Commit with message: "Initial commit: Excel Ingestion Agent"

## Step 4: Verify Push

Visit: `https://github.com/your-username/excel-ingestion-agent`

You should see all your files uploaded!

## Configure Git (First Time Only)

If this is your first time using Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## SSH Key Setup (Recommended)

For SSH URLs, set up SSH keys:

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to SSH agent (Windows with Git Bash)
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key to GitHub
# 1. Cat your public key:
cat ~/.ssh/id_ed25519.pub

# 2. Go to GitHub Settings → SSH and GPG keys
# 3. Click New SSH key
# 4. Paste the key and save
```

## Future Updates

After initial setup, pushing updates is simple:

```bash
# Make changes to your files

# Stage changes
git add .

# Commit
git commit -m "Your commit message"

# Push
git push origin main
```

## Useful Git Commands

```bash
# Check status
git status

# View history
git log

# Create a new branch
git checkout -b feature/your-feature

# Switch branches
git checkout main

# Merge branch
git merge feature/your-feature

# Pull latest changes
git pull origin main
```

## Files to Push

All files in your project will be added, but .gitignore prevents:
- `venv/` - Virtual environment
- `uploads/*` - User uploaded files
- `output/*` - Generated output files
- `__pycache__/` - Python cache
- `.env.local` - Local environment variables

## Questions?

- [GitHub Help](https://docs.github.com/en)
- [Git Documentation](https://git-scm.com/doc)
- [SSH Key Help](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
