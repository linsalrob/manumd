# ManuMD agent guide

## Project shape

- This is an early, local-first Markdown editor prototype.
- The runnable app is the single static file `dist/index.html`; open it directly in a modern browser to work on it.
- Keep the prototype dependency-free unless a change clearly needs a build system. If the project structure changes, update `README.md` with the new run instructions.
- `README.md` describes the current implemented behavior and limitations. Keep it accurate when changing features.
- The user documentation in `docs/` (Sphinx with MyST Markdown, published by Read the Docs) also describes behavior in detail. Update the affected pages when changing features, and check that `python -m sphinx -W -b html docs docs/_build/html` still builds without warnings.

## Product requirements

- Preserve the research-writing workflow: edit Markdown, see a live preview, insert citations from a Paperpile-exported BibTeX file, and open/download Markdown files.
- Keep manuscript drafts and bibliography local to the browser by default.
- GitHub integration must continue to use a token entered by the user and sent directly from the browser to GitHub. By product decision (issue #7) the token may be kept in the tab's `sessionStorage` so it survives a reload and is cleared when the tab closes. Never write it to `localStorage`, IndexedDB or any other persistent store, and never add telemetry or a server-side manuscript store without an explicit product decision.
- Be clear in the interface and README about limitations, especially around image asset commits and Grammarly browser-extension compatibility.
- Keep the ManuMD palette consistent with GenBankViz: navy `#173e51`, ink `#172433`, pale blue-grey `#edf2f6`, cyan `#03a9f4`, mint `#8ed7c4`, and gold `#ffbf47`.

## Implementation guidance

- Keep user-authored Markdown and BibTeX treated as untrusted input. Escape text inserted into HTML and avoid introducing unsafe HTML rendering.
- Preserve keyboard access, visible focus styles, and a usable narrow-screen layout when editing the interface.
- Keep source changes readable even though the current prototype is compact and self-contained. Avoid minifying new code.
- Do not add generated bundles, deployment archives, credentials, tokens, or manuscript data to commits. Commit source files and documentation only.

## Verification

- For changes to `dist/index.html`, check JavaScript syntax and open the app in a browser when available.
- Manually check the affected workflow: Markdown preview, BibTeX citation insertion, image preview, file open/download, or GitHub load/save as applicable.
- Report checks that could not be run and any remaining prototype limitations in the handoff.
