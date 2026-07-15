# ATOM REPORT

Sitio: https://jt-desing.github.io/atom-report/

Dashboard operativo de ATOM para entender el estado de la operación, detectar
cuellos de botella y priorizar acciones del equipo.

## Uso

Abre `index.html` o visita GitHub Pages. Mientras la integración no esté activa se
usan los datos estáticos de los reportes de ATOM. También es posible cargar un CSV
local; ese archivo se procesa dentro del navegador y no se sube al repositorio.

Campos esperados: `id_conversacion`, `fecha_asignacion`, `hora_asignacion`,
`horario_laboral`, `canal`, `tipo_origen`, `grupo`, `agente`, `tipificacion`,
`categoria`, `con_mensaje_agente`, `venta`, `cumple_sla`,
`tiempo_primera_respuesta` y `estado`.

## Integración S3

La conexión con `s3://epayco-atom-marketing/marketing/` está preparada en `backend/`.
Después de desplegarla con AWS SAM y configurar su URL en `config.js`, el dashboard
podrá leer automáticamente CSV, JSON, JSONL, Excel o Parquet enviados por ATOM.
Consulta [DATA_INTEGRATION.md](DATA_INTEGRATION.md) para el flujo y controles.

## Tipografía

Incluye la familia web Davivienda suministrada para este proyecto en pesos regular,
semibold y bold. Su uso debe estar cubierto por la licencia corporativa.
