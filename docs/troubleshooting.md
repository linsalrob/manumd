# Troubleshooting

## GitHub

| What you see | What to do |
|---|---|
| "GitHub did not accept the token" | The token was mistyped, has expired or was revoked. [Make a new one](github.md#create-a-token) and paste it into the dialog. |
| "Your token cannot read…" or "cannot write to…" | Check that the **Repository** field names the repository the token was made for. If it does, edit the token on GitHub (Settings → Developer settings → Fine-grained tokens): **Repository access** must include the repository, and **Contents** must be **Read and write** to save. |
| The same message, for an organisation's repository | The token's **Resource owner** must be the organisation, and the organisation may need to approve the token. |
| "Not found" | Check the repository, branch and path. GitHub also reports a private repository as not found when the token can't see it, or when there's no token. |
| "uses single sign-on" | On GitHub's token page, choose **Configure SSO** and authorise the token for the organisation. |
| "is a protected branch" | The branch doesn't accept direct commits. Save to another branch and open a pull request. |
| "rate limit was reached" | Wait a few minutes. Enter a token if you haven't: the limit without one is much lower. |
| "The file changed on GitHub since you loaded it" | **Save draft** to download your version, **Load file** again, and redo your edits. See [When someone else changed the file](github.md#when-someone-else-changed-the-file). |
| "A GitHub token with Contents: write access is required to commit" | Paste a token into the dialog. In a new tab, you need to paste it again. |
| The token field is empty after opening a new tab | That's by design: the token is kept for one tab only. Paste it again. |
| "Enter the repository as owner/repository" | Type the repository as `owner/name`, such as `linsalrob/manumd`. |

## Citations

| What you see | What to do |
|---|---|
| "Load your Paperpile .bib file first" | Click **Import .bib**, or load the paper from GitHub with its bibliography. |
| Citations appear as `?key`, and the status bar counts missing keys | The key isn't in the loaded bibliography. Check its spelling, or export the bibliography again. Hover over the status bar warning to see the keys. |
| The References panel is empty after loading from GitHub | Check the **BibTeX file** field, or the `bibliography:` field in the front matter, then **Load file** again. A notice says if the file wasn't found. |
| My imported bibliography was replaced | Loading from GitHub loads the repository's bibliography. Empty the **BibTeX file** field to keep yours. See [Bibliography from GitHub](citations.md#bibliography-from-github). |
| "duplicate keys ignored" after an import | Two entries in the `.bib` file share a key. ManuMD uses the first. Fix the key in your reference manager. |

## Images

| What you see | What to do |
|---|---|
| "Image not loaded: images/fig1.png" | Load the paper from GitHub with the right **Images folder**, or add the file with **＋ Image**. Check that the path in the Markdown matches the file name, including capitals. |
| An image in a subfolder of the images folder doesn't appear | Only images directly inside the folder are loaded. Add it with **＋ Image**, or move it up a level. |
| "Showing images cached from an earlier version" | GitHub couldn't be reached, so ManuMD shows the images it saved before. Load the file again when you're back online. |
| "Not loaded:" followed by image names | Those images are over 25 MB, or couldn't be downloaded. Use a smaller file, or load the paper again. |
| Images I added disappeared after a reload | Added images last for one session. Add them again, or commit them to the repository's images folder. |

## Equations

| What you see | What to do |
|---|---|
| "Equations are shown as TeX source" | ManuMD couldn't download KaTeX. Check your internet connection, then reload. |
| An equation shows an error in red | KaTeX doesn't support that command, or there is a typo. Check the TeX. |
| A price such as "$5" turned into math | Write `\$5`. |

## Drafts

| What you see | What to do |
|---|---|
| "Browser storage unavailable or full" in the status bar | Your draft is kept only until the tab closes. **Save draft** now. Private windows and very large bibliographies are the usual causes. |
| My draft is gone | Drafts belong to one browser on one computer, and to the address you opened ManuMD from. Check you're using the same browser and address. Clearing site data deletes the draft. |
| "The Markdown changed while you were editing this block" | The file changed under an open block edit, for example after a GitHub load. Make the edit again. |

## Still stuck?

[Open an issue](https://github.com/linsalrob/manumd/issues) describing what you did and what you saw. Never include your token.
