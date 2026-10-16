# ManuMD

ManuMD is a local-first Markdown writing prototype for research manuscripts.

## Current prototype

- Edit Markdown with a live preview and inline image display.
- Load a BibTeX file exported or synced from Paperpile, search it, and insert Pandoc-style citations.
- Open and download Markdown files.
- Load a Markdown file from GitHub and save changes as a commit using a fine-grained token entered for that browser tab.
- Keep draft text and the bibliography in browser local storage.

The sample manuscript and sample figure are illustrative. They are included to make the editor usable on first launch.

## Privacy and limitations

The editor has no server-side manuscript storage. Drafts and bibliography are saved in the current browser's local storage. GitHub operations send the selected file and token directly from the browser to GitHub. The token is held in memory for the current tab and is not saved by ManuMD. A browser Grammarly extension may work in the Markdown text area, depending on the browser and extension.

This is an early prototype. It currently loads and saves one Markdown file at a time; images can be previewed in the current session, but image assets are not automatically committed to GitHub.

## Run locally

Open `dist/index.html` in a modern browser. The GitHub API requires a network connection; local editing and preview work without one.
