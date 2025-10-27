# Marimo Notebooks Integration

This site includes interactive marimo notebooks that run in the browser using WebAssembly (WASM).

## Automatic Building

Marimo notebooks are **automatically built** when you start the development server:

```bash
# Using bundle exec (native)
bundle exec jekyll serve

# Using Docker
docker compose up
```

The build system will:
1. Check if source notebooks are newer than built HTML files
2. Build notebooks only if changes are detected
3. Copy notebooks and their data dependencies to `_site/`

## Manual Building

To manually rebuild notebooks:

```bash
python build_notebooks.py
```

## Directory Structure

```
notebooks/                    # Root-level notebooks
projects/
  └── project-name/
      ├── notebooks/         # Project-specific notebooks (auto-discovered)
      ├── data/              # Data files (auto-copied for WASM access)
      └── results/           # Results files (auto-copied for WASM access)
marimo_site/                 # Build output (gitignored)
_site/
  ├── marimo.html           # Notebook index page
  ├── notebooks/            # Root notebooks + assets
  └── projects/             # Project notebooks + data + results
```

## Adding New Notebooks

1. **Create a marimo notebook:**
   ```bash
   marimo edit notebooks/my_notebook.py
   # or for projects:
   marimo edit projects/my-project/notebooks/my_notebook.py
   ```

2. **For notebooks that load data files:**
   - Store data in `projects/my-project/data/` or `results/`
   - Use WASM-compatible data loading (see example below)

3. **Rebuild and test:**
   ```bash
   python build_notebooks.py
   bundle exec jekyll serve
   # Open http://localhost:4000/marimo.html
   ```

## WASM-Compatible Data Loading

When notebooks run in the browser, they need to fetch data via HTTP. Use this pattern:

```python
import sys
from pathlib import Path

# Detect if running in WASM (Pyodide)
is_wasm = sys.platform == "emscripten"

if is_wasm:
    # In WASM, use relative URLs from notebook location
    data_path = "../data/my_data.csv"
else:
    # Local execution: use file paths
    data_path = Path(__file__).parent.parent / "data" / "my_data.csv"

df = pd.read_csv(data_path)
```

## Build Process Details

### Jekyll Plugin (`_plugins/build_marimo_notebooks.rb`)
- Runs on Jekyll startup (`:after_init` hook)
- Checks file modification times
- Rebuilds only if source notebooks are newer than built HTML

### Build Script (`build_notebooks.py`)
- Exports notebooks to HTML with WASM runtime
- Copies data/results directories for each project
- Generates index page at `marimo_site/index.html`

### Copy Script (`copy_notebooks.sh`)
- Runs after Jekyll build (`:post_write` hook)
- Copies `marimo_site/` contents to `_site/`
- Preserves directory structure for correct relative paths

## Deployment

GitHub Actions automatically:
1. Installs Python dependencies (including marimo)
2. Builds notebooks before Jekyll build
3. Copies notebooks to `_site/` after Jekyll build
4. Deploys to GitHub Pages

See `.github/workflows/deploy.yml` for details.

## Troubleshooting

### Notebooks not showing figures/tables
- **Cause:** Data files not accessible or wrong path
- **Fix:** Check that data files are in `results/` or `data/` directories and use WASM-compatible loading pattern

### "FileNotFoundError" in browser console
- **Cause:** Data file path is incorrect for WASM environment
- **Fix:** Use relative URLs (e.g., `"../data/file.csv"`) when `sys.platform == "emscripten"`

### Notebooks not rebuilding on changes
- **Cause:** Modification times not updated
- **Fix:** Force rebuild with `python build_notebooks.py` or `touch` the notebook file

### Jekyll not finding plugin
- **Cause:** Plugin not in `_plugins/` directory
- **Fix:** Ensure `_plugins/build_marimo_notebooks.rb` exists and is executable

## Resources

- [Marimo Documentation](https://docs.marimo.io/)
- [Marimo WASM Export](https://docs.marimo.io/guides/exporting.html#webassembly-wasm)
- [Pyodide](https://pyodide.org/) - Python runtime in the browser
