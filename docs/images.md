# Images and figures

Include an image with Markdown's image syntax:

```markdown
![Entropy across the genome](images/fig1_entropy.png)
```

The text in square brackets is the image's description, read by screen readers and shown when the image can't be displayed. Keep image paths **relative**, like `images/fig1_entropy.png`, so the manuscript works the same in ManuMD, on GitHub and in Pandoc.

The preview shows an image from one of three places, in this order:

1. **Image files you add** from your computer.
2. **The paper's images folder on GitHub,** when the draft was loaded from GitHub.
3. **A web address,** such as `https://example.org/figure.png`.

A relative path that matches none of them shows a placeholder, **Image not loaded**, with the path.

## Add image files from your computer

Click **＋ Image** or **Add image files** and choose one or more images. They appear in the preview wherever the Markdown refers to them, matched by path and then by file name. So `images/fig1.png` in the Markdown matches a file you added called `fig1.png`.

Added images are kept for the current session only. After a reload, add them again.

## Images from GitHub

When you load a Markdown file from GitHub, ManuMD also downloads the images in the paper's images folder. This is the **Images folder** in the GitHub dialog, `images` by default, and is relative to the Markdown file. So for `paper/manuscript.md` the default folder is `paper/images`.

- **Which files:** PNG, JPEG, GIF, WebP, SVG, AVIF and BMP files directly inside the folder. Subfolders are not read.
- **Size limit:** images over 25 MB are skipped, and ManuMD names them.
- **Matching:** `images/fig1.png` and `./images/fig1.png` both match. An image that doesn't match by path is matched by file name.
- **Sidebar:** the images are listed under **images (from GitHub)**.
- **No images:** to skip images, empty the **Images folder** field. A paper with no images folder is fine. ManuMD doesn't report it.

### The image cache

Downloaded images are stored in your browser, in IndexedDB. Each image is identified by its Git blob SHA, which changes only when the file's contents change. As a result:

- the first load downloads every image; later loads download only images that have changed.
- after a reload, the images reappear without downloading again, even offline.
- a reloaded draft shows the images of the version it was loaded with.
- if the folder can't be refreshed, for example when you're offline, ManuMD shows the last cached copy and says so.

The cache keeps the images of the three most recently loaded versions of each folder and removes older ones automatically. Clearing your browser's site data removes it.

## ManuMD never commits images

Saving to GitHub commits only the Markdown file. To add or change a figure, commit the image file to the repository on GitHub, or ask the person who maintains the repository to. The next **Load file** downloads it.
