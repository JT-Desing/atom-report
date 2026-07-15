# Integración S3 de ATOM REPORT

Este backend busca cada cinco minutos el archivo compatible más reciente dentro de
`s3://epayco-atom-marketing/marketing/`, acepta CSV, JSON, JSONL, XLSX, XLSM y
Parquet, y genera `marketing/dashboard/atom_latest.json` para el dashboard.

## Despliegue

1. Instala AWS CLI y AWS SAM CLI en el equipo de infraestructura.
2. Usa un rol de despliegue autorizado; no copies claves dentro de este proyecto.
3. Desde esta carpeta ejecuta `sam build --use-container`.
4. Ejecuta `sam deploy --guided` y conserva los valores predeterminados.
5. Copia el output `AtomDataUrl` en `window.ATOM_DATA_ENDPOINT` de `config.js`.

Mientras no existan archivos compatibles, el proceso devuelve `waiting` y el
dashboard conserva los datos estáticos. Los archivos temporales o documentos con
otra extensión se ignoran.

## Contrato mínimo recomendado para ATOM

Los encabezados admitidos actualmente incluyen: `id_conversacion`,
`fecha_asignacion`, `hora_asignacion`, `horario_laboral`, `canal`, `tipo_origen`,
`grupo`, `agente`, `categoria`, `tipificacion`, `con_mensaje_agente`, `venta`,
`cumple_sla`, `tiempo_primera_respuesta` y `estado`.

La Function URL no contiene credenciales AWS, pero `AuthType: NONE` significa que
quien conozca la URL podría consultar el JSON. Antes de publicar datos personales,
debe sustituirse por autenticación corporativa (Cognito/CloudFront) o servir el
dashboard dentro de la red de ePayco.
