---
title: Prompts
icon: material/text-box 
---

Configurar los avisos tales como el aviso de comando, conmutador rápido etc.
.

Formatos aceptados: px, vw, vh

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Prompts
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Prompts

### Prompt width

CSS Variable(s) targeted:`var(--prompt-width)`

Predeterminado: 700 (px)

### Prompt max width

CSS Variable(s) targeted:`var(--prompt-max-width)`

Default: 80 (vw)

### Prompt max height

CSS Variable(s) targeted:`var(--prompt-max-height)`

Default: 70 (vh)

### Prompt alignment

CSS Classe(s) targeted: `.flexcyon-prompt-align-bottom-left,
,
.flexcyon-prompt-align-bottom-center, .flexcyon-prompt-align-center-izquierda,
,
.flexcyon-prompt-align-top-left, .flexcyon-prompt-align-top-center`

Predeterminado: ninguno (clase selecto)
Opciones:

- Arriba a la izquierda
- Topcenter
-Centerizquierda
- El fondo izquierdo
- Bottomcenter

### Suggestion item vertical padding

CSS Variable(s) targeted:`var(--flexcyon-suggestion-verti-padding)`

Valor por defecto: 8 (px)

### Suggestion item horizontal padding

CSS Variable(s) targeted:`var(--flexcyon-suggestion-horiz-padding)`

Default value: 12 (px)
