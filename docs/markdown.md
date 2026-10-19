# Markdown and equations

A ManuMD manuscript is a plain-text Markdown file: ordinary text, with a few symbols for formatting. The same file can be turned into Word, PDF or HTML with [Pandoc](https://pandoc.org/).

The preview supports the common subset of Markdown below. Anything else is shown as plain text, so nothing you write is lost; it simply isn't formatted in the preview.

## Markdown in two minutes

| You type | You get |
|---|---|
| `# Results`, `## Methods` | a heading and a subheading, down to `######` |
| `**bold**`, `*italic*`, `~~struck~~` | **bold**, *italic*, ~~struck~~ |
| `` `code` `` | `code` |
| `- item` or `1. item` at the start of a line | a bulleted or numbered list |
| a blank line | a new paragraph. A single line break doesn't start one. |
| `> quoted text` | a block quote |
| `[text](https://example.org)` | a link |
| `![A cat](images/cat.png)` | an image. See [Images and figures](images.md). |
| `$E = mc^2$` | an equation in the text |
| `$$ … $$` | an equation on its own line |
| `[@Smith2024]` | a citation. See [Citations](citations.md). |
| `<!-- note -->` | a hidden comment |

## Supported Markdown

**Headings.** `#` to `######` at the start of a line. Pandoc's `{#id}` after a heading sets its anchor, so `## Methods {#sec-methods}` can be linked as `[the methods](#sec-methods)`.

**Emphasis.** Bold, italic, strikethrough and inline code.

**Lists.** Bulleted (`-`, `*` or `+`) and numbered (`1.` or `1)`) lists. Indent a line by two or more spaces to continue the previous item. Nested lists are not supported in the preview.

**Code blocks.** Fence code with three backticks or tildes:

````markdown
```python
print("hello")
```
````

Nothing inside a code block is formatted, including comments, citations and math.

**Block quotes.** Lines starting with `>`.

**Tables.** A header row, then a delimiter row, then the body. Colons in the delimiter row set the alignment:

```markdown
| Sample | Reads | GC (%) |
|:-------|------:|:------:|
| A      | 1,204 | 41.2   |
```

**Horizontal rules.** A line of three or more `-`, `*` or `_`.

**Links.**

- Web links open in a new tab.
- `#heading` links scroll the preview to that heading.
- Relative links, such as `[the data](data/table.csv)`, open the file on GitHub when the draft was loaded from GitHub.

**Image attributes.** Pandoc's attributes after an image, such as the figure labels used by pandoc-crossref, are applied and not shown:

```markdown
![**Figure 1.** Entropy across the genome.](images/fig1.png){#fig:1 width=100%}
```

- the identifier (`#fig:1`) becomes a link target, so `[Figure 1](#fig:1)` scrolls the preview to the figure;
- `width` and `height` size the image, in pixels or units such as `%`, `cm` or `in`;
- other attributes are ignored by the preview and kept in the file for Pandoc.

Attributes after a link, such as `[text](https://example.org){.external}`, are hidden too.

**Fenced divs.** Pandoc's `:::` fences are hidden, and the text between them is shown as usual. `::: {#refs}` marks where the reference list goes, as it does in Pandoc. The preview places it there, under your own heading, instead of at the end:

```markdown
# References

::: {#refs}
:::
```

**YAML front matter.** A block between `---` lines at the very top of the file holds the title, authors and Pandoc settings. The preview shows it as text. ManuMD reads one field itself: `bibliography:`. See [Citations](citations.md#bibliography-from-github).

```yaml
---
title: "Entropy in microbial genomes"
bibliography: references.bib
---
```

**Raw HTML.** Shown as text, never rendered. This keeps the preview safe however the Markdown was written.

## Comments

Text between `<!--` and `-->` is a comment:

```markdown
<!-- RAE: should this be 0.19 bits, as in Fig. S14? -->
```

Comments are hidden from the preview and the word count, but they stay in the file. That makes them useful for:

- **notes to co-authors.** Start the comment with your initials, so others know who wrote it.
- **notes to yourself or to an AI agent** that works on the file. A fixed prefix such as `<!-- TODO:` or `<!-- AGENT:` makes them easy to search for.
- **provenance:** where a number came from.

Things to know:

- A comment inside a code block is shown as code, not hidden.
- Comments are not private. Anyone who can read the file, for example on GitHub, can read them.
- Pandoc drops comments when it makes Word or PDF output. In HTML output they remain in the page source.
- [Editing in the preview](editing.md#editing-in-the-preview) never shows or changes comments between blocks.

## Equations

Write LaTeX math with Pandoc's syntax:

- `$...$` for math in the text, such as `$H = -\sum_i p_i \log_2 p_i$`.
- `$$...$$` for an equation on its own line. It can be on one line or spread over several:

  ```latex
  $$
  H = -\sum_{i=1}^{n} p_i \log_2 p_i
  $$
  ```

A `$` followed by a space, or a closing `$` followed by a digit, is not math, so prices such as "$100 and $1" are left alone. Write `\$` for a literal dollar sign.

Equations are typeset with [KaTeX](https://katex.org/), which handles most LaTeX math but not every package. ManuMD downloads KaTeX the first time a draft contains math. If you are offline, or the download fails, equations are shown as their TeX source and the rest of the preview still works. See [Your data and privacy](privacy.md#katex).

## Turning the Markdown into a paper

ManuMD's preview is for writing, not for the final layout. To make a Word or PDF file in the journal's style, use Pandoc with its citation processor:

```bash
pandoc paper.md --citeproc --bibliography references.bib --csl journal.csl -o paper.docx
```

The citation syntax, front matter and math in ManuMD are all Pandoc's, so the same file works unchanged. If the front matter names the bibliography, you can leave out `--bibliography`.
