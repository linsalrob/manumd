# Editing a paper with co-authors

This guide is for co-authors who have been asked to edit a paper that is kept on GitHub. You don't need to have used GitHub before, and you don't need to install anything: everything happens in a web browser.

It is adapted from the [editing guide for the genome_entropy paper](https://github.com/linsalrob/genome_entropy/blob/manuscript/manuscript/EDITING.md), the first paper written with ManuMD.

:::{tip}
**Lead authors:** copy this page into your repository as `EDITING.md`, and replace the example names below with your own. Then co-authors have exact values to type.
:::

## The example in this guide

The guide uses these example names. Your lead author will tell you the real ones.

| | Example |
|---|---|
| The lead author's repository | `lead-author/paper` |
| The branch with the paper | `main` |
| The manuscript | `paper/manuscript.md` |
| The bibliography | `paper/references.bib` |
| The figures | `paper/images/` |

You will:

1. **Fork** the repository: make your own copy of it on GitHub ([step 1](#step-1-fork-the-repository)).
2. **Create a token**: a password that lets ManuMD save to your copy, and nothing else ([step 2](#step-2-create-a-personal-access-token)).
3. **Edit** the paper in [ManuMD](https://linsalrob.github.io/manumd/) ([step 3](#step-3-edit-the-paper-in-manumd)).
4. **Open a pull request**: send your changes back to the lead author, who reviews and merges them ([step 4](#step-4-send-your-changes-back-with-a-pull-request)).

Steps 1 and 2 are done once. After that, each editing session is step 3, plus step 4 if you don't already have a pull request open.

## A few words you will see

| Word | Meaning |
|---|---|
| **Repository** ("repo") | A project folder on GitHub, with the full history of every change. |
| **Branch** | A named version of the repository. The paper may live on a branch other than `main`. |
| **Fork** | Your own copy of the repository, under your GitHub account, such as `your-username/paper`. You can change your fork freely; nothing you do there affects the lead author's copy. |
| **Commit** | A saved change, with a short message saying what changed. |
| **Pull request** ("PR") | A request to copy your commits from your fork into the lead author's repository. They can read the changes line by line, comment on them, and merge them. |
| **Personal access token** | A long, password-like code that lets a program (here, ManuMD) act on your GitHub account, limited to the repositories and permissions you choose. |

## Before you start

You need a free GitHub account. If you don't have one, sign up at <https://github.com/signup>, then sign in.

## Step 1: Fork the repository

1. Go to the lead author's repository, such as `https://github.com/lead-author/paper`.
2. Click **Fork**, near the top right of the page.
3. On the **Create a new fork** page:
   - **Owner:** choose your own account.
   - **Repository name:** leave it as it is.
   - **Copy the `main` branch only:** if the paper is on a branch other than `main`, **untick this box**, so your fork includes that branch.
4. Click **Create fork**.

After a few seconds you'll be on your fork, at `https://github.com/your-username/paper`. The page says "forked from lead-author/paper" under the name.

To check that the paper is there, choose the paper's branch from the branch menu at the top left of the file list, and look for the manuscript file.

:::{note}
If the paper's branch is missing because the box was ticked, delete the fork and fork again. Open the fork's **Settings** tab, scroll to the **Danger Zone** at the bottom, and click **Delete this repository**. Make sure you are deleting *your fork*, `your-username/paper`. (You don't have permission to delete the lead author's repository anyway.)
:::

## Step 2: Create a personal access token

ManuMD saves your edits to your fork with a **fine-grained personal access token**. Make one that can change **only your fork**, and only its files.

1. On GitHub, click your profile picture (top right) and choose **Settings**.
2. In the left-hand menu, scroll to the bottom and click **Developer settings**.
3. Click **Personal access tokens**, then **Fine-grained tokens**.
4. Click **Generate new token**. GitHub may ask for your password or a security code.
5. Fill in the form:
   - **Token name:** something you'll recognise, such as `ManuMD paper`.
   - **Expiration:** a date after you expect to finish editing, such as 90 days. You can make a new token later.
   - **Resource owner:** your own account.
   - **Repository access:** choose **Only select repositories**, then select **your-username/paper**, your fork.
   - **Permissions:** under **Repository permissions**, find **Contents** and set it to **Read and write**. (On some versions of the page you first click **Add permissions** and tick **Contents**.) GitHub adds **Metadata: Read-only** automatically; that is expected. Leave every other permission off.
6. Click **Generate token** at the bottom, and confirm if asked.
7. **Copy the token now.** It starts with `github_pat_`. GitHub shows it only once; if you lose it, delete it and make another.

Keep the token private, like a password. Paste it only into ManuMD. Don't email it, and don't paste it into the manuscript, an issue or a pull request.

## Step 3: Edit the paper in ManuMD

[ManuMD](https://linsalrob.github.io/manumd/) shows the text beside a formatted preview, with the figures, equations and a reference list built from the paper's bibliography. It runs entirely in your browser: your text and token go only between your browser and GitHub.

Use a desktop browser (Chrome, Firefox, Edge or Safari) on a laptop or desktop computer.

### Connect ManuMD to your fork

1. Open <https://linsalrob.github.io/manumd/>. On your first visit it shows a sample manuscript; it will be replaced.
2. Click **↗ GitHub** in the toolbar at the top, or **Connect repository** in the right-hand panel. Fill in the dialog:

   | Field | What to enter |
   |---|---|
   | **Repository** | `your-username/paper`: your fork, *not* `lead-author/paper` |
   | **Branch** | the paper's branch, such as `main` |
   | **Markdown file path** | `paper/manuscript.md` |
   | **Images folder** | `images` (the default) |
   | **BibTeX file** | `references.bib` (the default) |
   | **GitHub token** | your token from step 2 |

   The images folder and BibTeX file are found relative to the manuscript, so `images` means `paper/images` and `references.bib` means `paper/references.bib`.
3. Click **Load file**. If ManuMD asks whether to replace the current draft, say yes.

ManuMD loads the paper, downloads the figures (all of them the first time; after that, only figures that have changed) and loads the bibliography. The status bar at the bottom shows the word count, and the **References** panel on the right lists the references.

ManuMD remembers the repository, branch and file, so next time you can open the dialog and click **Load file** straight away. It keeps the token only until you close the browser tab, so you'll paste it again in a new tab.

### Find your way around

- **Views.** The buttons above the text switch between **Split** (Markdown on the left, preview on the right), **Edit** (Markdown only) and **Preview** (formatted only).
- **Keeping the two panes together.** In Split view, double-click a place in either pane to bring the other pane to the same place. Or turn on **⇅ Sync scroll** to keep them scrolled together.
- **Editing in the preview.** In Preview view, double-click a paragraph, heading, list item, table row, equation or other block. A small editor opens with that block's Markdown. Make your change, then press {kbd}`Ctrl+Enter` ({kbd}`⌘+Enter` on a Mac), click **Apply**, or click elsewhere to apply it. Press {kbd}`Esc` to cancel. Only that block changes; the rest of the file is untouched.
- **Formatting.** The **B**, **I**, **H**, quote, code and link buttons wrap the selected text in Markdown, such as {kbd}`Ctrl+B` for bold.

### Markdown in two minutes

The paper is written in Markdown: plain text with a few symbols for formatting.

| You type | You get |
|---|---|
| `# Results`, `## Missing genes` | a section heading and a subsection heading |
| `**bold**`, `*italic*` | **bold**, *italic* |
| `- item` at the start of a line | a bulleted list |
| a blank line | a new paragraph (a single line break does not start one) |
| `$H = -\sum p \log_2 p$` | an equation in the text; `$$ … $$` puts it on its own line |
| `[@Hyatt2010-qv]` | a citation; see below |
| `![Caption](images/fig1.png)` | a figure |

There's more in [Markdown and equations](markdown.md).

### Things to leave alone

- **Hidden comments.** The text may contain comments like `<!-- src: Table S2 -->`. The preview hides them, but you'll see them in the Markdown and in the block editor. Papers often use them to record where numbers came from. **Don't delete or edit other people's comments.** If you change a number, leave its comment and say in your pull request where the new number comes from.
- **Figure lines.** Lines starting `![` place the figures. Edit the caption text if you like, but don't change the file name in brackets.
- **Citation keys.** Keep the exact text inside `[@…]`.

### Citations

References are cited by their key in the paper's bibliography, `paper/references.bib`. Keys look like `Hyatt2010-qv`. To add one:

1. Put the cursor where the citation should go.
2. Click **＋ Citation** (or press {kbd}`Ctrl+Shift+C`).
3. Search by author, title or year, and click the reference.

| Form | Use |
|---|---|
| `[@Hyatt2010-qv]` | one reference |
| `[@Hyatt2010-qv; @Larralde2022-xa]` | several. Picking a second reference straight after a citation adds it to the same brackets. |
| `[see @Hyatt2010-qv, p. 4]` | with a prefix or page number |

The preview shows simple author–year citations and a reference list. The journal's style is applied later, so don't worry about how the citations look.

**If the reference you need isn't in the list,** don't add it to the `.bib` file: ManuMD doesn't save that file, and the lead author probably maintains it in a reference manager such as Paperpile. Instead, put a comment where the citation should go, with its DOI:

```markdown
<!-- CITE: 10.xxxx/the-doi-of-the-paper -->
```

Then mention it in your pull request. The lead author will add the reference and replace the comment with the citation. The status bar warns about any citation key that isn't in the bibliography.

### Questions and comments for the other authors

To leave a note without changing the text, add a comment starting with your initials:

```markdown
<!-- RAE: should this be 0.19 bits, as in Fig. S14? -->
```

Comments don't appear in the preview or the rendered paper, but everyone reviewing your pull request sees them.

### Save your work

ManuMD has two kinds of saving. Only the second one sends your edits to GitHub.

- **Draft saved in this browser** (automatic). Every change is saved in your browser as you type. The status bar shows **● Draft saved in this browser**. This protects you against a closed tab, but nobody else can see it, and it is lost if you clear your browser data.
- **Save commit** (sends to GitHub). Click **↗ GitHub**, check the fields are still as in the table above, and click **Save commit**. ManuMD asks for a **commit message**: replace the suggested `Edit paper/manuscript.md with ManuMD` with a short description, such as `Tighten the Discussion; fix Fig. 3 wording`. Click **OK**. The status bar shows **Commit saved to GitHub**.

Save a commit whenever you finish a chunk of work, and always before you close the tab. Small, frequent commits make your changes easier to review.

:::{note}
**Save draft** in the toolbar (and {kbd}`Ctrl+S`) *downloads* the file to your computer. It does not save to GitHub. It's useful as a backup.
:::

ManuMD never uploads images or the bibliography. It commits only the manuscript. If you want a figure changed, describe the change in your pull request.

When you're finished, click **↗ GitHub** and then **Forget token**, especially on a shared computer. (Closing the tab also clears it.)

## Step 4: Send your changes back with a pull request

Your commits are now in your fork. To offer them to the lead author:

1. Go to your fork, `https://github.com/your-username/paper`, and choose the paper's branch from the branch menu.
2. You'll see a message that the branch is "N commits ahead of lead-author/paper". Click **Contribute**, then **Open pull request**.
3. **Check the two branches at the top of the page.** This is the most common mistake. They must read:

   | | repository | branch |
   |---|---|---|
   | **base** (where the changes go) | `lead-author/paper` | the paper's branch |
   | **head** (where the changes come from) | `your-username/paper` | the paper's branch |

   If the paper isn't on `main`, GitHub often sets the base branch to `main` anyway. If it does, click **base:** and choose the paper's branch. With the wrong base, the pull request shows many unrelated files.
4. Scroll down to check the changes. Lines you removed are red, lines you added are green.
5. Give the pull request a title, such as `Edits to the Discussion (RAE)`. In the description, say what you changed and why. Mention any new references (with DOIs), changed numbers and their sources, and any questions.
6. Leave **Allow edits by maintainers** ticked, so the lead author can make small fixes directly.
7. Click **Create pull request**.

The lead author will review it. They may comment on particular lines or ask questions in the pull request. You'll get an email when they do, and you can reply on GitHub.

**Keep editing while the pull request is open.** New commits you save from ManuMD to the same branch of your fork are added to the same pull request automatically, so you don't need to open another.

## Next time: start from the latest version

Other people's changes are merged into the lead author's repository while you work. Before each new editing session, bring your fork up to date:

1. Go to your fork, choose the paper's branch, and click **Sync fork**.
2. Click **Update branch**.
   - If your previous pull request has been merged, GitHub may say your branch has commits that aren't in the lead author's branch, and offer **Discard N commits**. That's expected when pull requests are merged as a single combined commit ("squash merge"): your original commits are no longer needed. Click **Discard N commits**. Don't do this if your pull request has *not* been merged yet: you'd lose those edits.
3. In ManuMD, click **↗ GitHub** and **Load file**, so you edit the latest text.

## Problems and fixes

| What you see | What to do |
|---|---|
| ManuMD: "GitHub did not accept the token" | The token was mistyped, has expired or was deleted. Make a new one (step 2) and paste it into the dialog. |
| ManuMD: a message that the token can't access the repository, or that Contents permission is missing | If the **Repository** field names the lead author's repository, change it to your fork; your token only works there. Otherwise, edit the token on GitHub (Settings → Developer settings → Fine-grained tokens). Check that **Repository access** includes your fork and that **Contents** is **Read and write**. |
| ManuMD: "Not found", or the file won't load | Check the dialog fields: the repository is *your* fork, the branch is the paper's branch, and the path is the manuscript's path. |
| ManuMD: "The file changed on GitHub since you loaded it" | Your fork changed after you loaded the file, for example because you synced the fork in another tab. Click **Save draft** to download your edits as a backup, then **Load file** again and redo the edits. ManuMD refuses to overwrite the newer version, so nothing is lost. |
| Figures show as placeholders | Check the **Images folder** field, and load the file again. |
| The References panel is empty | Check the **BibTeX file** field, and load the file again. |
| Your fork has no branch with the paper | You forked with **Copy the `main` branch only** ticked. Delete the fork and fork again (step 1). |
| The pull request shows many unrelated files | The base branch is wrong. Change it to the paper's branch (step 4). |

There's more in [Troubleshooting](troubleshooting.md).

## Prefer not to use GitHub?

Ask the lead author for the Markdown file or a Word version, and send them your edits or comments.
