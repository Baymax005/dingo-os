# Dingo OS Branding Assets

This directory contains branding materials for Dingo OS.

## Directory Structure

```
branding/
├── logos/           # Logo files in various formats
├── wallpapers/      # Desktop wallpapers
├── plymouth/        # Boot splash theme
├── grub/           # GRUB theme
└── icons/          # Custom icon theme
```

## Logo Guidelines

- **Primary Color**: Orange (#E65100)
- **Accent Color**: Amber (#FF8F00)
- **Logo**: Kangaroo silhouette with circuit board patterns
- **Typography**: Ubuntu font family

## Wallpapers

- Default: 4K abstract kangaroo design with orange/amber gradient
- Dark variant: For dark mode users
- Light variant: For light mode users

## Plymouth Theme

Boot splash animation featuring:
- Dingo logo with loading animation
- Orange progress bar
- Ubuntu-inspired design language

## GRUB Theme

Minimal theme with:
- Dingo logo centered
- Orange/amber color scheme
- Clean font rendering
- Transparent menu background

## Installation

Assets are automatically installed during ISO build process via `scripts/build-iso.sh`.

## Creating Custom Assets

### Logo Requirements
- SVG format for scalability
- PNG exports: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256, 512x512
- Transparent background
- Monochrome variants for system tray

### Wallpaper Requirements
- Resolution: 3840x2160 (4K)
- Format: PNG (lossless) or JPEG (high quality)
- Color space: sRGB
- Should work well with both light and dark GTK themes

### Plymouth Requirements
- Script-based animation
- 16:9 aspect ratio support
- Low resource usage
- Fallback to text mode

## License

All branding assets are licensed under Creative Commons Attribution-ShareAlike 4.0.
