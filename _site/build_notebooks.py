#!/usr/bin/env python3
"""
Simple build script for marimo notebooks.
Exports marimo notebooks to HTML/WebAssembly and generates an index page.
"""

import subprocess
from pathlib import Path
from typing import List
import jinja2
import shutil


def export_notebook(notebook_path: Path, output_dir: Path, as_app: bool = False) -> bool:
    """Export a marimo notebook to HTML/WebAssembly."""
    print(f"Exporting {notebook_path}...")
    
    output_file = output_dir / notebook_path.with_suffix(".html")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = ["marimo", "export", "html-wasm"]
    
    if as_app:
        cmd.extend(["--mode", "run", "--no-show-code"])
    else:
        cmd.extend(["--mode", "edit"])
    
    cmd.extend([str(notebook_path), "-o", str(output_file)])
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ Exported {notebook_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to export {notebook_path}: {e.stderr}")
        return False


def export_folder(folder: Path, output_dir: Path, as_app: bool = False) -> List[dict]:
    """Export all notebooks in a folder."""
    if not folder.exists():
        return []
    
    notebooks = list(folder.rglob("*.py"))
    if not notebooks:
        return []
    
    print(f"\nExporting {len(notebooks)} files from {folder}/")
    
    notebook_data = []
    for nb in notebooks:
        if export_notebook(nb, output_dir, as_app=as_app):
            notebook_data.append({
                "display_name": nb.stem.replace("_", " ").title(),
                "html_path": str(nb.with_suffix(".html"))
            })
    
    return notebook_data


def generate_index(output_dir: Path, template_file: Path, notebooks_data: List[dict], apps_data: List[dict]):
    """Generate index.html from template."""
    print(f"\nGenerating index.html...")
    
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_file.parent),
        autoescape=jinja2.select_autoescape(["html", "xml"])
    )
    template = env.get_template(template_file.name)
    
    html = template.render(notebooks=notebooks_data, apps=apps_data)
    
    index_path = output_dir / "index.html"
    with open(index_path, "w") as f:
        f.write(html)
    
    print(f"✓ Generated {index_path}")


def copy_project_data(project_dir: Path, output_dir: Path):
    """Copy data and results directories for a project to output."""
    project_name = project_dir.name
    project_output = output_dir / "projects" / project_name
    
    # Copy results directory if it exists
    results_dir = project_dir / "results"
    if results_dir.exists():
        dest_results = project_output / "results"
        print(f"Copying {results_dir} to {dest_results}")
        shutil.copytree(results_dir, dest_results, dirs_exist_ok=True)
    
    # Copy data directory if it exists
    data_dir = project_dir / "data"
    if data_dir.exists():
        dest_data = project_output / "data"
        print(f"Copying {data_dir} to {dest_data}")
        shutil.copytree(data_dir, dest_data, dirs_exist_ok=True)


def main():
    """Main build function."""
    print("=" * 60)
    print("Building marimo notebooks")
    print("=" * 60)
    
    output_dir = Path("marimo_site")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Export notebooks and apps from root
    notebooks_data = export_folder(Path("notebooks"), output_dir, as_app=False)
    apps_data = export_folder(Path("apps"), output_dir, as_app=True)
    
    # Export from projects/*/notebooks/ (submodule notebooks)
    print("\nScanning for project notebooks...")
    projects_dir = Path("projects")
    if projects_dir.exists():
        for project_dir in projects_dir.glob("*/"):
            if (project_dir / "notebooks").exists():
                print(f"Found notebooks in {project_dir.name}")
                # Export as apps (run mode, no code visible)
                project_notebooks = export_folder(project_dir / "notebooks", output_dir, as_app=True)
                notebooks_data.extend(project_notebooks)
                # Copy data and results directories
                copy_project_data(project_dir, output_dir)
    
    # Generate index
    template_file = Path("templates/index.html.j2")
    if template_file.exists():
        generate_index(output_dir, template_file, notebooks_data, apps_data)
    else:
        print(f"Warning: Template not found at {template_file}")
    
    print("\n" + "=" * 60)
    print(f"Build complete! Output in {output_dir}/")
    print(f"  Notebooks: {len(notebooks_data)}")
    print(f"  Apps: {len(apps_data)}")
    print("=" * 60)
    print("\nTo test locally, run:")
    print(f"  python -m http.server -d {output_dir}")


if __name__ == "__main__":
    main()
