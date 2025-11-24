# Copilot Instructions for Mitchell Valdes-Bobes Academic Website

## Project Overview

This is an academic portfolio website built with **Jekyll** using the [al-folio theme](https://github.com/alshedivat/al-folio), deployed via GitHub Pages. The site showcases research publications, CV, projects, and blog posts for Mitchell Valdes-Bobes, a PhD candidate in Economics.

## Architecture & Core Components

### Publication System (Critical)
- **BibTeX-driven**: Publications are managed in `_bibliography/papers.bib` (NOT manually in markdown)
- **Jekyll-Scholar integration**: The `{% bibliography %}` liquid tag in `_pages/publications.md` auto-generates publication lists
- **JMP (Job Market Paper) feature**: Papers with `jmp = {true}` in BibTeX render using custom layout `_layouts/jmp_bib.liquid` via `_includes/jmp.liquid`
- **Custom citation fetching**: `_plugins/google-scholar-citations.rb` scrapes Google Scholar for citation counts (includes rate limiting with random sleep 1.5-3.5s)
- **Marimo Notebooks**: Custom build system (`_plugins/build_marimo_notebooks.rb`) compiles Python notebooks from `notebooks/` and `projects/**/notebooks/` into HTML, then copies them to `_site/marimo_site/`. Requires `marimo` python package.


### Content Collections
Three Jekyll collections (defined in `_config.yml`):
1. **`_books/`**: Book reviews with custom `book-review.liquid` layout
2. **`_news/`**: News announcements (auto-displayed on homepage)
3. **`_projects/`**: Research projects with responsive grid display
4. **`_books/`**: Book reviews

### Special Layouts
- **Distill**: Scientific blog posts using `<d-article>`, `<d-title>`, etc. (see `_layouts/distill.liquid`).
- **JMP**: Job Market Paper layout (`_layouts/jmp_bib.liquid`).


### Custom Plugins (`_plugins/`)
- `cache-bust.rb`: Adds cache-busting hashes to assets
- `hide-custom-bibtex.rb`: Filters internal BibTeX fields from display
- `external-posts.rb`: Integrates external blog posts from RSS feeds
- All plugins are Ruby-based; test locally before deploying
- **Third-Party Libraries**: Managed in `_config.yml` under `third_party_libraries`. Use `_plugins/download-3rd-party.rb` to cache them if `download: true`.

### Data-Driven Pages
- **CV**: Dual system - uses `_data/cv.yml` as fallback if `assets/json/resume.json` missing
- **Venues/Coauthors**: Lookup tables in `_data/venues.yml` and `_data/coauthors.yml` enhance publication display with colors/links
- **Analytics**: Configured in `_config.yml` (Google, Cronitor, Pirsch, Openpanel).
- **Comments**: Giscus is the recommended system (configured in `_config.yml`).


## Development Workflow

### Local Development Commands
```bash
# Preferred: Docker (handles all dependencies)
docker compose up
# Site available at http://localhost:8080

# Alternative: Native Jekyll (requires Ruby, Bundler)
bundle install
bundle exec jekyll serve
# Site available at http://localhost:4000
```

### Deployment
- **Auto-deploys**: Every push to `main` triggers GitHub Actions → builds site → deploys to `gh-pages` branch
- **Build time**: ~4 minutes for full site build, ~45s for GitHub Pages deployment
- **Base URL config**: For user pages, `baseurl:` must be **empty** (not deleted) in `_config.yml`

### Testing Changes
- Configuration changes (`_config.yml`, plugin modifications) require full rebuild: `Ctrl+C` then restart `bundle exec jekyll serve`
- Content changes (markdown, layouts, includes) auto-reload without restart

## Key Conventions

### BibTeX Entry Structure
When adding publications to `_bibliography/papers.bib`:
```bibtex
@article{key_2025,
  title   = {Paper Title},
  author  = {Mitchell Valdes-Bobes and Co-Author},
  year    = {2025},
  abstract = {Full abstract text for JMP display},
  jmp = {true},              # Flags as Job Market Paper
  pdf = {filename.pdf},      # Place in /assets/pdf/
  slides = {slides.pdf},
  code = {https://github.com/...}
}
```

### Liquid Template Patterns
- Use `{% include jmp.liquid %}` to render JMP section anywhere
- Bibliography filtering: `{% bibliography --query @*[jmp=true]* %}`
- Never hardcode publication lists; always use Jekyll-Scholar

### Theme Customization
- Color theme: Edit `--global-theme-color` in `_sass/_themes.scss`
- CV sections: Add entries to `_data/cv.yml` following existing `type: time_table` or `type: list` structure
- Custom layouts in `_layouts/` can override theme defaults

## File Organization Logic

```
_config.yml                 # Site-wide settings (scholar config, collections, plugins)
_bibliography/papers.bib    # Single source of truth for publications
_data/cv.yml               # Structured CV data (education, experience, references)
_pages/                    # Static pages (about.md, publications.md, etc.)
_layouts/                  # Page templates (bib.liquid, jmp_bib.liquid, cv.liquid)
_includes/                 # Reusable components (jmp.liquid, social.liquid)
_plugins/                  # Ruby extensions (custom tags, data processors)
_sass/                     # SCSS stylesheets (modular by component)
assets/pdf/                # PDF files referenced in BibTeX entries
```

## Common Pitfalls

1. **BibTeX changes not showing**: Clear Jekyll cache with `docker compose down` then restart
2. **Plugin errors on GitHub**: GitHub Pages only supports [approved plugins](https://pages.github.com/versions/); custom plugins like `jekyll-scholar` require Actions-based deployment (already configured)
3. **Citation fetching fails**: Google Scholar scraping in `google-scholar-citations.rb` can be blocked; handle gracefully with error messages
4. **Mixed content warnings**: Ensure all URLs use HTTPS in `_config.yml` and BibTeX entries

## When Modifying Code

- **Adding publications**: ONLY edit `_bibliography/papers.bib`, place PDFs in `assets/pdf/`
- **Changing CV**: Edit `_data/cv.yml`, not markdown files
- **New blog posts**: Add to `_posts/` with `YYYY-MM-DD-title.md` naming
- **Custom layouts**: Follow existing Liquid conventions in `_layouts/`; check `bib.liquid` for reference

## Reference Files for Examples

- Custom bibliography layout: `_layouts/jmp_bib.liquid`
- Publication page structure: `_pages/publications.md`
- CV data schema: `_data/cv.yml` (lines 1-100)
- Plugin patterns: `_plugins/google-scholar-citations.rb`
