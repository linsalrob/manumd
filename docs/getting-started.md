# Getting started

## Open ManuMD

Open <https://linsalrob.github.io/manumd/> in a desktop browser: Chrome, Firefox, Edge or Safari. ManuMD works on a phone or tablet, but a laptop or desktop screen is much more comfortable for writing.

On your first visit ManuMD shows a sample manuscript, so you can see what it does. The sample is replaced when you open or start a file.

You can also run ManuMD without the hosted site: download [`dist/index.html`](https://github.com/linsalrob/manumd/blob/main/dist/index.html) from the repository and open it in your browser. It's the same single file.

## Start writing

You have three ways to start:

- **Start a new file.** Click **＋** next to **Draft files**, at the bottom of the left-hand panel, and give the file a name, such as `paper.md`.
- **Open a file from your computer.** Click **Open .md** in the top bar and choose a Markdown file.
- **Load a file from GitHub.** Click **↗ GitHub**. See [Working with GitHub](github.md).

Each of these replaces the current draft. ManuMD asks first, unless the draft is empty or is still the sample.

## Your draft is saved as you type

Every change is saved in your browser straight away. The status bar at the bottom shows **● Draft saved in this browser**. If you close the tab and come back in the same browser, the draft is still there.

This draft lives only in this browser on this computer. Nobody else can see it, and it is lost if you clear your browser data. To keep the paper somewhere safer:

- **Save draft** (or {kbd}`Ctrl+S`, {kbd}`⌘+S` on a Mac) downloads the Markdown file to your computer.
- **Save commit**, in the GitHub dialog, saves it to a GitHub repository. See [Working with GitHub](github.md#save-a-commit).

## Add citations

1. Click **Import .bib** and choose your BibTeX file, for example the one Paperpile exports.
2. Put the cursor where the citation should go and click **＋ Citation** (or press {kbd}`Ctrl+Shift+C`).
3. Search by author, title, year or key, and click the reference.

ManuMD inserts a citation such as `[@Smith2024]`. The preview shows it as "(Smith, 2024)" and adds the work to the reference list at the end. See [Citations](citations.md).

## Next steps

- [The workspace](workspace.md): what each part of the screen does.
- [Editing](editing.md): views, editing in the preview, and keyboard shortcuts.
- [Markdown and equations](markdown.md): what you can write.
