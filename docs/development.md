# For developers

ManuMD's source is at <https://github.com/linsalrob/manumd>. Bug reports and suggestions are welcome as [issues](https://github.com/linsalrob/manumd/issues).

## Project layout

```text
dist/index.html          the whole app: HTML, CSS and JavaScript in one file
docs/                    this documentation (Sphinx with MyST Markdown)
.readthedocs.yaml        the Read the Docs build configuration
.github/workflows/       GitHub Pages deployment of dist/
AGENTS.md                guidance for AI coding agents working on ManuMD
README.md                a summary of features and limitations
```

The app is deliberately a single static file with no build step and no runtime dependencies. The one external component is KaTeX, loaded from a CDN with Subresource Integrity when a draft contains math.

## Run it locally

Open `dist/index.html` in a modern browser. Local editing and the preview work offline. GitHub needs a network connection.

Some browsers restrict storage for pages opened from `file://` addresses. To test as a web page, serve the folder:

```bash
python3 -m http.server --directory dist 8000
```

then open <http://localhost:8000/>.

## Principles

These come from `AGENTS.md`, and apply to any change:

- **Local first.** Drafts and bibliographies stay in the browser. No telemetry and no server-side manuscript store without an explicit product decision.
- **Tokens.** The GitHub token is entered by the user and sent only from the browser to GitHub. It may be kept in the tab's `sessionStorage` (issue #7), and never in `localStorage`, IndexedDB or any other lasting store.
- **Untrusted input.** Markdown and BibTeX are untrusted. Escape everything inserted into HTML, and don't render raw HTML.
- **Dependency-free.** Keep the app a single static file unless a change clearly needs a build system.
- **Readable source.** Don't minify.
- **Accessible.** Keep keyboard access, visible focus styles and a usable narrow-screen layout.
- **Palette.** Navy `#173e51`, ink `#172433`, pale blue-grey `#edf2f6`, cyan `#03a9f4`, mint `#8ed7c4` and gold `#ffbf47`.
- **Documentation.** Keep `README.md` and these docs accurate when behaviour changes.

## Checking a change

- Check the JavaScript syntax. The Pages workflow does this before every deployment:

  ```bash
  node -e '
    const html = require("fs").readFileSync("dist/index.html", "utf8");
    const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
    scripts.forEach(s => new Function(s));
    console.log("syntax OK");
  '
  ```

- Open the app in a browser and try the workflows the change affects: the preview, citation insertion, images, opening and downloading files, and GitHub load and save.

## Deployment

### The app

Every push to `main` that changes `dist/` runs `.github/workflows/pages.yml`, which checks the JavaScript syntax and publishes `dist/` to GitHub Pages at <https://linsalrob.github.io/manumd/>.

### This documentation

The documentation is built by [Read the Docs](https://about.readthedocs.com/) from `docs/`, using `.readthedocs.yaml`. Read the Docs rebuilds it on every push to `main`. Warnings fail the build, so broken links between pages are caught.

To build it locally:

```bash
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
.venv/bin/python -m sphinx -W -b html docs docs/_build/html
```

then open `docs/_build/html/index.html`. The `docs/_build/` folder is ignored by Git.

The pages are Markdown, using [MyST](https://myst-parser.readthedocs.io/) for notes (`:::{note}`) and keyboard keys (`` {kbd}`Ctrl+S` ``). Add a new page to a `toctree` in `docs/index.md`.
