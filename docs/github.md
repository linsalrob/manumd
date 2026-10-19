# Working with GitHub

ManuMD can load a Markdown file from a GitHub repository, with its figures and bibliography, and save your changes back as a commit. Your browser talks to GitHub directly. Nothing passes through a ManuMD server.

If you are a co-author who has been asked to edit a paper, start with [Editing a paper with co-authors](collaborating.md). It walks through every step, including forking the repository and opening a pull request.

## Create a token

To save commits, or to read a private repository, ManuMD needs a GitHub **fine-grained personal access token**. A token is a password-like code that lets ManuMD act on your account. A fine-grained token is limited to the repositories and permissions you choose.

1. On GitHub, click your profile picture (top right) and choose **Settings**.
2. At the bottom of the left-hand menu, click **Developer settings**.
3. Click **Personal access tokens**, then **Fine-grained tokens**.
4. Click **Generate new token**. GitHub may ask for your password or a security code.
5. Fill in the form:
   - **Token name:** something you'll recognise, such as `ManuMD paper`.
   - **Expiration:** a date after you expect to finish, such as 90 days. You can make a new token later.
   - **Resource owner:** the account that owns the manuscript repository. For an organisation's repository, choose the organisation. The organisation may need to approve the token.
   - **Repository access:** **Only select repositories**, then the manuscript repository. If you write several papers, select each of their repositories, so one token works for all of them. See [One token for several manuscripts](#one-token-for-several-manuscripts).
   - **Permissions:** under **Repository permissions**, set **Contents** to **Read and write**. (On some versions of the page, first click **Add permissions** and tick **Contents**.) GitHub adds **Metadata: Read-only** automatically. Leave everything else off.
6. Click **Generate token**.
7. **Copy the token now.** It starts with `github_pat_`, and GitHub shows it only once. If you lose it, delete it and make another.

Keep the token private, like a password. Paste it only into ManuMD's GitHub dialog.

For a **public** repository, you can load files without a token. Saving always needs one.

### One token for several manuscripts

You don't need a new token for each paper. One fine-grained token can cover several repositories:

- **When you make the token,** choose **Only select repositories** and select every manuscript repository.
- **For a new paper later,** edit the token on GitHub (Settings → Developer settings → Fine-grained tokens, then click the token) and add the new repository under **Repository access**.

Some limits:

- **One owner per token.** A token covers repositories of one owner only: your account or a single organisation. Papers in your account and papers in a lab organisation need a token each.
- **More reach if it leaks.** Anyone who has the token can change every repository it covers. Select only manuscript repositories, rather than **All repositories**, and give only **Contents** permission.

ManuMD keeps the token until you close the tab, so you paste it once per tab and then switch between papers with [Recent manuscripts](#switch-between-manuscripts).

## Load a file

1. Click **↗ GitHub** in the top bar, or **Connect repository** in the right-hand panel.
2. Fill in the dialog:

   | Field | What to enter | Example |
   |---|---|---|
   | **Repository** | `owner/repository`. A pasted `https://github.com/…` address also works. | `linsalrob/genome_entropy` |
   | **Branch** | The branch with the paper. | `main` |
   | **Markdown file path** | The file's path in the repository. | `paper/manuscript.md` |
   | **Images folder** | Relative to the Markdown file. Leave empty for no images. | `images` |
   | **BibTeX file** | Relative to the Markdown file. Leave empty to keep your imported bibliography. | `references.bib` |
   | **GitHub token** | Your token. | `github_pat_…` |

3. Click **Load file**. If ManuMD asks whether to replace the current draft, say yes. (Download the draft first if you want to keep it.)

ManuMD loads the file, then the images and the bibliography. See [Images from GitHub](images.md#images-from-github) and [Bibliography from GitHub](citations.md#bibliography-from-github).

ManuMD remembers the repository, branch, file and folders with the draft. Next time, open the dialog and click **Load file** straight away.

## Switch between manuscripts

ManuMD keeps a list of the ten files you loaded or committed most recently. To switch to another paper:

1. Click **↗ GitHub**.
2. Choose the paper under **Recent manuscripts**. ManuMD fills in its repository, branch, file and folders.
3. Click **Load file**.

The list is kept in the browser's local storage, so it lasts after you close the tab. It holds only where each file is, never a token: in a new tab, paste the token again. With [one token for several manuscripts](#one-token-for-several-manuscripts), the same token works for every paper on the list.

**Clear list**, next to the list, removes every entry. The list is also cleared when you clear the browser's data for the site.

## Save a commit

1. Click **↗ GitHub**. Check that the fields still name the right repository, branch and file.
2. Click **Save commit**.
3. ManuMD asks for a **commit message**. Replace the suggested `Edit paper/manuscript.md with ManuMD` with a short description of the change, such as `Tighten the Discussion`.
4. Click **OK**. The status bar shows **Commit saved to GitHub**.

Commit whenever you finish a piece of work, and before you close the tab. Small, frequent commits are easier for co-authors to review.

Only the Markdown file is committed. ManuMD never commits images or the bibliography.

:::{note}
**Save draft** and {kbd}`Ctrl+S` download the file to your computer. They don't save to GitHub.
:::

### When someone else changed the file

ManuMD commits against the version of the file you loaded. If the file has changed on GitHub since then, for example because a co-author committed, ManuMD refuses to save rather than overwrite their work:

1. Click **Save draft** to download your version as a backup.
2. Click **↗ GitHub**, then **Load file**, to load the latest version.
3. Make your edits again. Your downloaded file shows what they were.

### Saving to a different file or branch

If you change the repository, branch or path to one you didn't load, ManuMD checks whether that file exists. If it does, ManuMD asks before replacing it. If it doesn't, the commit creates it.

### Protected branches

Some repositories don't allow direct commits to their main branch. ManuMD then explains that the branch is protected. Save to another branch instead, then open a pull request on GitHub.

## Your token in ManuMD

- **For the tab only.** ManuMD keeps the token in the tab's session storage. It survives a reload, and the browser clears it when you close the tab. In a new tab, paste it again.
- **Never stored permanently.** The token is never written to local storage, IndexedDB or any other lasting store.
- **Sent only to GitHub.** It goes from your browser to `api.github.com` and nowhere else.
- **Forget token** in the GitHub dialog removes it at once. Use it when you finish on a shared computer.

On the hosted site, session storage belongs to `linsalrob.github.io`, which all GitHub Pages projects under that account share. Another page from that address opened *in the same tab* could read the token. That's one reason to use a fine-grained token limited to your manuscript repositories. See [Your data and privacy](privacy.md).

## When GitHub refuses

If a load or save fails, the GitHub dialog stays open and explains the likely cause:

| Message begins | What it means |
|---|---|
| "GitHub did not accept the token" | The token has expired, was revoked or was mistyped. Make a new one. |
| "Your token cannot read…" / "cannot write to…" | The token's **Repository access** doesn't include this repository, or **Contents** isn't **Read and write**. Check the **Repository** field too: is it the repository the token was made for? |
| "Not found" | Check the repository, branch and path. GitHub also reports a private repository as not found when the token can't see it, or when no token is given. |
| "The organisation … uses single sign-on" | On GitHub's token page, choose **Configure SSO** and authorise the token for that organisation. |
| "… is a protected branch" | Save to another branch and open a pull request. |
| "GitHub's rate limit was reached" | Wait a few minutes. Without a token, GitHub's limit is much lower, so enter one. |
| "The file changed on GitHub since you loaded it" | See [When someone else changed the file](#when-someone-else-changed-the-file). |

More problems and fixes are in [Troubleshooting](troubleshooting.md).

## Setting up a repository for ManuMD

ManuMD works with any repository, but this layout needs no changes to the dialog's defaults:

```text
paper/
  manuscript.md      the paper
  references.bib     the bibliography, for example synced from Paperpile
  images/            the figures, referred to as images/fig1.png
```

Put `bibliography: references.bib` in the paper's front matter. ManuMD and Pandoc then both find the bibliography without being told.

Consider adding an `EDITING.md` for co-authors, based on [Editing a paper with co-authors](collaborating.md), with your repository's name, branch and file filled in.
