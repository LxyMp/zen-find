# Zen Find

A flat, theme-aware redesign of Zen Browser's native find bar.

![Zen Find](https://raw.githubusercontent.com/LxyMp/zen-find/main/docs/images/store-preview.png)

## Features

- Nine positions: left, center or right, combined with top, center or bottom. The default top position sits 40px below the content top.
- Opaque, theme-aware background with an optional custom CSS color.
- Entry and exit animation (180ms in, 140ms out) using only transform and opacity; disabled when reduced motion is requested.
- Optional compact mode that hides previous/next and the four find options, keeping close, input and match count.
- Native Firefox controls, keyboard behavior and accessibility are preserved.
- Responsive layout: on narrow panels the match count moves below the input and the options use two columns. The count reserves up to 180px on wider panels.

## Usage

Install **Zen Find** from Zen Mods, then press `Cmd+F` on macOS or `Ctrl+F` on Windows/Linux.

Open **Settings → Zen Mods → Zen Find** to change the position or enable compact mode.

## Settings

- **Horizontal position**: left, center, right.
- **Vertical position**: top, center, bottom. Top is 40px below the content top; left, right and bottom use 12px margins.
- **Background color**: leave empty to follow the Zen theme, or enter an opaque CSS color. `transparent` is rendered as black; invalid values make the background invalid.
- **Hide navigation and find options**: keeps close, input and match count.

## Compatibility

- Current target: Zen 1.23.3b (Gecko 158.0).
- Historical baseline: Zen 1.22b (Gecko 155.0.1).
- Verified on Zen 1.23.3b: input, Enter/Shift+Enter, Esc, no-match state, all native options, nine positions, narrow panels, sidebar, compact mode, split view, light/dark themes, custom background and disabling the mod.
- The final top 40px and 180/140ms animation were confirmed in the author's daily profile. The 180px count width is implemented; the Chinese long-count display has not been re-screenshotted. The structured layout measurements were taken before the final values were applied.
- The 1.22b build was not re-tested in this round.

## Notes

- This is a CSS-only mod. It does not change find behavior, shortcuts, match rules or the values of native find options.
- The background is intentionally opaque; page content does not show through.
- The exit animation is designed for the default top position. Other vertical positions move up by 40px on exit rather than returning to the absolute content top.
- Source and issue tracker: <https://github.com/LxyMp/zen-find>

## License

Theme store submissions are licensed under CC BY-NC-SA 4.0.
