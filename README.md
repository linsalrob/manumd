# ManuMD

ManuMD is a local-first Markdown writing prototype for research manuscripts.

## Current prototype

- Edit Markdown with a live preview (split, edit-only or preview-only view) and inline image display.
- In split view, double-click either pane to bring the other into line at the same place, or turn on **⇅ Sync scroll** to keep them scrolled together.
- Load a BibTeX file exported or synced from Paperpile, search it, and insert Pandoc-style citations. Import the `.bib` file with **Import .bib**, or keep it in the manuscript's GitHub repository and it is loaded with the Markdown. The preview formats citations and builds a reference list in order of first citation, and the status bar flags citation keys that are not in the loaded bibliography.
- Open and download Markdown files.
- Load a Markdown file from GitHub and save changes as a commit using a fine-grained token entered for that browser tab. The repository, branch and file are remembered with the draft, so the GitHub dialog is filled in after a reload.
- Download the images in the paper's images folder on GitHub (by default `images/`, next to the Markdown file) when the file is loaded, and cache them in the browser so later loads only download images that have changed.
- Keep draft text, the document name and the bibliography in browser local storage.

The sample manuscript and sample figure are illustrative. They are included to make the editor usable on first launch.

### Citations

Citations use Pandoc syntax, so the same Markdown can be converted with Pandoc and `--citeproc`:

- `[@Smith2024]` — a single citation
- `[@Smith2024; @Lee2023]` — several works; picking a second citation from the picker straight after a citation adds it to the same group
- `[see @Smith2024, p. 4]` — prefix and locator
- `[-@Smith2024]` — year only, for use after the author's name in the text

When a Markdown file is loaded from GitHub, ManuMD also loads its bibliography from the same repository and branch. It uses the file named by the `bibliography:` field in the Markdown's YAML front matter (the field Pandoc reads; for a list, the first file), or else the **BibTeX file** set in the GitHub dialog, `references.bib` next to the Markdown file by default. Paths are relative to the Markdown file. The loaded bibliography replaces the imported one, unless you import a `.bib` file while it loads; leave the BibTeX file empty, with no `bibliography:` field, to keep the imported one. ManuMD never commits the bibliography. A Markdown file opened from your computer cannot read files next to it, so import its `.bib` file.

The preview uses a simple author–year style. It does not apply journal citation styles (CSL); use Pandoc for final formatting. BibTeX parsing handles Paperpile's quoted values, nested braces, common LaTeX accents and escapes, multi-line fields and corporate (braced) authors. Duplicate keys are reported and the first entry is used.

### Markdown preview

The preview supports a common subset of Markdown: headings, paragraphs, bold, italic, strikethrough, inline code, fenced code blocks, links (web links open in a new tab, `#heading` links scroll the preview, and relative links open the file on GitHub when the draft was loaded from there), images, bulleted and numbered lists (not nested), block quotes, tables with a header row, horizontal rules, and YAML front matter (shown as text). HTML comments (`<!-- ... -->`) are hidden from the preview and the word count, except inside code. Other raw HTML in the Markdown is displayed as text, not rendered.

### Equations

LaTeX math uses Pandoc syntax: `$...$` for inline math and `$$...$$` for display math (on one line or spread over several). A dollar sign followed by a space or followed by a digit after the closing `$` is not treated as math, so prices such as "$100 and $1" are left alone; write `\$` for a literal dollar sign. Equations are typeset with [KaTeX](https://katex.org/), which supports most LaTeX math but not every package.

KaTeX is the one external component. When a draft contains math, ManuMD fetches KaTeX 0.19.0 from the jsDelivr CDN, pinned to that version and checked with Subresource Integrity. Only the KaTeX files are requested: manuscript text is never sent. Offline, or if the CDN is unreachable, equations are shown as TeX source.

## Privacy and limitations

The editor has no server-side manuscript storage. Drafts and bibliography are saved in the current browser's local storage. If browser storage is unavailable or full (for example, with a very large bibliography), the status bar says so and the content is kept only until the tab closes. GitHub operations send the selected file and token directly from the browser to GitHub. The token is kept in the tab's session storage, so you do not have to re-enter it for each load or save, or after reloading the page. The browser clears it when the tab is closed; it is never written to local storage, and "Forget token" clears it at once. Session storage belongs to the site's origin, so other pages on the same origin opened in that tab (for example, other GitHub Pages projects under the same account) could read the token. Use Forget token on a shared computer, and use a fine-grained token limited to the manuscript repository. If GitHub refuses a request, the GitHub dialog explains the likely cause, such as a token whose Repository access does not include the manuscript repository or which lacks Contents access. A browser Grammarly extension may work in the Markdown text area, depending on the browser and extension.

When you save to GitHub, ManuMD commits against the version you loaded. If the file has changed on GitHub since then, the commit is refused rather than overwriting the newer version; download your draft, load the file again and reapply your edits. Saving to a path you did not load asks before replacing an existing file.

This is an early prototype. It loads and saves one Markdown file at a time. ManuMD never commits images to GitHub. When a file is loaded from GitHub, the image files directly inside its images folder (set in the GitHub dialog, relative to the Markdown file; subfolders are not read) are downloaded and cached in the browser's IndexedDB. Each image is identified by its Git blob SHA, so a later load only downloads images that have changed, and cached images are shown after a reload, even offline. The cache keeps the images of the three most recently loaded versions of each folder, and a reloaded draft shows the images of the version it was loaded with. Images over 25 MB are skipped. If the folder cannot be refreshed (for example, offline or when GitHub is unavailable), the last cached copy is shown. Images added with "Add image files" are previewed for the current session only. Images referenced by relative paths show a placeholder until they are loaded. Opening a file, loading from GitHub or starting a new file replaces the local draft, after confirmation.

## Run locally

Open `dist/index.html` in a modern browser. The GitHub API requires a network connection; local editing and preview work without one.

## Hosted version

Each push to `main` that changes `dist/` publishes the app to GitHub Pages at <https://linsalrob.github.io/manumd/> via `.github/workflows/pages.yml`. The hosted page is the same static file: drafts, bibliography and tokens stay in your browser exactly as they do locally.
