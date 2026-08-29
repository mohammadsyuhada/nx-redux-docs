# NX Redux Docs

User documentation website for [NX Redux](https://github.com/mohammadsyuhada/nx-redux),
custom firmware for TrimUI retro handheld devices.

Built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
Screenshots are captured from a real device (TrimUI Brick, 1024×768).

## Local development

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Then open http://127.0.0.1:8000.

## Deployment

Pushing to `main` triggers the GitHub Actions workflow in
`.github/workflows/deploy.yml`, which builds the site and publishes it to
GitHub Pages at https://mohammadsyuhada.github.io/nx-redux-docs/.
