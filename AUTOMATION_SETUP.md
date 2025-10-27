# Automated Marimo Notebook Builds

## ✅ What's Automated Now

### Local Development
When you run `bundle exec jekyll serve`:
1. **Jekyll hook** (`_plugins/build_marimo_notebooks.rb`) automatically:
   - Runs `python build_notebooks.py` before Jekyll builds
   - Runs `./copy_notebooks.sh` after Jekyll builds
2. Notebooks are built and copied **automatically** - no manual steps!

### Production Deployment (GitHub Actions)
When you push to `main` branch, GitHub Actions automatically:
1. **Checks out submodules** (teleworkability-index repo)
2. **Installs Python** and dependencies from `requirements.txt`
3. **Builds marimo notebooks** (`python build_notebooks.py`)
4. **Builds Jekyll site**
5. **Copies notebooks** to `_site/`
6. **Deploys to GitHub Pages**

## 🔧 Files Created/Modified

### New Files:
1. `_plugins/build_marimo_notebooks.rb` - Jekyll hooks for automatic builds
2. `copy_notebooks.sh` - Script to copy notebooks to _site
3. `AUTOMATION_SETUP.md` - This documentation

### Modified Files:
1. `.github/workflows/deploy.yml` - Added:
   - Submodule checkout
   - Python setup
   - Marimo notebook build steps
2. `requirements.txt` - Added marimo and dependencies

## 🚀 Usage

### Local Development
```bash
# Just run Jekyll as usual - notebooks build automatically!
cd /path/to/mitchv34.github.io-my-website
bundle exec jekyll serve --host 127.0.0.1 --port 4002
```

You'll see:
```
🔧 Building marimo notebooks...
✓ Marimo notebooks built successfully
Configuration file: _config.yml
...
📦 Copying marimo notebooks to site...
✓ Notebooks copied to _site
```

### Production Deployment
```bash
# Just push to GitHub - everything happens automatically!
git add .
git commit -m "Your changes"
git push origin main
```

GitHub Actions will:
- ✅ Build notebooks
- ✅ Build Jekyll site
- ✅ Deploy to GitHub Pages

## 📋 Workflow Summary

### Local: `bundle exec jekyll serve`
```
┌─────────────────────────┐
│  Start Jekyll           │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Hook: :after_init      │
│  → python build_notebooks.py │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Build Jekyll site      │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Hook: :post_write      │
│  → ./copy_notebooks.sh  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Site ready!            │
└─────────────────────────┘
```

### Production: GitHub Actions
```
┌─────────────────────────┐
│  Push to main           │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Checkout (+ submodules)│
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Setup Ruby + Python    │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  pip install -r requirements.txt │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  python build_notebooks.py │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  bundle exec jekyll build │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  ./copy_notebooks.sh    │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Deploy to Pages        │
└─────────────────────────┘
```

## 🔍 Troubleshooting

### Local Build Issues

**Problem:** Notebooks not building
```bash
# Check if marimo is installed
pip list | grep marimo

# Install dependencies manually
pip install -r requirements.txt
```

**Problem:** Hook not running
```bash
# Check if plugin exists
ls _plugins/build_marimo_notebooks.rb

# Restart Jekyll completely
```

### GitHub Actions Issues

**Problem:** Python dependencies failing
- Check `requirements.txt` is committed
- Check Actions log for specific errors

**Problem:** Submodule not checked out
- Verify `.gitmodules` exists and is committed
- Check Actions shows "Checkout (+ submodules)"

**Problem:** Notebooks not copied
- Check `copy_notebooks.sh` is executable: `chmod +x copy_notebooks.sh`
- Check it's committed to repo

## 📦 Adding New Notebooks

1. **Add notebook to project:**
   ```bash
   # In submodule
   cd projects/teleworkability-index/notebooks
   # Create new notebook
   marimo edit new_notebook.py
   ```

2. **Update datasets.yml:**
   ```yaml
   interactive:
     - label: "🎯 New Analysis"
       url: "/notebooks/teleworkability/new_notebook.html"
   ```

3. **Push changes:**
   ```bash
   # Push submodule first
   cd projects/teleworkability-index
   git add notebooks/new_notebook.py
   git commit -m "Add new analysis notebook"
   git push origin main
   
   # Then push website
   cd ../..
   git add projects/teleworkability-index _data/datasets.yml
   git commit -m "Update to latest teleworkability notebooks"
   git push origin main
   ```

4. **Automatic deployment** will handle the rest!

## 🎯 Benefits

✅ **No manual steps** - Everything automatic
✅ **Consistent** - Same process locally and in production
✅ **Version controlled** - Notebooks always match code
✅ **Fast iteration** - Edit → Push → Live
✅ **Reliable** - CI/CD handles dependencies

## 📝 Notes

- **First run** may take 2-3 minutes to install dependencies
- **Subsequent runs** are faster due to caching
- **Local builds** show progress in terminal
- **GitHub Actions** logs available in Actions tab

