---
layout: page
title: research
permalink: /research/
description: Current interests and previous research projects.
nav: true
nav_order: 2
---

## Current research

<div class="research-current">
  <p>
    I am currently exploring research directions with <a href="https://hridesh.github.io/">Dr. Hridesh Rajan</a> in the
    <a href="https://lab-design.github.io/">Laboratory for Software Design</a> at Tulane. The lab applies programming-language and
    software-engineering principles to make software and AI more dependable, with recent work on fault localization in deep
    learning, fairness in machine learning, and runtime verification of AI agents.
  </p>
  <p>
    I am especially interested in how these questions connect to my previous work on data infrastructure for health AI and on
    natural language processing.
  </p>
</div>

## Previous research

<div class="research-timeline">
  {% assign sorted_projects = site.projects | sort: "importance" %}
  {% for project in sorted_projects %}
    <div class="research-entry">
      <div class="research-period">{{ project.period }}</div>
      <div class="research-content">
        <div class="research-text">
          <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
          <p class="research-affiliation">{{ project.affiliation }}{% if project.role %} · {{ project.role }}{% endif %}</p>
          <p>{{ project.summary }}</p>
          <div class="research-links">
            {% for link in project.links %}
              {% if forloop.index <= 2 %}
                <a class="project-link" href="{{ link.url }}"><i class="{{ link.icon }}"></i> {{ link.name }}</a>
              {% endif %}
            {% endfor %}
          </div>
        </div>
        {% if project.img %}
          <a class="research-thumb" href="{{ project.url | relative_url }}" aria-label="{{ project.title }}">
            <img src="{{ project.img | relative_url }}" alt="{{ project.title }}" loading="lazy">
          </a>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
