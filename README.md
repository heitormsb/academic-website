# Academic Website of Heitor Marques S. Barbosa

Source of my academic website, **https://heitormsb.github.io**. I am a Ph.D. student in Computer Science at Tulane University.

The site is built with [Jekyll](https://jekyllrb.com/) on the [al-folio](https://github.com/alshedivat/al-folio) v1 starter and deployed to
GitHub Pages by the `Deploy site` workflow on every push to `main`.

## Where things live

| What                       | File(s)                                                                 |
| -------------------------- | ----------------------------------------------------------------------- |
| Landing page (bio, photo)  | `_pages/about.md`, `assets/img/prof_pic.jpg`                            |
| Research page and projects | `_pages/research.md`, `_projects/*.md`                                  |
| Publications               | `_bibliography/papers.bib` (add `selected = {true}` to feature a paper) |
| News                       | `_news/*.md`                                                            |
| CV (web and PDF)           | `_data/cv.yml`, `assets/rendercv/*.yaml`                                |
| Social links               | `_data/socials.yml`                                                     |
| Site settings              | `_config.yml`                                                           |
| Colors and custom styles   | `assets/css/main.scss` (local override of the `al_folio_core` file)     |
| Footer                     | `_includes/footer.liquid` (local override of the `al_folio_core` file)  |

## Run locally

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/
```

## Regenerate the PDF CV

The PDF at `assets/pdf/Heitor_Barbosa_CV.pdf` is rendered from `_data/cv.yml` with [RenderCV](https://docs.rendercv.com). The
`Render a CV` workflow does this automatically when `_data/cv.yml` changes; to do it locally:

```bash
python3 -m pip install -r requirements.txt
python3 bin/render_cv.py
```

## Template documentation

The al-folio guides are kept in [`docs/`](docs/README.md). See [`docs/CUSTOMIZE.md`](docs/CUSTOMIZE.md) for configuration options.
The site's code is under the [MIT License](LICENSE) inherited from al-folio.
