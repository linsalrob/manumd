# Limitations

ManuMD is an early prototype. These are the main things it doesn't do, or does differently from what you might expect.

## Files

- **One file at a time.** ManuMD edits one Markdown file. A paper split across several files is edited one file at a time.
- **No version history in ManuMD.** The draft in your browser has no undo history beyond the text area's own. Commit to GitHub, or download the file, to keep versions.
- **One browser.** The draft lives in one browser on one computer. It doesn't follow you to another device unless you save it to GitHub or download it.

## GitHub

- **Only the Markdown file is committed.** ManuMD never commits images or the bibliography. Add or change those on GitHub directly.
- **No pull requests from ManuMD.** Open them on GitHub. See [Editing a paper with co-authors](collaborating.md).
- **No merging.** If the file changed on GitHub since you loaded it, ManuMD refuses to save. Download your draft, load the new version and redo your edits.
- **Images folder: top level only.** Images in subfolders of the images folder are not downloaded, and images over 25 MB are skipped.
- **Token per tab.** The token is cleared when you close the tab. Paste it again in a new tab.

## Preview

- **A subset of Markdown.** Nested lists, footnotes, definition lists, task lists, bracketed spans and raw HTML are not formatted. They stay in the file unchanged, and Pandoc formats them as usual. See [Markdown and equations](markdown.md).
- **Cross-references: the common cases.** The preview numbers figures, tables, equations and sections, and formats references to them, with pandoc-crossref's default style and a few of its settings. It doesn't do subfigures, chapter-based numbering, `cref` style, lists of figures or tables, or code-listing labels. See [Cross-references](markdown.md#cross-references).
- **In-text citations.** Only bracketed citations, such as `[@Smith2024]`, are formatted. An in-text citation such as `@Smith2024` is shown as text. (`@fig:1` and the other cross-references are formatted.)
- **Simple citation style.** The preview uses a fixed author–year style. Journal styles (CSL) are applied by Pandoc.
- **KaTeX, not LaTeX.** Most LaTeX math works, but not every package. Equations need an internet connection the first time.
- **Front matter as text.** The YAML front matter is shown as text. ManuMD reads only its `bibliography:` field.

## Other

- **Grammar checkers.** ManuMD has no grammar checker. A browser extension such as Grammarly may work in the Markdown text area, depending on the browser and the extension.
- **Bibliography from a local file.** A Markdown file opened from your computer can't load the `.bib` file next to it. Use **Import .bib**.
- **Large bibliographies.** Browser storage is limited, typically to about 5 MB per site. A very large bibliography may not fit; ManuMD says so, and you'll need to import it again in the next session.
