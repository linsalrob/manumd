# Editing

## Views

The **Split**, **Edit** and **Preview** buttons above the text choose the view:

- **Split:** Markdown on the left, preview on the right.
- **Edit:** Markdown only, for distraction-free writing.
- **Preview:** the formatted paper only. You can still edit it, block by block. See [Editing in the preview](#editing-in-the-preview).

The preview updates as you type.

## Jumping to a section

The **Outline** in the left-hand panel lists the paper's headings: `#`, `##` and `###`, indented by level. Click a heading, or {kbd}`Tab` to it and press {kbd}`Enter`, to jump there:

- **Split view:** both panes scroll to the heading, and the cursor moves to the start of its line, ready to type.
- **Edit view:** the Markdown scrolls to the heading, with the cursor on it.
- **Preview view:** the preview scrolls to the heading. Press {kbd}`Enter` to edit it.

The outline updates as you add, rename or remove headings. Headings inside code blocks, block quotes and comments are left out, as they are in the preview. Deeper headings (`####` and below) aren't listed.

## Keeping the two panes together

In Split view:

- **Double-click** a place in either pane to scroll the other pane to the same place.
- Turn on **⇅ Sync scroll** to keep the two panes scrolled together. ManuMD remembers the setting.

## Editing in the preview

In Preview view you can change the text without reading Markdown source for the whole paper.

1. **Double-click** a paragraph, heading, list item, table row, quote, equation, code block or the front matter. Or, with the keyboard, move focus to the preview and press {kbd}`Enter` to edit the first block visible at the top of the view.
2. A small editor opens in place, showing exactly the Markdown that block was made from.
3. Make your change, then:
   - press {kbd}`Ctrl+Enter` ({kbd}`⌘+Enter` on a Mac), click **Apply**, or click elsewhere to apply it; or
   - press {kbd}`Esc`, or click **Cancel**, to discard it.

Only that block's lines change. The rest of the file, including citations, equations and comments between blocks, is left exactly as it was. Comments inside the block do appear in the editor, so take care not to delete them.

While the editor is open:

- the citation picker ({kbd}`Ctrl+Shift+C`) and the formatting buttons apply the edit, then act at the place where you were typing in the block.
- the preview waits to re-render until you finish, for example when images or the bibliography finish loading.
- switching view or downloading the file applies the edit first.

If the Markdown changed while the block was open, for example because you loaded a file from GitHub, ManuMD doesn't apply the edit. It tells you, so you can make it again.

In Split view, double-clicking aligns the panes instead. Edit the Markdown directly there.

## Formatting

The formatting buttons wrap the selected text, or add a prefix to the line:

| Button | Shortcut | Markdown |
|---|---|---|
| **B** (bold) | {kbd}`Ctrl+B` / {kbd}`⌘+B` | `**text**` |
| *I* (italic) | {kbd}`Ctrl+I` / {kbd}`⌘+I` | `*text*` |
| **H** (heading) | | `# ` at the start of the line |
| ❞ (quote) | | `> ` at the start of the line |
| `</>` (code) | | `` `text` `` |
| ↗ (link) | | `[text](https://…)`; ManuMD asks for the address |

See [Markdown and equations](markdown.md) for everything the preview understands.

## Keyboard shortcuts

| Keys | Action |
|---|---|
| {kbd}`Ctrl+B` / {kbd}`⌘+B` | Bold |
| {kbd}`Ctrl+I` / {kbd}`⌘+I` | Italic |
| {kbd}`Ctrl+S` / {kbd}`⌘+S` | Download the Markdown file |
| {kbd}`Ctrl+Shift+C` / {kbd}`⌘+Shift+C` | Open the citation picker |
| Click or {kbd}`Enter` on an outline heading | Jump to that section |
| Double-click, Split view | Align the other pane |
| Double-click or {kbd}`Enter`, Preview view | Edit a block in place |
| {kbd}`Ctrl+Enter` / {kbd}`⌘+Enter` | Apply a block edit |
| {kbd}`Esc` | Cancel a block edit, or close a dialog |

Every control can be reached with {kbd}`Tab`, and the focused control is outlined.

## Grammar checkers

A browser Grammarly extension may work in the Markdown text area, depending on the browser and the extension. ManuMD has no grammar checker of its own. See [Limitations](limitations.md).
