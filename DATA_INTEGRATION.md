# Integración temporal de datos sin API

## Decisión recomendada

Usa GitHub Pages únicamente para la demostración. Para información real, sirve este mismo dashboard en la red interna y automatiza una exportación CSV de ATOM. Un sitio de GitHub Pages y cualquier CSV que descargue desde el repositorio deben considerarse públicos.

## Flujo temporal

1. Un equipo o servidor interno abre ATOM con una cuenta de solo lectura.
2. Una automatización de navegador (Playwright, Power Automate Desktop o UiPath) inicia sesión y descarga el reporte cada 5–15 minutos.
3. Un proceso local valida encabezados, zona horaria, duplicados y tipos de datos.
4. El archivo validado se guarda como `data/atom_latest.csv` en el servidor web interno.
5. El dashboard consulta ese archivo al abrir y cuando el usuario pulsa **Actualizar**.

## Por qué no hacer scraping desde GitHub Pages

El navegador no puede acceder de forma segura a una sesión autenticada de ATOM desde otro dominio por controles de origen, cookies y CORS. Incluir credenciales en JavaScript expondría la cuenta. Además, un workflow en GitHub con datos reales podría dejar los registros en artefactos, logs o historial Git.

## Puesta en marcha

1. Confirma con Seguridad/ATOM que la automatización de interfaz está permitida y crea una cuenta técnica de solo lectura con MFA gestionado.
2. Identifica el flujo estable: URL del reporte, filtros, botón de exportación y nombre del archivo descargado.
3. Ejecuta el robot en infraestructura interna, no en el navegador de cada usuario.
4. Conserva secretos en el almacén corporativo; nunca en el HTML, el CSV o el repositorio.
5. Antes de reemplazar el archivo, valida todos los campos y escribe primero a un archivo temporal para evitar lecturas parciales.
6. Registra fecha de extracción, número de filas, duración y error; alerta si la fuente lleva más de 20 minutos sin actualizarse.
7. Retén solo la ventana de datos necesaria y elimina PII que el dashboard no use.

## Camino preferido mientras llega la API

Si ATOM permite programar reportes por correo, SFTP o carpeta compartida, usa esa exportación antes que scraping. Es más estable, auditable y menos sensible a cambios visuales. Power Automate puede guardar el adjunto en SharePoint/OneDrive interno y un job puede publicarlo en el servidor interno.

## Paso final con API

Cuando exista la integración oficial, conserva el mismo esquema CSV/JSON como contrato de datos y cambia únicamente el colector. Valida oficialmente las fórmulas de SLA, primera respuesta, exclusión de bots, horario laboral y definición de venta.

