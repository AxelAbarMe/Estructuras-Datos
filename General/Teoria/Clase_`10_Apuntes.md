# CRIPTA 

## 1. Idea General (Notas de texto)

- **Mapa grande**, no necesariamente una matriz — son salas conectadas entre sí.
- El personaje (PJ) debe **escapar de la Cripta**; cada cuarto tiene conexiones con otros cuartos, algunos con puertas que pueden bloquear.
- **PJ, enemigos y objetos** tienen HP y Velocidad.
- Al entrar a un cuarto, el jugador puede **elegir una acción**.
- Qué enemigo ataca primero **depende de la velocidad** (no es por turnos fijos).
- **Inventario navegable** (Pociones, llaves, etc.).
- **Objeto especial: pergamino de retroceso** — permite retroceder *n* pasos, regresa como un *checkpoint* al pasado y reinicia el estado anterior del juego (incluye resetear al personaje).
- **Enemigos con 3 tipos de movimiento**:
  - **Olfato**: se acerca solo si tiene visión del jugador.
  - **Random**: movimiento aleatorio.
  - **Estático**: no se mueve (guardián).
- **Interfaz**: patrón Modelo/Vista/Controlador; parte gráfica opcional con **Pygame/Arcade**.
- **API en AWS**: al iniciar el juego se hace un *query* al API que devuelve un JSON con todos los mapas disponibles; con el ID de un mapa se pide otro JSON con su información específica; para las salas (*rooms*) se hace otro *query* para obtener su JSON.
- **Máximo de Requests al API: 20** (por partida/cripta).
- Se debe poder **guardar el proyecto offline**, con backups en archivos JSON.

---

## 2. Guía Visual (Pizarra)

El diagrama de pizarra resume el flujo de datos y la arquitectura:

- **API** ⇄ Programa: se hacen *queries* (`/maps`, `/maps/{id}`, `/maps/{id}/room/{id}`) y el API responde con **JSON** (mapas, contenido de sala).
- El **grid/mapa** dibujado representa una sala con: **Health**, **Velocidad**, actores (número `2`), enemigos con distintos íconos, y un **inventario** (con opción de **retroceso**).
- **Enemigos**: se comportan según **Olfato**, **Random** o **Estático**; tienen **Health** y **Velocidad**.
- **Objetos**: parte del inventario del jugador.
- **Vista/Controlador**: se implementa con **Pygame/Arcade**, y debe soportar **modo Offline** (guardar JSON localmente).
- **Github**: se debe entregar un **README.md** con la justificación del proyecto y un **requirements.txt**.

---

## 3. Expansión Técnica (según el enunciado oficial en PDF)

Estas notas de clase corresponden, en términos formales del proyecto **CRIPTA**, a lo siguiente:

| Nota de pizarra/texto | Concepto técnico real en el enunciado |
|---|---|
| "Mapa grande, no una matriz" | Grafo de salas conectadas por salidas N/S/E/O (§2.1) |
| "Cada cuarto puede tener puertas bloqueadas" | Puertas cerradas con llave, posible cierre automático (§2.1, §2.5) |
| "Qué enemigo ataca depende de velocidad" | No hay turnos: hay un **reloj virtual** con eventos programados por `tiempo_siguiente`, resuelto con `intervalo = max(1, costo*100 // velocidad)` (§2.3) |
| "Elegir acción al entrar a un cuarto" | Costo de acciones: moverse=100, atacar=100, esperar=100, usar objeto=50, equipar=50, recoger/soltar=25, abrir puerta=50 (§2.3) |
| "Pergamino de retroceso" | Operación de **deshacer** el estado completo (no copias completas), máx. 5 acciones, excluye el propio pergamino de la reversión (§2.11, §4.6) |
| "3 tipos de movimiento: Olfato, Random, Estático" | Comportamientos de enemigo: **Rastreador** (sigue rastro fresco <400 unidades), **Errante** (movimiento aleatorio), **Guardián** (nunca se mueve) (§2.8, §2.9) |
| "Inventario navegable" | Debe recorrerse adelante/atrás, soltar en O(1) sin importar posición, vista ordenada por peso/valor/nombre sin alterar el orden real (§4.5) |
| "API en AWS, JSON de mapas" | Servicio REST real: `GET /criptas`, `GET /criptas/{id}`, `GET /criptas/{id}/salas`, `GET /criptas/{id}/contenido`, `GET /catalogo` (§3.3) |
| "Máximo 20 requests" | En realidad el límite es **variable por cripta** (`presupuesto_solicitudes`), no un número fijo quemado en código (§3.3, §5.1) |
| "Guardar offline en JSON" | Modo `--offline` que lee un paquete de respuestas pregrabadas con el mismo contrato lógico que la red (§3.4); además guardado binario propio del estado de partida (§4.10) |
| "Modelo Vista/Controlador con Pygame/Arcade" | Arquitectura MVC obligatoria + Adaptadores de red/disco; `--replay` y `--bench` deben correr sin instanciar la vista (§6) |

### Restricciones clave que no aparecen en las notas pero son obligatorias
- **Prohibido usar `dict`** como índice/caché/tabla de búsqueda para los problemas evaluados (§7); las estructuras deben implementarse a mano.
- **Prohibido `list.sort()`/`sorted()`** para los ordenamientos evaluados; deben implementarse al menos 2 algoritmos y elegir cuál usar según los datos (§4.9).
- Toda aleatoriedad debe usar `random.Random(semilla)` propio, nunca el generador global (§2.6).
- Cada request HTTP debe incluir el header `X-Cripta-Client-Id` (un UUID generado una vez por ejecución).
- El **Documento de Decisiones de Diseño** es obligatorio: problema, alternativas, decisión, complejidad, evidencia empírica con `--bench`, límites conocidos (§8).
- Bitácora de prompts de LLM (`PROMPTS_LLM.md`) obligatoria si se usa IA (§10.3).
