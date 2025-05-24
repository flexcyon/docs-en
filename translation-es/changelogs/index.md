---
icon: material/script-text
title: Cambios
---

#### Note

The changelogs show versions in order of most recent to least recent.
Or, if you prefer the changelogs in chronological order, you can use
the sidebar or hamburger menu to view the relevant sub-pages.

___

## Version 0.4.x

### Version 0.4.1 Quickfix Update

- Fijar el renderizado TUI en modo de luz

- Fijar la barra lateral izquierda cuando la cinta no está habilitada

- Fijar texto resaltado bg específicamente con sugerencias-luz

- Fijar las incrustaciones sin mostrar

### Version 0.4.0 Light Mode Update

- Cambio de la barra lateral de fondo de brillo predeterminado a`unset`. Was
previously causing issues like blurring Calender plugin content.

- Tema de luz WIP (mixes flexoki light + paleta de colores origami)

- Otros cambios erróneos

- Agregado a la parrilla de colores extendida, por defecto

  - Added table header size option

  - Updated documentation to show a small preview of colors/opacity applied by
  the theme

- Muestra web agregada de las características del tema

- Retirar la Pascua Modo de huevo

- Pincha de color estilo para opciones de modo ligero y oscuro

- ASCII Arte y citas ahora heredan de la fuente de interfaz

- Mejora de estilo rápido y relleno de elementos de árbol

- Regresar a Zero (modo minimalista del ultra) inspirado en el tema Shimmering Focus

## Version 0.3.x

### Version 0.3.6 Canvas Menu Update

- Cuestiones de fondo de barra lateral fija

- Evitar que los indicadores de encabezado aparezcan fuera de las instancias del editor de marcados

- Refactor de base de código menor

- Cambio de luz en color de acento

- Opciones de alineación del menú de la tarjeta de lienzo (plenty de opciones)

### Version 0.3.5 Configuration Update

- La documentación ahora tiene su propio sitio.
.

- opción de brillo suave para las partidas

- Añadido iconos de metadatos de arco iris

- Opciones de accesibilidad adicionales para el brillo, contraste y saturación global

- Added option to enable heading indicators globally, customisable for
different heading levels.

- Los indicadores de encabezado ahora mejor heredan del color base del encabezado

- opción agregada para configurar la duración de la animación popup callout

- opción agregada para configurar los contenedores de metadatos

### Version 0.3.4 Easter Egg Mode

- Made translation for hide until hover status bar configurable, useful for
longer status bars

- Trasfondo de explorador de archivos fijos roto

- opción de árbol de archivo marcado adicional para estilo de carpeta

- Añadido la lista de productos de metadatos

- Modo de huevo de Pascua reversible

### Version 0.3.3 QOL Update

- Added configurable indentation factor and dimming of collapsed headers for
Style Settings menu

- Added writing mode callout metadata utility, it increases text indent and
paragraph spacing

  - It also has a CSS class provider which allows you to apply the same text
  indent and paragraph spacing increments to the target note

- Add rhombus editor background option

- You can now use grid, dotted or rhombus as background options for the left
and right sidebar

- Estas opciones de url de fondo lateral izquierdo y derecho

- Cita ahora usa el mismo color que el arte ASCII

- La cita predeterminada se actualiza para no ser un rickroll

- Añadido soporte para plugin Kanban

- Añada antes de la nueva pestaña título de estado vacío ahora predeterminado a ninguno:

- Si usted está usando citas o arte ASCII, hacer re-enable it

- Ahora puede configurar el color de fondo para las citas o arte ASCII

- Los cambios pueden necesitar una recarga de la aplicación/restaurante para entrar en vigor

### Version 0.3.2 Animations

- Styling Ajustes a la tienda comunitaria, diseños existentes

- Las animaciones han vuelto, las opciones actuales incluyen:

- Diapositiva de izquierda a derecha

- Diapositiva en derecho a la izquierda

- Diapositiva en Top to Bottom

- Slide in Bottom to Top

- Girar en el fondo para arriba

- Girar en la derecha a la izquierda

- Diseño añadido y estilo de estado para Powerlevel10k

- Añadido servicio de metadatos de llamada de tarjetas flash

- opción agregada para añadir cotización personalizada antes del título de estado vacío

- No es seleccionable con el arte ASCII, el arte ASCII es seleccionado por defecto

- Added option to angle grid editor background

- Added background image option for modals (background image for settings,
prompts etc)

### Version 0.3.1 Tidying Up

- Servicios de metadatos adicionales para:

- cuadrícula y fondo abatido

- título y contenido itálico y oblicuo

- dashed, dotted, double, overline, underline and line-through for title and content

- Apply Heading 1 a 6 estilos para título

- peso de fuente para título y contenido

- Opciones de tamaño de fuente de encabezados adicionales

- Iconos sonrientes fijos (esperadamente por última vez)

- Opciones adicionales para añadir y configurar los fondos de imagen en las barras laterales izquierda y derecha

- Modificaciones de la luz a los elementos de navegación en la palanca, Calendario plugin de estilo

- Slight tweaks to editor background dotted and grid background styling.

- La barra de títulos se adapta ahora al estilo de diseño seleccionado

- opción agregada para desenfocar los nodos de Canvas inactivos para el plugin de Canvas núcleo

- Los cambios de fondo del editor ahora afectan el plugin de Canvas núcleo.
.

- Tal vez necesite volver a cargar / reiniciar para los cambios de configuración de estilo para aparecer en el Canvas

- Estilismo mojado de controles de tela y menú de tarjeta

- Cambia el estilo de las migas de pan para usar ASCII en lugar de emoji

### Version 0.3.0 TUI Layout

- Añadido TUI inspirado add-on al diseño de tarjetas

- Activado por defecto

- Cambios en el estilo de mesa

- Added cssclasses for heading indicators, callout metadata for tilting callout
title and content

- Añadido soporte para plugin de calendario

- Tweaked existing styling for Full Calendar plugin

- El estilo de la comunidad empapado

- Edición de alineación de iconos sonrientes fijos

- El diseño angosto se aplica a más elementos de la UI ahora

- Ahora debería ser más visible.

- Opciones de alineación rápida agregadas, configurando con ajustes de estilo:

- Arriba a la izquierda

- Topcenter

-Centerizquierda

- El fondo izquierdo

- Bottomcenter

-[See the documentation](../index.md) for more details

___

## Version 0.2.x

### Version 0.2.2 Layout styling

- Color de fondo de dobles comillas fijas

- Apoyo añadido para el plugin de estadísticas por defecto

- Tejidos menores para efectos de productos comunitarios

- Added card, angled options for workspace layout

- Necesidad de volver a cargar o reiniciar la aplicación si desea cambiar los diseños

- Vim mode status text and status bar mode (reading/live preview etc) text now
has a color option:

- Desactivado por defecto

- Añadir tarjeta, en ángulo (inspirado por Powerlevel10k) estilos para barra de estado

- Afecta el texto del estado del modo vim también

- Opciones de tamaño de la barra de estado añadido

### Version 0.2.1 Small Update

- Animaciones de ventana eliminadas ya que no son performant.
.

- Colores extendidos actualizados para que`*-color1-color2`y`*-color-2-color` will
always return the same color mix when using in callout metadata utilities.

- Efecto activo de fondo de archivos más consistente

- Añadido ASCII Art Line Highight opción

- Cssclasses añadidos para las opciones de fondo de editor de cuadrículas

- Opciones de estilo añadido para el título en línea

### Version 0.2.0 Aesthetics Update

- Añadido margen vertical de llamada, opción de radio fronterizo

- Opción de radio de la imagen agregada

- Added extended color palette (can be used as callout metadata utilities or in
css variables)

- Added popup callout, adapted from
[Ukiyo](https://github.com/technerium/obsidian-ukiyo)Tema de vaykinov y wizentex

- Opacidad fija de las principales acciones como nueva nota, nueva carpeta etc

- Added window animations for modals, prompts and settings.
Choose from the following options:

- Ninguna (Revierte al comportamiento predeterminado)

- Diapositiva hacia arriba

- Slide Up to Down

- Diapositiva izquierda a derecha

- Diapositiva derecha a izquierda

- También puede configurar la duración de la animación

- opción agregada para cambiar la visualización de propiedades en modo de lectura y modo de edición

- No mostrar propiedades en modo de lectura está habilitado por defecto

- No mostrar propiedades en modo de edición es deshabilitado por defecto

- opción agregada para permitir árboles minimalistas (carpeta/outline)

- carpetas de arco iris adicionales para el explorador de archivos

- Opciones de fondo dotted y grid

- Ver el[documentation](../index.md)para más detalles

___

## Version 0.1.x

### Version 0.1.1 Hotfixes

- opción agregada para cambiar el tamaño de la fuente ASCII

- Iconos sonrientes fijos en el móvil

- Nombre añadido y color de fondo metadatos

- Opciones adicionales para cambiar la visibilidad de las propiedades en modo de lectura y vista previa en vivo

- Añadido soporte para el plugin Dataview

- Puntos de bala arco iris añadidos (desactivados por defecto)

- Más elementos de la interfaz de usuario están reducidos para la consistencia

- Los medios de comunicación tienen ahora margen vertical que se puede establecer

### Version 0.1.0: Utilities Update

- Apoyo añadido para el enchufe de repetición espaciada

- Apoyo añadido para el enchufe de pan

- opción suplementaria adicional para partidas

- Efectos alternos del elemento activo en la configuración

- Opciones de personalización agregadas para los avisos

- Añadido estilo explorador de archivos alternativos

- Opciones adicionales para cambiar el color del enlace

- Cajas de verificación ASCII

- Servicios adicionales para llamadas

- No Icon

- No Título

- Antecedentes transparentes

- Capitalizar, mayúscula, minúscula Título y Contenido

- RTL, LTR,CenterTítulo y contenido

- Tategaki (RTL vertical)

- LTR vertical

- Cisclases adicionales para

- Tategaki (RTL vertical)

- LTR vertical

- Ver el[documentation](../index.md)para más detalles

Credits:

-`@OWA/bennyyip`sobre la discordia del grupo de miembros obisidianos para el tategaki

-`@Tuck`en la discordia del grupo de miembros obsidianos para opciones para cambiar el color de enlace

### Version 0.0.5: Minor Changes

- Hecho arte ASCII sensible, puede establecer un tamaño de fuente limiten él

- La barra de estado no se solapa con el texto de entrada del modo de comando

- opción adicional para habilitar la barra de estado en el móvil

- Opción de altura de línea agregada en tipografía para partidas

- Añadir opción para ocultar la cinta lateral izquierda

- Agregar opción para alinear las principales acciones a nivel mundial

