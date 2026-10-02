---
layout: page
permalink: /projects/legal-nlp/
title: "Justiça 4.0: Grouping Similar Court Cases"
description: Unsupervised learning to group similar cases and support intelligent triage in the Brazilian Judiciary.
importance: 2
period: 2022 – 2023
affiliation: AI.lab, University of Brasília · Justiça 4.0 (CNJ/UNDP)
role: Machine learning researcher
summary: >-
  As part of Justiça 4.0, a program of Brazil's National Council of Justice (CNJ) and the United Nations Development
  Programme (UNDP), I worked on grouping similar court cases to support intelligent triage. I compared clustering methods
  (K-means, Gaussian mixtures, spectral clustering, self-organizing maps, and DBSCAN) and built reproducible text-processing
  pipelines with DVC and MLflow.
links:
  - name: Justiça 4.0 program (CNJ)
    url: https://www.cnj.jus.br/tecnologia-da-informacao-e-comunicacao/justica-4-0/
    icon: fa-solid fa-scale-balanced
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

**Justiça 4.0** (officially _Justiça 4.0: Inovação e Efetividade na Realização da Justiça para Todos_, BRA/20/015) is an international technical cooperation project between Brazil's National Council of Justice (CNJ) and the United Nations Development Programme (UNDP), launched in December 2020 to accelerate the digital transformation of the Brazilian Judiciary.

The University of Brasília took part in the program through AI.lab, under the coordination of Dr. Nilton Correia da Silva and Dr. Fabrício Ataídes Braz. I worked on its artificial intelligence track, whose goals were to **automate repetitive routines**, **group similar cases**, and support **intelligent triage** of court cases.

My work focused on grouping similar cases. I implemented and compared five clustering algorithms to discover topics in legal cases: K-means, Gaussian mixture models, spectral clustering, Kohonen self-organizing maps, and DBSCAN. I built and refined text-preprocessing pipelines versioned with **DVC**, tracked parameters, metrics, and artifacts with **MLflow** to compare results systematically, and used multiprocessing to handle large document collections.

I worked closely with legal experts to validate the resulting groups, which improved model quality and supported the modernization of the Judiciary.
