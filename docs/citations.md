# Citations

ManuMD cites works by their key in a BibTeX file, using Pandoc's citation syntax. The preview formats the citations and builds a reference list, so you can see the paper as it will read.

## Load a bibliography

There are two ways to give ManuMD a bibliography:

- **Import it from your computer.** Click **Import .bib** and choose the file.
- **Keep it in the manuscript's GitHub repository.** It is then loaded with the Markdown. See [Bibliography from GitHub](#bibliography-from-github).

ManuMD keeps the bibliography in your browser, with the draft, until you load another.

### From Paperpile

ManuMD is designed around Paperpile's BibTeX export, but any BibTeX file works.

1. In Paperpile, select the folder or label for the paper, or all papers.
2. Export it as BibTeX. Paperpile can also keep an exported `.bib` file up to date automatically; see Paperpile's help for the options.
3. Import that file into ManuMD, or commit it to the manuscript repository.

Paperpile keys look like `Hyatt2010-qv`. Keep them exactly as they are.

ManuMD reads quoted and braced values, nested braces, common LaTeX accents and escapes such as `{\"u}` and `\&`, multi-line fields and corporate authors in braces, such as `{World Health Organization}`. If two entries share a key, ManuMD says so and uses the first.

## Insert a citation

1. Put the cursor where the citation should go.
2. Click **＋ Citation**, or press {kbd}`Ctrl+Shift+C` ({kbd}`⌘+Shift+C` on a Mac).
3. Type a few words: an author, part of the title, a year, a journal or the key. Every word must match.
4. Click the reference, or press {kbd}`Enter` to choose the first one.

To cite several works together, insert them one after another. A citation inserted straight after another one joins its brackets, giving `[@Smith2024; @Lee2023]`.

## Citation syntax

| You type | Preview | Use |
|---|---|---|
| `[@Smith2024]` | (Smith, 2024) | one work |
| `[@Smith2024; @Lee2023]` | (Smith, 2024; Lee & Park, 2023) | several works |
| `[see @Smith2024, p. 4]` | (see Smith, 2024, p. 4) | a prefix and a locator |
| `Smith [-@Smith2024] showed…` | Smith (2024) showed… | the year only, after the author's name |

The preview uses a simple author–year style: one author by surname, two joined by "&", three or more as "et al.". The reference list at the end lists each work in order of first citation, with a link to its DOI or URL.

The preview does not apply journal styles (CSL). Use Pandoc for the final formatting. See [Turning the Markdown into a paper](markdown.md#turning-the-markdown-into-a-paper).

## Missing citations

A citation key that isn't in the bibliography appears in the preview as `?key`, and the status bar counts the missing keys. Hover over the warning to see which they are.

Common causes:

- the key was mistyped;
- the bibliography is an older export that doesn't yet include the work;
- no bibliography is loaded.

If you can't add the work to the bibliography yourself, leave a comment where the citation should go, with its DOI, for whoever maintains the bibliography:

```markdown
<!-- CITE: 10.1186/1471-2105-11-119 -->
```

## Bibliography from GitHub

When you load a Markdown file from GitHub, ManuMD also loads its bibliography from the same repository and branch. It looks for:

1. the file named by the `bibliography:` field in the Markdown's YAML front matter, the field Pandoc reads. If the field lists several files, ManuMD loads the first. Then, if there's no such field:
2. the **BibTeX file** set in the GitHub dialog, which is `references.bib` by default.

Both are relative to the Markdown file. If the paper is `paper/manuscript.md`, then `references.bib` means `paper/references.bib`, and `../refs/library.bib` means `refs/library.bib`. Paths can't point outside the repository.

The loaded bibliography replaces the one you imported. Two exceptions:

- **To keep your imported bibliography,** empty the **BibTeX file** field, and make sure the front matter has no `bibliography:` field.
- **If you import a `.bib` file while the GitHub one is still loading,** your import wins.

ManuMD never commits the bibliography. To change it, update the file in the repository, for example from Paperpile.

A Markdown file opened from your computer can't load its bibliography this way, because a browser can't read the files next to it. Use **Import .bib**.
