---
layout: page
permalink: /projects/datafabric-dermalert/
title: DataFabric-DermAlert
description: Governed, federated integration of health data for fairness-aware dataset construction.
img: assets/img/projects/datafabric-dermalert.jpg
importance: 1
period: 2025 – 2026
affiliation: University of Brasília
role: Researcher and co-author
summary: >-
  Clinical data for dermatology AI are scattered across institutions, coded in different ways, and often cannot be centralized.
  I co-developed DataFabric-DermAlert, an open-source tool that integrates these sources through federated queries and
  semantic mappings, and produces versioned, auditable datasets for subgroup-aware evaluation of AI models.
links:
  - name: Paper (SBES 2026)
    url: https://cbsoft.sbc.org.br/2026/data/papers/sbes/DataFabric-DermAlert%20A%20Tool%20for%20Federated%20Health%20Data%20Integration%20and%20Fairness-Aware%20Dataset%20Construction.pdf
    icon: fa-solid fa-file-pdf
  - name: Code (backend)
    url: https://github.com/DermAlert/datafabric-backend
    icon: fa-brands fa-github
  - name: Code (frontend)
    url: https://github.com/DermAlert/datafabric-frontend
    icon: fa-brands fa-github
  - name: Artifact
    url: https://doi.org/10.6084/m9.figshare.33042992.v3
    icon: fa-solid fa-box-archive
---

<div class="project-meta">
  <span><i class="fa-regular fa-calendar"></i> {{ page.period }}</span>
  <span><i class="fa-solid fa-building-columns"></i> {{ page.affiliation }}</span>
  {% if page.role %}<span><i class="fa-solid fa-user"></i> {{ page.role }}</span>{% endif %}
</div>
{% if page.links %}
<div class="project-links">
  {% for link in page.links %}
    <a class="project-link" href="{{ link.url }}"><i class="{{ link.icon }}"></i> {{ link.name }}</a>
  {% endfor %}
</div>
{% endif %}

**DermAlert** is an application and data platform designed to improve the screening and monitoring of skin cancer in Brazil's public health system. It is intended for health centers and Basic Health Units (UBS), where it supports the capture, storage, and analysis of dermatology images and clinical data, helping professionals identify suspicious lesions early and refer patients to specialists faster.

Clinical data rarely live in one place. The same patient attribute can appear under different column names, codes, and formats across institutions, and governance rules often prevent full centralization. These issues slow down dataset construction and make subgroup-aware evaluations of AI models hard to reproduce.

**DataFabric-DermAlert** is the open-source data-fabric layer of the project. It lets data engineers and clinical researchers:

- register heterogeneous sources and define **federated queries** across them without moving all data to one place;
- manage **semantic equivalences** through data dictionaries, value mappings, and auditable normalization;
- materialize versioned **Bronze** (raw or virtualized) and **Silver** (curated) dataset layers;
- share curated datasets in a controlled way through **Delta Sharing**, with manifests that trace every dataset back to its sources.

{% include figure.liquid path="assets/img/projects/datafabric-dermalert.jpg" class="img-fluid rounded z-depth-1" alt="Architecture of DataFabric-DermAlert" caption="Architecture of DataFabric-DermAlert: distributed sources (left), the data-fabric core with federation, semantic catalog, and versioned dataset layers (center), and downstream consumers (right)." zoomable=true %}

The paper evaluates the tool on controlled federated execution, semantic retrieval and normalization, and the reproducible construction, validation, versioning, and sharing of dermatology metadata derived from the HAM10000, HIBA Skin Lesions, and PAD-UFES-20 datasets.

## Publication

<div class="publications">
  {% bibliography --group_by none --query @*[key=hannan2026datafabric]* %}
</div>
