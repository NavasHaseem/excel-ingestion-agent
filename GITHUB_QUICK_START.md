# Quick Start: Add Project to GitHub (Web Method)

## Steps to Create Repo and Upload Project

### Step 1: Create a New Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click your **profile icon** → **Your repositories** → **New**
   OR go directly to https://github.com/new

3. Fill in repository details:
   - **Repository name**: `excel-ingestion-agent`
   - **Description**: `Python agent for parsing Excel and normalizing test cases to JSON`
   - **Visibility**: Public (recommended) or Private
   - **Initialize repository**: 
     - ❌ Do NOT check "Add a README file"
     - ❌ Do NOT check "Add .gitignore"
     - ❌ Do NOT check "Choose a license"
   
4. Click **Create repository**

### Step 2: Get Your Repository URL

After creation, GitHub shows:
```
https://github.com/YOUR-USERNAME/excel-ingestion-agent
```

Copy this URL.

### Step 3: Upload Files (Web Method - No Git Required!)

1. Click **uploading an existing file** link (or click **Add file** → **Upload files**)
2. **Drag and drop** your project files into the upload area
3. Upload ALL files EXCEPT:
   - `venv/` folder (Python environment)
   - `uploads/` folder contents (user files)
   - `output/` folder contents (generated files)
   - `__pycache__/` folders
   - `.pyc` files

### Step 4: Commit Your Upload

1. Add commit message:
   ```
   Initial commit: Excel Ingestion Agent
   
   - Flask web application with REST API
   - Excel parser and test case normalizer
   - Standalone CLI tools
   - AWS EC2 deployment configuration
   - Complete documentation
   ```

2. Click **Commit changes**

### Step 5: Repository Created! ✅

Your repo is now live at:
```
https://github.com/YOUR-USERNAME/excel-ingestion-agent
```

---

## Files to Upload

### Required Files:
- ✅ `app.py`
- ✅ `agent.py`
- ✅ `agent_cli.py`
- ✅ `config.py`
- ✅ `upload.html`
- ✅ `requirements.txt`
- ✅ `README_GITHUB.md` → rename to `README.md`
- ✅ `LICENSE`
- ✅ `.gitignore_github` → rename to `.gitignore`
- ✅ `DEPLOYMENT.md`
- ✅ `ec2-setup.sh`
- ✅ `excel-agent.service`
- ✅ `.env` (environment template)

### Folders to Upload:
- ✅ `src/` (all files)
- ✅ `tests/` (all files)
- ✅ `.github/` (if exists)
- ✅ `.vscode/` (optional, VS Code settings)

### Files/Folders to SKIP:
- ❌ `venv/` (virtual environment)
- ❌ `uploads/` (user uploaded files)
- ❌ `output/` (generated files)
- ❌ `__pycache__/` (Python cache)
- ❌ `*.pyc` (Python compiled)
- ❌ `.pytest_cache/`
- ❌ `sample.txt` (if temporary)

---

## Rename Files Before Upload

GitHub web upload doesn't support file renames, so rename locally:

1. Rename `README_GITHUB.md` → `README.md`
2. Rename `.gitignore_github` → `.gitignore`

Then upload all files.

---

## After Upload

Your repository will have:
- Complete source code
- Full documentation
- Deployment guides
- Ready for AWS EC2 deployment
- Ready for team collaboration

---

## (Optional) Set Up Git Locally Later

Once you have Git installed, you can:

```bash
cd your-project
git clone https://github.com/YOUR-USERNAME/excel-ingestion-agent.git
cd excel-ingestion-agent
# Make changes
git add .
git commit -m "Your message"
git push origin main
```

---

## Your GitHub URL

Once created, share this URL:
```
https://github.com/YOUR-USERNAME/excel-ingestion-agent
```

✅ You're all set!
