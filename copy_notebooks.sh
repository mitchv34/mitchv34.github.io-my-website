#!/bin/bash
# Post-Jekyll build script to copy marimo notebooks to _site

echo "📦 Copying marimo notebooks to Jekyll site..."

# Copy the entire marimo_site structure to _site
# This preserves the paths expected by marimo_site/index.html
if [ -d "marimo_site" ]; then
    # Copy marimo index page
    if [ -f "marimo_site/index.html" ]; then
        cp marimo_site/index.html _site/marimo.html
        echo "✓ Copied marimo index to /marimo.html"
    fi
    
    # Copy notebooks folder (root-level notebooks)
    if [ -d "marimo_site/notebooks" ]; then
        mkdir -p _site/notebooks
        cp -r marimo_site/notebooks/* _site/notebooks/
        echo "✓ Copied root notebooks"
    fi
    
    # Copy projects folder (preserves full path structure)
    if [ -d "marimo_site/projects" ]; then
        mkdir -p _site/projects
        cp -r marimo_site/projects/* _site/projects/
        echo "✓ Copied project notebooks"
    fi
    
    # Copy data and results directories for projects (needed for notebook data access)
    # This copies directories from source projects to maintain relative paths
    for project_dir in projects/*/; do
        project_name=$(basename "$project_dir")
        
        if [ -d "${project_dir}data" ] || [ -d "${project_dir}results" ]; then
            mkdir -p "_site/projects/$project_name"
            
            if [ -d "${project_dir}data" ]; then
                cp -r "${project_dir}data" "_site/projects/$project_name/"
                echo "✓ Copied data for $project_name"
            fi
            
            if [ -d "${project_dir}results" ]; then
                cp -r "${project_dir}results" "_site/projects/$project_name/"
                echo "✓ Copied results for $project_name"
            fi
        fi
    done
else
    echo "⚠ Warning: marimo_site not found. Run 'python build_notebooks.py' first"
fi

echo "✅ Done! Notebooks available at /marimo.html, /notebooks/ and /projects/"
