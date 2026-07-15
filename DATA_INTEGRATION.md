# Integración de datos ATOM mediante S3

ATOM deposita sus archivos en `s3://epayco-atom-marketing/marketing/`. Una función
programada revisa esa ruta cada cinco minutos, selecciona el archivo compatible más
reciente y lo convierte a JSON. Una segunda función entrega ese JSON al dashboard
sin revelar credenciales del bucket.

Formatos aceptados: CSV, JSON, JSONL, XLSX, XLSM y Parquet.

## Comportamiento

- Si todavía no hay archivos, el dashboard conserva los datos estáticos.
- Un archivo nuevo se procesa como máximo cinco minutos después.
- El navegador consulta el endpoint automáticamente cada cinco minutos.
- Los formatos desconocidos se ignoran y se conserva el último resultado válido.
- El objeto normalizado se cifra en S3 y nunca se almacena en GitHub.

## Activación pendiente de infraestructura

El código está en `backend/`. Infraestructura debe desplegar `backend/template.yaml`
con AWS SAM y copiar el output `AtomDataUrl` en `config.js`. Las claves encontradas
en el archivo local no se utilizan ni se publican; el despliegue debe usar un rol IAM.

La URL sin autenticación solo es apropiada para datos agregados autorizados para
exposición. Si los reportes incluyen datos personales, clientes o conversaciones,
el acceso debe protegerse con Cognito/CloudFront o servirse en un entorno interno.

## Primera entrega

Cuando ATOM publique el primer archivo se debe validar una vez la equivalencia de
encabezados, fechas, booleanos y unidades. El contrato reconocido está documentado
en `backend/README.md`.
