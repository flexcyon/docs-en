---
title: Archivos
icon: material/file-cog
---

Configurar árboles de archivos y estilos de carpeta.

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Files
|   |   |-- 。
|   |-- 。
|-- 。
```

## Opciones de configuración

### Habilitar extensiones de archivo dimmed en el explorador de archivos

CSSVariable(s) targeted:`var(--flexcyon-file-exp-dimmed-file-exts-enabled)`
Default:true(de clase)

### Seleccionar estilo de carpeta

CSSClasse(s) targeted:`.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`
Predeterminado: ninguno (clase selecto)

Opciones:

- Carpetas de arco iris
- Estilo de carpeta alternativo
- Estilo de árbol de archivos

### Color de fondo en lugar de texto para carpetas arco iris

CSSClasse(s) targeted:`var(--flexcyon-is-bg-rainbow)`
Default:false

#### Enable minimalist trees

CSSVariable(s) targeted:`var(--flexcyon-minimalist-tree)`
Default:false(de clase)

### Vertical Tree Item Padding

CSSClasse(s) targeted:`var(--flexcyon-tree-item-verti-padding)`
Default:1.5 px)

### Horizontal Tree Item Padding

CSSClasse(s) targeted:`var(--flexcyon-tree-item-horiz-padding)`
Predeterminado: 12 (px)

### Wrap Long File Names
Envuelve nombres de archivo largos a una nueva línea en lugar de omitir la parte final.
.

CSSVariable(s) targeted:`var(--flexcyon-wrap-long-filenames)`
Default:true(de clase)
