# Data & Code Section Setup

## ✅ Created Files

### 1. **_data/datasets.yml**
Main dataset registry (like papers.bib for datasets)
- Contains metadata for teleworkability-index
- Easy to add new datasets in the future
- Includes downloads, interactive tools, documentation links

### 2. **_pages/data.md**
Landing page for the Data & Code section
- Accessible at `/data/`
- Loops through datasets and displays cards
- Includes data use & citation info

### 3. **_includes/dataset_card.liquid**
Reusable component for displaying datasets
- Preview image
- Authors, year, description
- Download buttons (CSV, metrics, feature importance)
- Interactive tool links (explore, retrain, analyze)
- Documentation links
- Tags and related paper link

### 4. **_sass/custom.scss**
Custom styling for dataset cards
- Publication-style layout
- Responsive design
- Button groups and badges
- Hover effects

### 5. **assets/img/data_preview/teleworkability_preview.png**
Visual preview showing:
- Distribution histogram (labeled vs predicted)
- Summary statistics
- Top 5 most teleworkable occupations
- Bottom 5 least teleworkable occupations

## 📊 Current Dataset

**Teleworkability Index (ψ)**
- 4 download options (full dataset, metrics, feature importance)
- 3 interactive tools (explore, retrain, analyze)
- 2 documentation links (GitHub, setup guide)
- Links to related JMP paper
- 5 tags for categorization

## 🎯 Next Steps

1. **Add to navigation** (optional - already has nav: true)
2. **Test the page** at http://localhost:4002/data/
3. **Add more datasets** by editing `_data/datasets.yml`
4. **Create preview images** for new datasets using similar matplotlib code

## 📝 Adding New Datasets

Edit `_data/datasets.yml`:

```yaml
- id: new-dataset-id
  title: "Dataset Title"
  authors:
    - Author Name
  year: 2025
  description: >
    Multi-line description here...
  preview: new_dataset_preview.png  # Optional
  downloads:
    - label: "CSV File"
      url: "/path/to/file.csv"
      size: "10 KB"
  interactive:
    - label: "🔍 Explore"
      url: "/notebooks/explore.html"
      description: "Interactive exploration"
  documentation:
    - label: "README"
      url: "https://github.com/..."
  paper: bibtex_key  # Optional
  tags: ["tag1", "tag2"]
  featured: true  # Optional
```

## 🎨 Preview Image Template

See `assets/img/data_preview/` for example.
Create 10x8 inch figure with:
- Distribution plots
- Summary statistics
- Key highlights
- Save as PNG at 150 DPI

## 🔗 URLs

- Main page: `/data/`
- Direct downloads: `/projects/teleworkability-index/results/*.csv`
- Interactive tools: `/notebooks/projects/teleworkability-index/notebooks/*.html`

