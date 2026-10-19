# ManuMD

ManuMD is a Markdown editor for research manuscripts. It runs entirely in your web browser: there is nothing to install, and your text never passes through a ManuMD server.

**Open it at <https://linsalrob.github.io/manumd/>.**

You write the paper in plain Markdown, beside a live preview that shows the figures, typeset equations, formatted citations and a reference list. Citations come from a BibTeX file, such as one exported from Paperpile. When you're ready, ManuMD saves the file back to GitHub as a commit, so co-authors can review every change.

ManuMD is an early prototype. It edits one Markdown file at a time, and some things, such as committing images, are deliberately left to GitHub. See [Limitations](limitations.md).

## Where to start

- **New to ManuMD?** Start with [Getting started](getting-started.md).
- **Asked to edit a paper on GitHub?** [Editing a paper with co-authors](collaborating.md) takes you from a new GitHub account to a pull request, with no installation.
- **Setting up a paper for ManuMD?** See [Working with GitHub](github.md), [Citations](citations.md) and [Images and figures](images.md).
- **Something went wrong?** See [Troubleshooting](troubleshooting.md).

## What it does

- **Edit and preview:** Markdown beside a live preview, in split, edit-only or preview-only view. In the preview you can double-click a paragraph to edit it in place.
- **Citations:** search a BibTeX library and insert Pandoc citations such as `[@Smith2024]`. The preview formats them and builds the reference list.
- **Equations:** LaTeX math, typeset with KaTeX.
- **GitHub:** load a Markdown file from a repository, with its figures and bibliography, and save your changes back as a commit.
- **Private by default:** drafts stay in your browser. A GitHub token goes only from your browser to GitHub. See [Your data and privacy](privacy.md).

```{toctree}
:maxdepth: 2
:caption: Using ManuMD

getting-started
workspace
editing
markdown
citations
images
github
```

```{toctree}
:maxdepth: 2
:caption: Guides

collaborating
```

```{toctree}
:maxdepth: 2
:caption: Reference

privacy
troubleshooting
limitations
development
```
