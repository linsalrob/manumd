# ManuMD

ManuMD is a local-first Markdown writing prototype for research manuscripts.

## Current prototype

- Edit Markdown with a live preview (split, edit-only or preview-only view) and inline image display.
- Load a BibTeX file exported or synced from Paperpile, search it, and insert Pandoc-style citations. The preview formats citations and builds a reference list in order of first citation, and the status bar flags citation keys that are not in the loaded bibliography.
- Open and download Markdown files.
- Load a Markdown file from GitHub and save changes as a commit using a fine-grained token entered for that browser tab.
- Keep draft text, the document name and the bibliography in browser local storage.

The sample manuscript and sample figure are illustrative. They are included to make the editor usable on first launch.

### Citations

Citations use Pandoc syntax, so the same Markdown can be converted with Pandoc and `--citeproc`:

- `[@Smith2024]` — a single citation
- `[@Smith2024; @Lee2023]` — several works; picking a second citation from the picker straight after a citation adds it to the same group
- `[see @Smith2024, p. 4]` — prefix and locator
- `[-@Smith2024]` — year only, for use after the author's name in the text

The preview uses a simple author–year style. It does not apply journal citation styles (CSL); use Pandoc for final formatting. BibTeX parsing handles Paperpile's quoted values, nested braces, common LaTeX accents and escapes, multi-line fields and corporate (braced) authors. Duplicate keys are reported and the first entry is used.

### Markdown preview

The preview supports a common subset of Markdown: headings, paragraphs, bold, italic, strikethrough, inline code, fenced code blocks, links, images, bulleted and numbered lists (not nested), block quotes, tables with a header row, horizontal rules, and YAML front matter (shown as text). Raw HTML in the Markdown is displayed as text, not rendered.

## Privacy and limitations

The editor has no server-side manuscript storage. Drafts and bibliography are saved in the current browser's local storage. If browser storage is unavailable or full (for example, with a very large bibliography), the status bar says so and the content is kept only until the tab closes. GitHub operations send the selected file and token directly from the browser to GitHub. The token is held in memory for the current tab, so you do not have to re-enter it for each load or save; it is not saved by ManuMD, and "Forget token" clears it. A browser Grammarly extension may work in the Markdown text area, depending on the browser and extension.

When you save to GitHub, ManuMD commits against the version you loaded. If the file has changed on GitHub since then, the commit is refused rather than overwriting the newer version; download your draft, load the file again and reapply your edits. Saving to a path you did not load asks before replacing an existing file.

This is an early prototype. It loads and saves one Markdown file at a time. Images can be previewed in the current session only: they are not kept in browser storage and are not committed to GitHub. Images referenced by relative paths show a placeholder until you add the image file. Opening a file, loading from GitHub or starting a new file replaces the local draft, after confirmation.

## Run locally

Open `dist/index.html` in a modern browser. The GitHub API requires a network connection; local editing and preview work without one.
