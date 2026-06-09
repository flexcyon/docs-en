---
title: Accessibility
---

Toggle accessibility options.

Current options let you configure brightness, contrast, saturation etc. for the
theme's colours or globally.

Configuring the theme related accessibility settings before reaching for the global
filter effects is better for performance. The theme related settings also dynamically
almost all colours in the theme itself.

## Navigation

```md
Style Settings
|-- flexcyon://Accessibility
```

## Configuration Options

### Theme colour contrast offset

Define the contrast offset for the theme's colours.
For dark theme greater positive values increase contrast, the opposite is true
for light theme.

CSS Variable(s) targeted: `var(--flexcyon-theme-contrast-offset)`

Default: 0 (variable slider, range from -0.3 to 0.3)
> Values greater than +/- 0.3 do not feel that sensible for daily use.
> If a wider range of values are desired, do let me know.

### Theme colour warmth offset

Define the warmth offset the theme's colours.
Because oklch is a cyclical colour space, here are some tips on getting the
desired colour warmth.
- Dark mode = very cool background, set towards -20 for cool colours, 130
towards warmer colours.
- Light mode = somewhat warm background, set -70 toward to warmer colours, 80
towards cooler colours.

If you go beyond the ranges the colours would probably alternate from becoming
cool to becoming warm and vice versa.
> Do experiment with values ^_^.

CSS Variable(s) targeted: `var(--flexcyon-theme-warmth-offset)`

Default: 0

### Theme colour brightness ratio

Define the brightness ratio for the theme's colours.

CSS Variable(s) targeted: `var(--flexcyon-theme-brightness-ratio)`

Default: 1 (variable slider, range from 0 to 2)

### Theme colour saturation ratio

Define the saturation ratio for the theme's colours.

CSS Variable(s) targeted: `var(--flexcyon-theme-saturation-ratio)`

Default: 1 (variable slider, range from 0 to 5)

### Global brightness ratio

CSS Variable(s) targeted: `var(--flexcyon-brightness-ratio)`

Default: 1

### Global contrast ratio

CSS Variable(s) targeted: `var(--flexcyon-contrast-ratio)`

Default: 1

> E.g. if you want slightly more contrast like on an OLED screen, try values
> between 1 to 1.5

### Global saturation ratio

CSS Variable(s) targeted: `var(--flexcyon-saturation-ratio)`

Default: 1

> Use to modify the saturation of colors
