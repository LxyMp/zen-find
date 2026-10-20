# Zen Find

A flat, theme-aware redesign of Zen Browser's native find bar.

![Zen Find](https://raw.githubusercontent.com/LxyMp/zen-find/main/docs/images/store-preview.png)

## Features

- Nine positions: left, center or right, combined with top, center or bottom.
- Opaque, theme-aware background with an optional custom CSS color.
- Optional compact mode that hides previous/next and the four find options, keeping close, input and match count.
- Native Firefox controls, keyboard behavior and accessibility are preserved.
- Responsive layout: on narrow panels the match count moves below the input and the options use two columns.

## Usage

Install **Zen Find** from Zen Mods, then press `Cmd+F` on macOS or `Ctrl+F` on Windows/Linux.

Open **Settings → Zen Mods → Zen Find** to change the position or enable compact mode.

## Settings

- **Horizontal position**: left, center, right.
- **Vertical position**: top, center, bottom.
- **Background color**: leave empty to follow the Zen theme, or enter an opaque CSS color. `transparent` is rendered as black; invalid values make the background invalid.
- **Hide navigation and find options**: keeps close, input and match count.

## Compatibility

- Baseline: Zen 1.22b (Gecko 155.0.1).
- Layout, nine positions, narrow panel, compact mode and focus styles verified on Zen 1.23.3b (Gecko 158.0).
- Full interaction and theme acceptance on 1.23.3b is still in progress.

## Notes

- This is a CSS-only mod. It does not change find behavior, shortcuts, match rules or the values of native find options.
- The background is intentionally opaque; page content does not show through.
- Source and issue tracker: <https://github.com/LxyMp/zen-find>

## License

Theme store submissions are licensed under CC BY-NC-SA 4.0.
