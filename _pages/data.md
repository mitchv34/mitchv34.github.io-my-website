---
layout: page
permalink: /data/
title: Data & Code
description: Interactive datasets, replication materials, and code repositories for my research
nav: true
nav_order: 4
---

<div class="data-section">
  <p class="lead">
    This page provides access to datasets, interactive tools, and replication code from my research. 
    All datasets include documentation, and many feature interactive notebooks that run entirely in your browser.
  </p>

  <div class="datasets mt-4">
    {% for dataset in site.data.datasets %}
      {% include dataset_card.liquid dataset=dataset %}
    {% endfor %}
  </div>

  <div class="mt-5">
    <h3>Data Use & Citation</h3>
    <p>
      All datasets are provided for research and educational purposes. If you use any of these datasets 
      in your work, please cite the corresponding paper. For questions or data requests, please 
      <a href="/contact/">contact me</a>.
    </p>
  </div>
</div>
