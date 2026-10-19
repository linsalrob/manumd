# The workspace

ManuMD's screen has a top bar, a left-hand panel, the editor in the middle, a right-hand panel and a status bar.

## Top bar

| Control | What it does |
|---|---|
| **Local draft** / repository name | Where the current draft came from. |
| **↗ GitHub** | Opens the GitHub dialog, to load a file from a repository or save a commit. See [Working with GitHub](github.md). |
| **Open .md** | Opens a Markdown file from your computer, replacing the draft. |
| **Save draft** | Downloads the Markdown file to your computer ({kbd}`Ctrl+S` or {kbd}`⌘+S`). It does not save to GitHub. |

## Left-hand panel

- **Draft files:** the current Markdown file, the bibliography and any images. **＋** starts a new, empty Markdown file.
- **Quick actions:**
  - **＋ Citation** opens the citation picker.
  - **Import .bib** loads a BibTeX file.
  - **＋ Image** adds image files from your computer to the preview.
  - **⇩ Download** downloads the Markdown file, like **Save draft**.

## Editor

Above the text are:

- **Split**, **Edit** and **Preview:** choose the view. See [Views](editing.md#views).
- **Formatting buttons:** bold, italic, heading, quote, code and link. See [Formatting](editing.md#formatting).
- **⇅ Sync scroll:** keeps the two panes scrolled together in Split view.
- **＋ Citation:** opens the citation picker.

The Markdown is on the left and the live preview is on the right.

## Right-hand panel

- **References:** how many entries the bibliography has, with **Import .bib**.
- **Citation syntax:** a reminder of the Pandoc citation forms.
- **Images and figures:** **Add image files**, for previewing images from your computer.
- **GitHub workflow:** **Connect repository** opens the GitHub dialog.
- **Keyboard shortcuts:** a summary of the [shortcuts](editing.md#keyboard-shortcuts).

## Status bar

The status bar shows:

- the word and character counts. Comments are not counted.
- whether the draft is saved in the browser, or a warning if browser storage is unavailable or full.
- how many citation keys are not in the loaded bibliography, if any. Hover over the warning to see the keys.

## Narrow screens

- **Narrower than about 1100 pixels:** the right-hand panel is hidden.
- **Phone width (narrower than about 760 pixels):** the left-hand panel is hidden too, and the editor fills the screen. Split and Edit views show the Markdown, and Preview view shows the preview. Use the top bar for GitHub, opening and saving. The GitHub dialog scrolls, so its buttons can always be reached.
