# Teleworkability Index Integration

## ✅ Setup Complete!

The teleworkability-index repository has been added as a Git submodule and integrated with your website.

### Structure

```
mitchv34.github.io-my-website/
├── projects/
│   └── teleworkability-index/       # Git submodule
│       ├── data/                     # O*NET + ORS data
│       ├── results/                  # Model outputs & predictions
│       ├── wfh_share_estimation.py   # Core ML pipeline
│       ├── run_wfh_share_minimal.py  # Training script
│       └── notebooks/                # 🎉 NEW: Marimo notebooks
│           ├── explore_index.py      # Interactive data exploration
│           ├── retrain_model.py      # Model retraining interface
│           └── feature_explorer.py   # Feature importance analysis
├── build_notebooks.py                # Updated to scan projects/
├── marimo_site/                      # Built HTML outputs
└── _site/notebooks/                  # Deployed to Jekyll site
```

### Three Interactive Notebooks

1. **explore_index.py** - Data exploration (fast, read-only)
   - Filter by occupation, category, source
   - Distribution charts
   - Top/bottom rankings
   - Summary statistics
   
2. **retrain_model.py** - Model retraining (10-30 seconds)
   - Adjust hyperparameters (trees, depth, threshold)
   - Train new model in browser
   - Compare with baseline
   - Download new predictions
   
3. **feature_explorer.py** - Feature importance (analysis)
   - MDI and permutation importance
   - Feature direction (increases/decreases teleworkability)
   - Category breakdowns

### Workflows

#### Update Index Repo Only
```bash
cd projects/teleworkability-index/
# Edit code, notebooks, data
git add .
git commit -m "Update teleworkability index"
git push origin main
```

#### Pull Latest Index into Website
```bash
cd /path/to/mitchv34.github.io-my-website

# Update submodule to latest
git submodule update --remote projects/teleworkability-index

# Rebuild marimo notebooks
python build_notebooks.py

# Copy to Jekyll site
cp -r marimo_site/projects _site/notebooks/

# Commit (updates submodule pointer)
git add projects/teleworkability-index build_notebooks.py
git commit -m "Update to latest teleworkability index"
git push origin main
```

#### Update Website Only (No Index Changes)
```bash
# Edit website pages, config, etc.
git add _pages/ _config.yml
git commit -m "Update website content"
git push origin main
# Submodule stays at same commit
```

### URLs (After Deployment)

- Explore Index: `http://localhost:4002/notebooks/projects/teleworkability-index/notebooks/explore_index.html`
- Retrain Model: `http://localhost:4002/notebooks/projects/teleworkability-index/notebooks/retrain_model.html`
- Feature Explorer: `http://localhost:4002/notebooks/projects/teleworkability-index/notebooks/feature_explorer.html`

### Next Steps

1. **Create landing page** at `_pages/teleworkability.md`
2. **Add to navigation** in `_config.yml`
3. **Test notebooks** locally
4. **Create post-Jekyll copy script** to ensure notebooks persist after rebuild
5. **Push both repos** to GitHub

### Commands Reference

```bash
# Build notebooks
python build_notebooks.py

# Test locally
python -m http.server -d marimo_site

# Initialize submodule (for others cloning your repo)
git submodule init
git submodule update

# Update all submodules to latest
git submodule update --remote --recursive
```

