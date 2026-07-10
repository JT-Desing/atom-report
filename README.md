# ATOM REPORT

Sitio: https://jt-desing.github.io/atom-report/

Dashboard operativo de ATOM para responder cuatro preguntas: cómo está la operación, dónde está el cuello de botella, qué cambió y qué acción debe tomar el equipo.

## Uso

Abre `index.html` o visita GitHub Pages. La versión pública usa datos demostrativos. Para revisar una exportación real, pulsa **Cargar CSV**; el archivo se procesa dentro del navegador y no se sube al repositorio.

Campos esperados:

`id_conversacion`, `fecha_asignacion`, `hora_asignacion`, `horario_laboral`, `canal`, `tipo_origen`, `grupo`, `agente`, `grupo_tipificacion`, `tipificacion`, `categoria`, `con_mensaje_agente`, `venta`, `cumple_sla`, `tiempo_primera_respuesta`, `estado`.

La fecha debe usar `AAAA-MM-DD`. Los booleanos aceptan `true`, `1`, `sí`, `si`, `yes` o `cumple`.

## Datos automáticos

Si existe `data/atom_latest.csv`, el dashboard lo carga al pulsar **Actualizar**. No publiques datos personales u operativos en GitHub Pages. Consulta [DATA_INTEGRATION.md](DATA_INTEGRATION.md) para la arquitectura temporal recomendada.

## Tipografía

Incluye la familia web Davivienda suministrada para este proyecto en pesos regular, semibold y bold. Verifica que el uso y redistribución estén cubiertos por la licencia corporativa correspondiente.
