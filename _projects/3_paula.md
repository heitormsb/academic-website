---
layout: page
permalink: /projects/paula/
title: "PAULA: Handwriting Recognition for Literacy"
description: An offline mobile app that helps semi-literate and illiterate residents of Paranoá, Brazil, learn to read and write.
importance: 3
period: 2023
affiliation: University of Brasília · Extension project in Paranoá
summary: >-
  PAULA (Paranoá Alfabetizando Usando Letramento Analógico) is a University of Brasília extension project: an offline
  mobile app, based on Paulo Freire's method, that helps semi-literate and illiterate residents of Paranoá learn to read and
  write. I led the AI team that added handwriting recognition, so that learners can write letters with their fingers on the
  screen and receive immediate feedback.
links:
  - name: App code
    url: https://github.com/Paula-Project/Paula-app
    icon: fa-brands fa-github
  - name: API code
    url: https://github.com/heitormsb/paulaIA-api
    icon: fa-brands fa-github
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

**PAULA** (_Paranoá Alfabetizando Usando Letramento Analógico_) is an extension project of the University of Brasília (UnB), developed within UnB's extension network (REPE) in Paranoá, an administrative region of the Federal District. According to the 2015 District Household Sample Survey (PDAD), 43.9% of Paranoá's residents had not completed elementary school and about 4% were illiterate, while most residents owned a mobile phone.

The app turns that phone into a private tutor. It works offline (the Internet is needed only to install it), so learners can practice on their own, as often as they like, wherever they are, and without embarrassment. Following **Paulo Freire's method**, lessons start from the learners' own world: the vowels and everyday words, such as _PARANOÁ_, _LAGO_, _IGREJA_, and _PADARIA_, were chosen from words mentioned by students at CEF 01 do Paranoá, a local public school, and from photos of places in the city.

The first version, released in 2022, taught reading. In 2023, I led the AI team responsible for the next step: **writing**. In the new version, learners trace uppercase letters and words with their fingers on the screen, guided by screens that show the direction of each stroke, and the app reads and corrects what they wrote right away.

To make this possible, we researched neural networks that recognize handwriting with high accuracy, combining **convolutional architectures**, **transformer-based models**, and stroke-analysis techniques. I also designed the backend APIs that serve the models and process data efficiently and securely.
