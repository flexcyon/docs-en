---
title: Plugins
icon: material/hexagon-outline
---

For configuration of officially supported plugins

Accepted formats: HEX, rem, x.y, %

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## Configuration Options

### Alternate file tree

#### Folders font size

CSS Variable(s) targeted: `var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

<span style="font-size: 0.925rem">Sample Alternate file tree Folders font size</span>

#### Folders font color

CSS Variable(s) targeted: `var(--oz-fta-folder-pane-file-name-color)`

Default (light mode):
<span class="col-sqr" style="background-color: #080808"></span> #080808

Default (dark mode):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### Active folder color

CSS Variables(s) targeted: `var(--oz-fta-all-panes-active-text-color)`

Default (light mode):
<span class="col-sqr" style="background-color: #080808"></span> #080808

Default (dark mode):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### Files font size

CSS Variable(s) targeted: `var(--oz-fta-file-font-size)`

Default: 0.9 (rem)

<span style="font-size: 0.9rem">Sample Alternate file tree Files font size</san>

#### Files font color

CSS Variable(s) targeted: `var(--oz-fta-file-pane-file-name-color)`

Default:
<span class="col-sqr" style="background-color: #6f768599"></span> #6f768599

#### Disable folder icons

CSS Variable(s) targeted: `var(--flexcyon-oz-folder-icons-disabled)`

Default: false (class toggle)

#### Disable file tree header

CSS Variable(s) targeted: `var(--flexcyon-oz-file-tree-header-disabled)`

Default: false (class toggle)

#### Enable Alternate folder count

CSS Variable(s) targeted: `var(--flexcyon-oz-alternate-folder-count)`

Default: false (class toggle)

#### Enabled dimmed file extensions in file tree

CSS Variable(s) targeted: `var(--flexcyon-oz-dimmed-file-exts-enabled)`

Default: true (class toggle)

___

### Full Calendar

Accepted formats: x.y, %

#### Opacity of dimmed full calendar items

CSS Variables(s) targeted: `var(--flexcyon-fc-dimmed-items-opacity)`

Default: 0.89

<span style="opacity: 0.89">Sample opacity of dimmed full calendar items</span>

___

### Dataview

Accepted formats: px

#### Horizontal padding of dataview error messages

CSS Variables(s) targeted: `var(--flexcyon-dataview-horizontal-padding)`

Default: 8 (px)

___

### Canvas

Defines styles for the core Canvas plugin.

Accepted formats: px, RGB

#### Blur inactive Canvas nodes

CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-inactive-nodes)`

Default: false (class toggle)

#### Blur intensity for inactive nodes

Used with the previous setting to set the blur intensity of inactive canvas nodes
and all arrows/edges.

CSS Variable(s) targeted: `var(--flexcyon-canvas-blur-intensity)`

Default: 1 (px)

#### Canvas card menu alignment

Configure the alignment of the canvas card menu.

CSS Classe(s) targeted: `.flexcyon-canvas-menu-bottom-left,`
`
.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align
`

Default: none (class select)

Options:

- Bottom left

- Bottom right

- Top center

- Top left

- Top right

- Left aligned center

- Left aligned top

- Left aligned bottom

- Right aligned center

- Right aligned top

- Right aligned bottom

- Right aligned center align

___

### Various Complements
#### Vertical Suggestion Padding
CSS Variable(s) targeted: `var(--flexcyon-var-comps-sugg-vert-padding)`

Default: 7 (px)

#### Horizontal Suggestion Padding
CSS Variable(s) targeted: `var(--flexcyon-var-comps-sugg-horiz-padding)`

Default: 12 (px)

#### Compact Suggestion Mode
Overrides defaults. Uses padding 4px 8px.

CSS Variable(s) targeted: `var(--flexcyon-var-comps-compact-mode)`

Default: false (class toggle)

___
### Omnisearch

#### Disable Omnisearch Icons

CSS Classe(s) targeted: `var(--flexcyon-omnisearch-no-icons)`

Default: false (class toggle)

#### Omnisearch Body Left Margin

CSS Classe(s) targeted: `var(--flexcyon-omnisearch-body-margin-left-margin-left)`

Default: 1.45 (rem)

___
### Bases

#### Bases View Vertical Padding

CSS Variable(s) targeted: `var(--flexcyon-bases-padding-horiz)`

Default: 16 (px)

#### Bases View Horizontal Padding

CSS Variable(s) targeted: `var(--flexcyon-bases-padding-horiz)`

Default: 16 (px)

#### Bases Embed Padding

CSS Variable(s) targeted: `var(--bases-embed-padding)`

Default: 4 (px)

___

#### Bases Cards View

##### Bases Card Label Opacity

CSS Variable(s) targeted: `var(--flexcyon-bases-cards-label-opacity)`

Default: 0.85

##### Default string when Card View item image not found

CSS Variable(s) targeted: `var(--bases-no-img-str)`

Default: "No image path could be found for this file"

##### Bases Card Border Radius

CSS Variable(s) targeted: `var(--bases-border-r)`

Default: 16 (px)

##### Bases Card Group Padding

CSS Variable(s) targeted: `var(--bases-cards-group-padding)`

Default: 16 (px)

##### Bases Card Padding Top

CSS Variable(s) targeted: `var(--flexcyon-bases-card-padding-top)`

Default: 8 (px)

##### Bases Card Padding Right

CSS Variable(s) targeted: `var(--flexcyon-bases-card-padding-right)`

Default: 0 (px)

##### Bases Card Padding Bottom

CSS Variable(s) targeted: `var(--flexcyon-bases-card-padding-bottom)`

Default: 0 (px)

##### Bases Card Padding Left

CSS Variable(s) targeted: `var(--flexcyon-bases-card-padding-left)`

Default: 2 (px)

##### Bases Card View Flex Grow

This is the factor of how long the Card View takes to scale depending on tab size.

CSS Variable(s) targeted: `var(--flexcyon-bases-card-flex-grow)`

Default: 0.55

___

#### Bases Table View

##### Bases Table Cell left padding

CSS Variable(s) targeted: `var(--flexcyon-bases-td-padding-l)`

Default: 2 (px)

##### Bases Table Cell Content Alignment

CSS Variable(s) targeted: `var(--flexcyon-bases-table-content-alignment)`

Default: left (variable select)

Options:

- Left
- Center
- Right
