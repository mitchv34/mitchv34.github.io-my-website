---
layout: page
permalink: /publications/
title: Research
description: 
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2>Working Papers</h2>

{% bibliography --query @*[status=working]* %}

<h2>Work in Progress</h2>

{% bibliography --query @*[status=wip]* %}

</div>
