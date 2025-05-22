---
layout: page
title: Projects
permalink: /projects/
description: A showcase of my key research and development projects.
nav: true
nav_order: 3 # Adjust order as needed
display_categories: [research, software, other] # Example categories, customize as needed
horizontal: false # Set to true for a different layout if preferred
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category | slugify }}" href="#{{ category | slugify }}" class="project-category-anchor">
    <h2 class="category">{{ category | capitalize }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category  | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in categorized_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in categorized_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->
{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->
{% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<div style="margin-top: 2em;">
  <p><em>Please note: You will need to create individual Markdown files for each project in the <code>_projects</code> folder. See the example placeholder project file (e.g., <code>_projects/placeholder_project.md</code>) for the required structure and front matter.</em></p>
</div>

