# Your data and privacy

ManuMD has no server of its own. The app is one static web page. Once it has loaded, everything happens in your browser. Your manuscript, bibliography and token are never sent to ManuMD's authors or to any other service, apart from GitHub when you ask it to load or save.

ManuMD has no analytics, tracking or telemetry.

## What is stored, and where

| What | Where | How long |
|---|---|---|
| Draft text, document name and bibliography | the browser's local storage | until you replace them or clear your browser data |
| Repository, branch, file, folders and the version you loaded | local storage, with the draft | as above |
| The **⇅ Sync scroll** setting | local storage | as above |
| GitHub token | the tab's session storage | until you close the tab or click **Forget token** |
| Images from GitHub | the browser's IndexedDB | the three most recent versions of each folder; older ones are removed |
| Image files you add | memory only | until you reload or close the tab |

All of this belongs to the site you opened ManuMD from. The hosted app at `linsalrob.github.io` and a copy opened from your own computer have separate storage, so a draft in one doesn't appear in the other.

If browser storage is unavailable or full, for example in some private windows or with a very large bibliography, the status bar says so. The content is then kept only until the tab closes, so download it.

## Your GitHub token

- The token goes only from your browser to GitHub's API, `api.github.com`.
- It is kept in the tab's session storage, so it survives a reload. The browser clears it when you close the tab, and **Forget token** clears it at once.
- It is never written to local storage, IndexedDB or any other lasting store.

**Shared origin.** Session storage belongs to the site's origin. On the hosted app the origin is `linsalrob.github.io`, which every GitHub Pages project under that account shares. Another page from that origin opened *in the same tab* could read the token. To limit the risk:

- use a fine-grained token limited to the manuscript repository, with only **Contents** permission;
- give it an expiry date;
- click **Forget token** when you finish, especially on a shared computer.

## What goes over the network

| Request | When | What is sent |
|---|---|---|
| The ManuMD page | when you open it | nothing of yours |
| GitHub API | when you load or save | the repository, branch and paths you entered, your token and, when saving, the Markdown file |
| KaTeX, from the jsDelivr CDN | the first time a draft contains math | nothing of yours |

### KaTeX

ManuMD has one external component: [KaTeX](https://katex.org/), which typesets equations. When a draft contains math, ManuMD downloads KaTeX 0.19.0 from the jsDelivr CDN. The version is pinned, and the files are checked with Subresource Integrity, so the browser refuses them if they differ from the published release. Only the KaTeX files are requested. Your text is never sent. Offline, or if the CDN can't be reached, equations are shown as their TeX source.

## Your manuscript is untrusted input

ManuMD treats the Markdown and BibTeX it displays as untrusted, because they may come from other people. Raw HTML in the Markdown is shown as text, not rendered, and links and images are limited to safe addresses. A manuscript can't run code in your browser through ManuMD.

## Grammar-checking extensions

Browser extensions such as Grammarly can read what you type in the Markdown text area, as they can on any page. Whether they work, and what they send to their own servers, is up to the extension.
