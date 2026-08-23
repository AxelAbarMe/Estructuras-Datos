# Problemas de Estructuras de Datos
### Casos de alta complejidad inspirados en sistemas reales de producción

## Objetivo

Para cada escenario, diseñe una solución basada en estructuras de datos estudiadas en el curso y justifique su elección en función de las operaciones, restricciones y comportamiento requerido por el sistema.

## Instrucciones generales

- Modele los datos necesarios y defina con claridad las operaciones principales de su solución.
- Seleccione la estructura o combinación de estructuras que considere más apropiada. La elección debe justificarse técnicamente.
- Analice la complejidad temporal de las operaciones relevantes usando notación O grande.
- Explique al menos una alternativa que podría utilizarse y por qué sería menos conveniente bajo las restricciones del problema.
- Cuando el escenario incluya grandes volúmenes de datos, considere el impacto que tendría una operación lineal ejecutada repetidamente.
- ¿Puede utilizar pseudocódigo, diagramas o una implementación en el lenguaje indicado por el docente?

---

## Problema 1 - Gestión de solicitudes en un API Gateway
### Procesamiento ordenado, saturación y control de capacidad

Una plataforma de comercio electrónico recibe solicitudes desde múltiples aplicaciones móviles y web. Durante períodos normales procesa alrededor de 2 000 solicitudes por segundo, pero durante eventos promocionales puede alcanzar picos de 25 000 solicitudes por segundo.

Las solicitudes llegan a un API Gateway. El servicio encargado de procesarlas tiene un número limitado de workers; si todos están ocupados, las solicitudes aceptadas deben conservarse temporalmente hasta que exista capacidad de procesamiento.

Por razones funcionales, las solicitudes deben ser atendidas en el mismo orden en que fueron aceptadas por el Gateway. Una solicitud que llegó antes no puede ser adelantada por otra que llegó después.

#### Datos de cada solicitud

- `request_id`
- `client_id`
- `arrival_time`
- `operation`
- `payload_size`

#### Requisitos funcionales

1. Registrar una nueva solicitud pendiente.
2. Obtener la siguiente solicitud que debe ser procesada.
3. Consultar cuántas solicitudes se encuentran pendientes.
4. Rechazar nuevas solicitudes cuando se alcance un máximo configurable de elementos pendientes.
5. Registrar cuántas solicitudes fueron descartadas debido a saturación.
6. Simular la llegada de solicitudes y el procesamiento concurrente por parte de varios workers.

Durante una simulación de alta carga pueden existir cientos de miles de solicitudes pendientes. La solución no debe requerir desplazar masivamente elementos cada vez que una solicitud es procesada.

#### Preguntas de análisis

- ¿Qué estructura de datos utilizaría para almacenar las solicitudes pendientes? Justifique su respuesta.
- ¿Qué propiedad de la estructura permite conservar correctamente el orden de procesamiento?
- ¿Cuál es la complejidad de insertar una nueva solicitud y retirar la siguiente?
- ¿Qué impacto tendría sobre el rendimiento utilizar una representación que requiera desplazar todos los elementos después de cada operación?
- ¿Cómo afectaría a su diseño que la capacidad máxima pudiera modificarse dinámicamente durante la ejecución?

---

## Problema 2 - Priorización de incidentes de producción
### Severidad, SLA y cambios dinámicos de prioridad

Una empresa opera cientos de microservicios distribuidos en varios proveedores de nube. Su plataforma de observabilidad genera incidentes que deben ser atendidos por el equipo de Site Reliability Engineering.

#### Datos de cada incidente

- `incident_id`
- `service`
- `severity`
- `creation_time`
- `sla_deadline`
- `description`

La severidad puede tomar los valores **P1** (Critical), **P2** (High), **P3** (Medium) y **P4** (Low). El siguiente incidente a atender no depende únicamente de su hora de llegada.

La prioridad se determina, en este orden, por: severidad, tiempo restante antes de violar el SLA y hora de creación en caso de empate.

#### Ejemplo

| Incidente | Severidad | SLA |
|---|---|---|
| INC-105 | P3 | SLA en 40 minutos |
| INC-106 | P1 | SLA en 15 minutos |
| INC-107 | P2 | SLA en 5 minutos |
| INC-108 | P1 | SLA en 30 minutos |

El sistema debe soportar decenas de miles de incidentes activos y debe evitar ordenar nuevamente toda la colección cada vez que se inserta o se retira un incidente.

#### Operaciones requeridas

- `report_incident(incident)`
- `get_next_incident()`
- `peek_next_incident()`
- `pending_incidents()`

#### Cambio dinámico

Durante la vida de un incidente su prioridad puede cambiar. Por ejemplo, un incidente P3 puede convertirse posteriormente en P1 o su SLA puede acercarse al vencimiento mientras espera ser atendido.

#### Preguntas de análisis

- ¿Qué estructura de datos utilizaría y cuál sería la clave o criterio de comparación entre elementos?
- ¿Cómo garantiza su diseño que el siguiente elemento seleccionado sea siempre el más urgente según las reglas definidas?
- ¿Por qué ordenar completamente todos los incidentes después de cada inserción sería costoso?
- Analice la complejidad de insertar, consultar y retirar el siguiente incidente.
- Proponga una estrategia para manejar cambios de prioridad sin reconstruir completamente la colección.

---

## Problema 3 - Rollback automático de un despliegue
### Operaciones compensatorias, anidamiento y recuperación después de fallos

Una plataforma interna realiza despliegues automatizados de aplicaciones. Cada despliegue está compuesto por una secuencia de operaciones que modifican infraestructura o configuración.

#### Ejemplos de operaciones

1. Crear una nueva configuración
2. Cambiar una variable de entorno
3. Actualizar la imagen del contenedor
4. Modificar una regla de red
5. Actualizar un secreto
6. Cambiar el tráfico hacia la nueva versión

Cada operación exitosa tiene asociada una operación compensatoria capaz de revertir su efecto.

#### Ejemplos de compensación

```
crear_config("v2")     -> eliminar_config("v2")
set_image("app:v2")    -> set_image("app:v1")
set_traffic(100,0)     -> set_traffic(0,100)
create_route("api-v2") -> delete_route("api-v2")
```

Considere que un despliegue ejecuta A, B, C y D correctamente, pero E falla. Para recuperar el estado anterior, las operaciones exitosas deben revertirse comenzando por la última que modificó el sistema y continuando hasta la primera.

```
A completada
B completada
C completada
D completada
E ERROR
```

**Orden de recuperación requerido:** D, C, B, A

Algunas operaciones pueden contener suboperaciones. Si una suboperación falla, primero deben revertirse los cambios realizados dentro de esa operación antes de continuar con los cambios externos.

#### Operaciones requeridas

- `execute(operation)`
- `rollback()`
- `rollback_all()`

Únicamente deben registrarse operaciones que hayan terminado exitosamente. Adicionalmente, el sistema podría reiniciarse inmediatamente después de un error, por lo que debe plantearse una estrategia para persistir el estado mínimo necesario y continuar la recuperación después del reinicio.

#### Preguntas de análisis

- ¿Qué estructura representa de forma natural el orden de recuperación requerido?
- ¿Por qué es importante revertir las operaciones en orden inverso al de su ejecución?
- ¿Qué información mínima almacenaría por cada operación completada?
- Determine la complejidad de registrar una operación exitosa y revertir la última operación.
- ¿Cómo adaptaría el diseño para soportar operaciones anidadas y recuperación después de un reinicio?

---

## Problema 4 - Administrador de bloques libres de memoria
### Asignación dinámica, división de bloques y fusión de regiones contiguas

Un servidor procesa grandes cantidades de mensajes provenientes de clientes. Para reducir el costo de solicitar memoria continuamente al sistema operativo, la aplicación reserva inicialmente un bloque de 1 GiB y administra internamente ese espacio.

El administrador debe mantener un registro de las regiones actualmente disponibles. El número de regiones libres cambia constantemente durante la ejecución.

#### Ejemplo de estado

| Address | Size |
|---|---|
| 0x00200000 | 4 MiB libres |
| 0x02000000 | 12 MiB libres |
| 0x08000000 | 2 MiB libres |
| 0x10000000 | 30 MiB libres |

#### Operaciones requeridas

- `allocate(size)`
- `release(address, size)`
- `dump_free_blocks()`

Para `allocate(size)` se utilizará inicialmente una estrategia **First Fit**: se recorre la estructura desde el inicio y se selecciona la primera región suficientemente grande.

Si una región de 20 MiB recibe una solicitud de 8 MiB, los 8 MiB iniciales pasan a estar ocupados y los 12 MiB restantes deben continuar registrados como espacio libre.

Cuando una región es liberada, debe agregarse nuevamente a la estructura. Las regiones libres se mantendrán ordenadas por dirección de memoria. Si dos regiones libres son adyacentes, deben fusionarse en una única región de mayor tamaño.

#### Restricciones

- No existe un número máximo conocido de regiones libres.
- Las regiones pueden aparecer, dividirse, fusionarse y desaparecer continuamente.
- La representación elegida debe permitir modificar la colección sin copiar de forma innecesaria grandes cantidades de elementos.

#### Preguntas de análisis

- Seleccione una estructura apropiada para representar las regiones libres y justifique su elección.
- Explique cómo implementaría `allocate(size)` usando First Fit.
- Explique cómo implementaría `release(address, size)`, incluyendo la fusión de regiones contiguas.
- Analice la complejidad de búsqueda, inserción y eliminación.
- ¿En qué escenarios su solución comenzaría a ser poco eficiente y qué característica del patrón de acceso causaría el problema?

---

## Problema 5 - Scheduler distribuido de tareas con reintentos
### Trabajos disponibles, exponential backoff y temporización eficiente

Una plataforma procesa trabajos asíncronos como generar facturas, enviar correos, procesar imágenes, generar reportes, sincronizar usuarios y procesar pagos.

Cuando un trabajo nuevo llega y existen workers disponibles, puede ejecutarse inmediatamente. Si hay varios trabajos listos, deben respetar el orden en que quedaron disponibles para procesamiento.

Sin embargo, un trabajo puede fallar. Cuando esto ocurre no debe ejecutarse inmediatamente otra vez: se aplica **exponential backoff**.

#### Política de reintentos

```
Intento 1 -> esperar 5 segundos
Intento 2 -> esperar 10 segundos
Intento 3 -> esperar 20 segundos
Intento 4 -> esperar 40 segundos
```

#### Datos adicionales para trabajos fallidos

- `job_id`
- `attempts`
- `next_execution_time`
- `payload`

#### Ejemplo

**Hora actual: 10:00:00**

| Job | Ejecutar nuevamente |
|---|---|
| A | 10:00:25 |
| B | 10:00:07 |
| C | 10:00:40 |
| D | 10:00:12 |

El scheduler debe determinar eficientemente cuál es el próximo trabajo cuyo período de espera ha terminado. Una vez alcanzado `next_execution_time`, dicho trabajo vuelve al conjunto de trabajos disponibles para los workers.

Con cientos de miles de trabajos, no se permite recorrer todos los trabajos fallidos cada segundo para determinar cuáles pueden volver a ejecutarse.

#### Operaciones requeridas

- `submit(job)`
- `get_next_job()`
- `job_failed(job)`
- `process_retries(current_time)`

#### Preguntas de análisis

- ¿Puede una sola estructura resolver eficientemente todas las necesidades del sistema? Justifique.
- ¿Qué estructura utilizaría para los trabajos que ya están disponibles para ejecución?
- ¿Qué estructura utilizaría para los trabajos que permanecen esperando hasta una hora futura?
- ¿Cuál debería ser la clave utilizada para organizar los trabajos en espera?
- Analice la complejidad de las operaciones principales.
- Explique cómo `process_retries(current_time)` puede determinar qué trabajos están listos sin recorrer toda la colección.
