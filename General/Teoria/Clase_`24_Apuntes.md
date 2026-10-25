# =========================================
# SEGMENTO 22: GRAFOS PONDERADOS, KRUSKAL, DIJKSTRA Y CRIPTA 2
# =========================================

# Grafos Ponderados

Un grafo ponderado es un grafo donde cada arista tiene un **peso** (costo, distancia, tiempo). Se define como `G = {V, E, w}`, donde `w(a,b)` es el peso de la arista `(a,b)`.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Peso** | Valor numérico asociado a una arista | `w(A,B) = 5` |
| **Costo de un camino** | Suma de los pesos de sus aristas | `A -> B -> C` con pesos 5 y 3 cuesta 8 |
| **Camino mínimo** | Camino entre dos vértices con la menor suma de pesos | El de costo 8 frente a otro de costo 11 |
| **Camino con menos aristas** | No es lo mismo que el de menor costo | BFS lo encuentra solo si los pesos son uniformes |

* En una **matriz de adyacencia** se guarda el peso en lugar de `1` (y `0` o `∞` si no existe la arista).
* En una **lista de adyacencia** cada elemento guarda el vecino y el peso: `A -> (B, 5) -> (E, 2)`.

```python
# Lista de adyacencia ponderada
grafo = {
    "A": [("B", 5), ("E", 2)],
    "B": [("A", 5), ("D", 1)],
    "D": [("B", 1)],
    "E": [("A", 2)],
}
```

> BFS cuenta aristas, no pesos: cuando los costos no son uniformes, **contar salas no basta** para encontrar la ruta más barata.

## Árbol de expansión mínima (MST)

Dado un grafo **conexo**, no dirigido y ponderado, un **árbol de expansión** es un subgrafo que conecta todos los vértices, sin ciclos. El de **expansión mínima** es el que tiene la menor suma de pesos.

| Propiedad | Descripción |
|---|---|
| **Conecta todos los nodos** | Cualquier vértice alcanza a cualquier otro |
| **Sin ciclos** | Es un árbol |
| **Aristas** | Siempre `V - 1` (8 nodos → 7 aristas) |
| **Objetivo** | Minimizar el costo total de conexión |
| **No es un itinerario** | No sirve para visitar los nodos en orden ni da caminos mínimos entre pares |
| **Unicidad** | Si todos los pesos son distintos, el MST es único |
| **Si no es conexo** | No existe un árbol, se obtiene un bosque de expansión mínima |

* Usos: diseño de redes (cableado, tuberías, carreteras, redes de fibra) donde se quiere conectar todo con el menor costo.

### Propiedad de corte y de ciclo

| Propiedad | Enunciado | Consecuencia |
|---|---|---|
| **Corte** | Dado cualquier corte del grafo, la arista de menor peso que lo cruza pertenece a algún MST | Justifica que Kruskal y Prim aceptan la arista más barata segura |
| **Ciclo** | En cualquier ciclo, la arista de mayor peso no pertenece al MST (si es única) | Justifica descartar aristas que cierran ciclos |

### Algoritmo de Kruskal

Estrategia **voraz** (*greedy*): considera las aristas de menor a mayor peso y acepta cada una si no forma un ciclo.

| Paso | Qué se hace |
|---|---|
| **1** | Ordenar todas las aristas de menor a mayor peso |
| **2** | Comenzar con cada nodo en un componente separado |
| **3** | Aceptar la arista si une **dos componentes diferentes**; si sus extremos ya están conectados, descartarla porque produciría un ciclo |
| **4** | Detenerse al aceptar `V - 1` aristas |

```python
def kruskal(n, aristas):
    # aristas: lista de (peso, a, b)
    aristas.sort()
    padre = list(range(n))

    def find(x):
        while padre[x] != x:
            padre[x] = padre[padre[x]]   # compresión de caminos
            x = padre[x]
        return x

    mst, total = [], 0
    for peso, a, b in aristas:
        ra, rb = find(a), find(b)
        if ra != rb:                      # componentes distintos
            padre[ra] = rb                # unir
            mst.append((a, b, peso))
            total += peso
            if len(mst) == n - 1:
                break
    return mst, total
```

#### Estructura Union-Find (conjuntos disjuntos)

| Operación | Qué hace | Tiempo |
|---|---|---|
| `find(x)` | Devuelve el representante del componente de `x` | Casi O(1) |
| `union(a, b)` | Une los componentes de `a` y `b` | Casi O(1) |

* Con **compresión de caminos** y **unión por rango** el costo amortizado es `O(α(n))` (prácticamente constante).
* Permite saber si dos nodos ya están conectados, es decir, **detectar el ciclo**.

| Aspecto | Kruskal |
|---|---|
| **Estrategia** | Voraz, por aristas |
| **Complejidad** | `O(E log E)`, dominada por el ordenamiento |
| **Estructura clave** | Union-Find |
| **Mejor para** | Grafos dispersos |

### Algoritmo de Prim (alternativa)

| Aspecto | Descripción |
|---|---|
| **Estrategia** | Voraz, por vértices: crece un único árbol desde un nodo inicial |
| **Idea** | Agrega siempre la arista más barata que conecta el árbol con un vértice nuevo |
| **Estructura clave** | Cola de prioridad |
| **Complejidad** | `O(E log V)` con cola de prioridad |
| **Mejor para** | Grafos densos |

## Camino mínimo

Encontrar la ruta de **menor suma de pesos** entre vértices.

| Variante | Qué resuelve |
|---|---|
| **Origen único, un destino** | Camino mínimo de un vértice a otro |
| **Origen único, todos los destinos** | Distancias desde un vértice a todos los demás |
| **Todos los pares** | Distancias entre cualquier par de vértices |

### Algoritmo de Dijkstra

Encuentra un camino de menor suma de pesos entre un origen y un destino dentro del grafo considerado. **No exige visitar todos los nodos.**

| Requisito | Descripción |
|---|---|
| **Pesos finitos** | No se admiten pesos infinitos |
| **Pesos no negativos** | Con pesos negativos puede dar resultados incorrectos |
| **Estrategia** | Voraz: confirma siempre el nodo pendiente de menor distancia |

#### Procedimiento

| Paso | Qué se hace |
|---|---|
| **1** | Distancia provisional `0` para el origen e `∞` para los demás |
| **2** | Seleccionar, mediante la **cola de prioridad**, el nodo pendiente de menor distancia provisional y **confirmar** su valor |
| **3** | Para cada vecino, calcular una propuesta: `distancia(actual) + peso(arista)` |
| **4** | Si la propuesta es menor, actualizar la distancia y el **predecesor** del vecino (**relajación**) |
| **5** | Repetir hasta confirmar el destino o agotar los nodos alcanzables; reconstruir el camino siguiendo los predecesores en sentido inverso |

#### Estructuras que usa

| Estructura | Función |
|---|---|
| **Cola de prioridad** (`pendientes`) | Escoger el siguiente nodo de menor distancia provisional |
| **Distancias** | Mejores costos conocidos hasta el momento |
| **Predecesor** | Permite reconstruir el camino |
| **Confirmados** | Evita procesar de nuevo nodos ya resueltos |

* Un valor `inf` indica que **todavía no se ha encontrado un camino**, no una distancia física infinita.

```python
def dijkstra(grafo, origen, destino=None):
    INF = float("inf")
    distancias = {v: INF for v in grafo}
    predecesor = {v: None for v in grafo}
    distancias[origen] = 0
    pendientes = [(0, origen)]           # cola de prioridad (mín.)
    confirmados = set()

    while pendientes:
        d, u = extraer_minimo(pendientes)  # nodo de menor distancia provisional
        if u in confirmados:
            continue
        confirmados.add(u)               # distancia ya definitiva
        if u == destino:
            break
        for v, peso in grafo[u]:
            propuesta = d + peso
            if propuesta < distancias[v]:        # relajación
                distancias[v] = propuesta
                predecesor[v] = u
                insertar(pendientes, (propuesta, v))
    return distancias, predecesor

def reconstruir(predecesor, destino):
    camino = []
    while destino is not None:
        camino.append(destino)
        destino = predecesor[destino]
    return camino[::-1]
```

| Cola de prioridad | Complejidad |
|---|---|
| **Arreglo sin ordenar** | `O(V²)` |
| **Heap binario** | `O((V + E) log V)` |

#### Propiedades

| Propiedad | Descripción |
|---|---|
| **Correctitud** | Cuando un nodo se confirma, su distancia ya es la mínima (por eso no admite pesos negativos) |
| **Parada anticipada** | Si solo importa un destino, se detiene al confirmarlo |
| **Empates** | Si hay varias rutas de igual costo, se necesita una regla de desempate explícita para que el resultado sea determinista |
| **Con pesos uniformes** | Equivale a BFS |

### Otros algoritmos de camino mínimo

| Algoritmo | Qué resuelve | Pesos negativos | Complejidad |
|---|---|---|---|
| **BFS** | Origen único, pesos uniformes | No aplica | `O(V + E)` |
| **Dijkstra** | Origen único, pesos no negativos | No | `O((V + E) log V)` |
| **Bellman-Ford** | Origen único | Sí (detecta ciclos negativos) | `O(V · E)` |
| **Floyd-Warshall** | Todos los pares | Sí (sin ciclos negativos) | `O(V³)` |

## Comparación MST y camino mínimo

| Aspecto | Árbol de expansión mínima | Camino mínimo (Dijkstra) |
|---|---|---|
| **Pregunta** | ¿Cómo conecto todo al menor costo total? | ¿Cuál es la ruta más barata de A a B? |
| **Resultado** | Conjunto de `V - 1` aristas | Una secuencia de vértices |
| **Algoritmos** | Kruskal, Prim | Dijkstra, Bellman-Ford |
| **Dirigido** | No dirigido | Dirigido o no dirigido |
| **Visita todos los nodos** | Sí | No necesariamente |
| **Minimiza** | Suma de las aristas del árbol | Suma de las aristas del camino |
| **Ruta entre dos nodos dentro del resultado** | No es necesariamente la más corta | Es la más corta |

> El MST minimiza el costo de **conectar** todo; no garantiza que el camino entre dos nodos dentro del árbol sea el más barato.

## Resumen de grafos ponderados

| Idea | Resumen |
|---|---|
| **Grafo ponderado** | Cada arista tiene un peso |
| **Kruskal** | Ordena aristas, acepta las que unen componentes distintos (Union-Find), `V - 1` aristas |
| **Prim** | Crece un árbol desde un nodo con una cola de prioridad |
| **Dijkstra** | Camino mínimo con pesos no negativos, cola de prioridad, relajación y predecesores |
| **BFS** | Solo es camino mínimo si los pesos son uniformes |
| **Desempate** | Regla explícita para resultados deterministas |

# Proyecto 2: CRIPTA (Segunda parte)

Proyecto de Estructuras de Datos, II Ciclo 2026. Continúa sobre el repositorio de la primera parte.

| Aspecto | Definición |
|---|---|
| **Modalidad** | Los mismos grupos de la primera parte (hasta 4 personas) |
| **Lenguaje** | Python 3.11 o superior |
| **Metodología** | Desarrollo dirigido por especificaciones (SDD) con GitHub spec-kit |
| **Porcentaje** | 15% |
| **Uso de LLM** | Permitido, con bitácora obligatoria de prompts (incluye comandos de spec-kit) |
| **Entrega** | Miércoles 18 de noviembre |

> Regla editorial: las reglas del juego están especificadas; las decisiones de estructuras de datos no. Las especificaciones las escriben ustedes **antes** que el código.

## Las cuatro capacidades nuevas

| Capacidad | Qué agrega | Problema de estructuras de datos |
|---|---|---|
| **Terreno y cazadores** | Salidas con costo; enemigo que calcula la ruta más barata al jugador | Camino mínimo (Dijkstra) con desempate, rutas que dejan de ser válidas |
| **Niebla de guerra** | El jugador solo conoce lo explorado; comando «ir a» | Mapa conocido con consultas frecuentes y reversible |
| **Resolubilidad** | Verificar si la cripta puede ganarse y explicar por qué | Recorrido incremental, frontera bloqueada, ciclos de llaves |
| **Línea de tiempo** | Consultar el estado en cualquier instante pasado | Puntos de control cada K acciones y registro de cambios |

## Reglas nuevas

### Terreno y costo de las salidas

| Regla | Descripción |
|---|---|
| **Campo `costo`** | Entero mayor o igual que 1; por defecto 100; igual en ambos sentidos |
| **Costo de moverse** | El costo de la salida reemplaza al valor fijo 100 |
| **Intervalo** | `intervalo = max(1, costo_salida * 100 // velocidad)` |
| **Aplica a** | Todos los actores; atacar, esperar y demás acciones no cambian |

### El cazador

Cuarto comportamiento de enemigo, con campo `rango` (en unidades de costo). En su turno, en orden:

| Orden | Regla |
|:--:|---|
| **1** | Si comparte sala con el jugador, ataca |
| **2** | Si no, calcula el costo mínimo `d` hasta la sala del jugador usando solo salidas **abiertas** en ese instante |
| **3** | Si no hay ruta o `d > rango`, espera (costo 100) |
| **4** | Si existe, se mueve un paso por una ruta de costo `d` |

* **Desempate**: entre las vecinas `v` con `costo(u, v) + dist(v, jugador) = d`, se mueve a la de **menor id**.
* **Conocimiento**: conoce el esqueleto completo y el estado actual de las puertas; no le afecta la niebla; no abre puertas cerradas.
* **Equivalencia observable**: la decisión debe ser idéntica a calcular la ruta desde cero en ese instante. Se pueden reutilizar cálculos, pero nunca a costa de una decisión distinta.

### Niebla de guerra

| Estado de una sala | Cuándo | Qué conoce el jugador |
|---|---|---|
| **Explorada** | El jugador entró al menos una vez (la inicial desde el instante 0) | Nombre, salidas, costos y estado de puertas según la última observación |
| **Avistada** | Es destino de una salida de una sala explorada | Solo que existe una sala detrás |
| **Desconocida** | Ninguna de las anteriores | Nada |

* **Memoria de puertas**: el mapa recuerda el estado de cada puerta en su **última observación**, aunque haya cambiado.
* **Antorcha**: encendida, al entrar a una sala quedan exploradas todas sus vecinas (por cualquier salida); revela nombre y salidas, no contenido, y no activa enemigos ni trampas.
* **Separación**: el esqueleto completo es infraestructura (precarga); lo que muestra la vista y usa «ir a» debe derivarse **solo** del conocimiento del jugador.
* El conocimiento es **estado del juego**: se guarda, se revierte con el pergamino y forma parte de la línea de tiempo.

### Viaje automático: `ir a <sala>`

| Regla | Descripción |
|---|---|
| **Destino** | Debe ser una sala explorada; si no, se rechaza sin consumir tiempo |
| **Ruta** | Solo salas exploradas y salidas recordadas como abiertas; minimiza costo; desempate por menor id |
| **Pasos** | Cada paso es una acción completa del jugador y ocurren los eventos del reloj entre pasos |
| **Recalculo** | Se recalcula antes de cada paso con el conocimiento vigente |
| **Se detiene** | Llega al destino, entra a sala con enemigos (activos o dormidos), recibe daño o no queda ruta |
| **Puertas** | No abre puertas aunque tenga la llave |
| **Registro** | Cada paso es un movimiento en `partida.log`; `ir a` queda como comentario |
| **Pergamino** | Revierte solo el último paso y el viaje no continúa |

### Verificación de resolubilidad

| Aspecto | Descripción |
|---|---|
| **Supuestos** | Se atraviesa toda salida abierta o cerrada con llave ya obtenida; las llaves no se consumen; todo enemigo puede derrotarse; la llave de un enemigo está en su sala inicial; trampas y cierres automáticos no bloquean |
| **Resoluble** | Desde la sala inicial se obtiene `llave_salida` y se llega a `sala_salida` por una puerta que la requiere |
| **Si es resoluble** | Orden determinista de obtención de llaves (cada llave después de las necesarias) |
| **Si no lo es** | Llaves inalcanzables, puertas de la **frontera bloqueada** con la llave requerida, ubicación de cada llave y el **ciclo** de dependencia concreto |
| **Bandera `--verificar <cripta>`** | Solo ejecuta la verificación, sin vista |
| **Bandera `--forzar`** | Permite iniciar una cripta no resoluble |

### Línea de tiempo

| Aspecto | Descripción |
|---|---|
| **Independiente del pergamino** | El pergamino sigue limitado a 5 acciones |
| **Estado en el instante t** | Después de todos los eventos con tiempo ≤ t; si hay decisión del jugador en t, justo antes de tomarla |
| **Comandos** | `historia <t>` e `historia #k` (antes de la acción `k`); no consumen tiempo ni se registran |
| **Sin interacción** | `--replay partida.log --hasta <t>` |
| **Puntos de control** | Copias completas del estado, no más de una cada **K** acciones (`--checkpoint-cada K`) |
| **Reconstrucción** | Hacia adelante (re-simulando, con el estado de `random.Random`) o hacia atrás (invirtiendo cambios) |
| **Pergamino** | Las acciones revertidas dejan de existir en la línea |
| **Persistencia** | Conserva la línea completa; archivos de la primera parte se rechazan o migran de forma explícita |

## Cambios al servicio web

| Cambio | Detalle |
|---|---|
| **`costo` en salidas** | Campo nuevo; ausente equivale a 100 |
| **Cazador en el catálogo** | `comportamiento: "cazador"` y `rango` |
| **`GET /criptas/<id>/llaves`** | Ubicación de cada llave; con campo `enemigo` si la suelta un enemigo (sala = donde inicia) |
| **Presupuesto** | La consulta de llaves cuenta dentro de `presupuesto_solicitudes` |
| **Criptas no resolubles** | El servicio las publica; en la revisión se usará una cripta nueva |
| **Versiones nuevas** | Lo persistido de la primera parte se invalida con la validación de versión |

## Problemas de estructuras de datos

| Problema | Propiedades exigidas |
|---|---|
| **Ruta más barata del cazador** | Costo proporcional a la región dentro del rango; decidir entre cálculo individual o compartido con decenas de cazadores; desempate siempre |
| **Rutas que dejan de ser válidas** | Decisión igual a cálculo desde cero; identificar qué eventos invalidan qué; medir contra recalcular siempre |
| **Mapa conocido** | Consultas frecuentes; explorar cuesta según las salas reveladas; barato de registrar e invertir |
| **Resolubilidad** | Costo aproximadamente lineal en salas, salidas y llaves; frontera y dependencias salen del mismo recorrido; ciclos deterministas |
| **Línea de tiempo** | Consulta aplica o deshace ≤ K acciones; memoria crece con los cambios más un punto de control cada K; recortar al usar pergamino sin recorrer toda la historia |
| **Revisión de la primera parte** | Repetir mediciones con la carga nueva; cambiar y documentar lo que deje de ser adecuado |

## Restricciones de implementación

| Restricción | Detalle |
|---|---|
| **`dict` y `set`** | Prohibidos como índice o caché en los problemas evaluados |
| **Bibliotecas prohibidas** | `heapq`, `bisect`, `collections` (`deque`, `OrderedDict`, `defaultdict`, `Counter`), `networkx` y cualquier biblioteca de grafos o rutas |
| **Estructuras auxiliares** | De implementación propia (cola de prioridad, tablas de distancias, etc.) |
| **Herramientas de proceso** | spec-kit y el agente no pueden introducir dependencias prohibidas |

## Límites de rendimiento

| Operación | Límite | Condiciones |
|---|---|---|
| **Ciclo de eventos** | 20 ms | Cripta de referencia con decenas de cazadores activos |
| **Verificación de resolubilidad** | 200 ms | La cripta publicada más grande |
| **Consulta `historia`** | 50 ms | Partida de 5 000 acciones, K por defecto |
| **Un paso de «ir a»** | 5 ms | Mapa conocido completo de la cripta de referencia |

## Modo de medición (`--bench`)

| Medición | Qué compara |
|---|---|
| **Ruta del cazador** | Uno frente a muchos; rango pequeño frente a grande; cálculo compartido frente a individual |
| **Invalidación** | Reutilización frente a recálculo siempre, con puertas estables e inestables |
| **Mapa conocido y «ir a»** | Consultas y cálculo de rutas |
| **Resolubilidad** | Incremental frente a repetido por llave (criptas sintéticas con llaves encadenadas) |
| **Línea de tiempo** | Memoria y tiempo con al menos tres valores de K, y alternativa sin puntos de control |
| **Primera parte** | Mediciones repetidas con la carga nueva |

* Las criptas sintéticas deben ser deterministas por semilla.

# Spec-Kit (Desarrollo dirigido por especificaciones)

Spec Kit es un toolkit de código abierto que da a los agentes de programación **procesos estructurados, plantillas reutilizables y resultados documentados**. Su proceso principal es el **Spec-Driven Development (SDD)**: definir qué construir y por qué, y convertir la especificación en plan, tareas y código.

## Procesos disponibles

| Necesidad | Proceso | Resultado |
|---|---|---|
| **Construir una funcionalidad o aplicación** | Spec-Driven Development (en el núcleo) | Especificación llevada por planificación, implementación y convergencia |
| **Diagnosticar y reparar un comportamiento roto** | Bug fixing (extensión) | Causa evaluada, corrección acotada y verificación registrada |
| **Decidir si una idea merece inversión** | Idea assessment (extensión) | Decisión respaldada con evidencia: go, clarify o stop |
| **Adoptar o crear otro proceso** | Proceso propio | Proceso armado con primitivas reutilizables |

## Instalación

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify init --here --ai <agente>
```

| Requisito | Descripción |
|---|---|
| **Python** | 3.11 o superior |
| **uv** | Gestor para instalar la herramienta |
| **Agente de programación** | Claude Code, GitHub Copilot, Gemini CLI u otro compatible |
| **Versión fija** | Se registra en el README (todo el grupo usa la misma) |
| **Archivos generados** | `.specify/` y comandos del agente se versionan en el repositorio |

## Flujo obligatorio por capacidad

| Paso | Comando | Qué hace | Produce |
|:--:|---|---|---|
| **1** | `/speckit.constitution` | Una sola vez: principios del proyecto | `.specify/memory/constitution.md` |
| **2** | `/speckit.specify` | Qué debe hacer la capacidad y por qué (punto de vista del juego) | `specs/<NNN-nombre>/spec.md` |
| **3** | `/speckit.clarify` | Resuelve ambigüedades; las preguntas y respuestas quedan en la especificación | `spec.md` actualizada |
| **4** | `/speckit.plan` | Cómo se implementará: estructuras, módulos, mediciones previstas | `plan.md`, `research.md`, `data-model.md` |
| **5** | `/speckit.tasks` | Descompone el plan en tareas verificables | `tasks.md` |
| **6** | `/speckit.analyze` | Revisión de consistencia entre especificación, plan y tareas antes de implementar | Reporte de consistencia |
| **7** | `/speckit.implement` | Ejecución de las tareas (manual, con el agente o combinando ambos) | Código |

* En el README de Spec Kit el flujo base es: `constitution` → `specify` → `plan` → `tasks` → `implement` → `converge`, repitiendo `implement` y `converge` hasta que se reporte `Converged`.
* Como mínimo, una especificación por capacidad: terreno y cazador, niebla de guerra (con «ir a»), resolubilidad y línea de tiempo.

## Constitución del proyecto

| Principio | Descripción |
|---|---|
| **Estructuras a mano** | Prohibido `dict` como índice o caché y equivalentes de bibliotecas |
| **Determinismo** | Misma cripta, semilla y acciones producen la misma partida |
| **MVC** | `--replay` y `--bench` no instancian la vista |
| **Sin datos de una cripta en el código** | Nada concreto de una cripta escrito en el código |
| **Presupuesto** | Respetar `presupuesto_solicitudes` |
| **Rendimiento medido** | Toda afirmación se respalda con `--bench` |
| **Especificación primero** | Una especificación precede a su implementación |

* Los agentes leen la constitución en cada fase; si un plan o tarea la contradice, el error es del grupo, no del agente.

## ¿Qué va en cada artefacto?

| Artefacto | Contiene | No contiene |
|---|---|---|
| **`spec.md`** | Reglas del juego, historias de usuario, escenarios de aceptación, requisitos funcionales y de rendimiento numerados | Nombres de estructuras de datos, clases o módulos |
| **`plan.md`** | Estructuras elegidas, alternativas, complejidad esperada, módulos afectados, mediciones planificadas | Reglas nuevas que no estén en `spec.md` |
| **`tasks.md`** | Tareas pequeñas y verificables, con dependencias y requisito asociado | Tareas sin requisito asociado |

* El `plan.md` es el borrador de la sección correspondiente del **Documento de Decisiones**.

## Trazabilidad

| Elemento | Regla |
|---|---|
| **Requisito funcional** | Identificador estable (por ejemplo `FR-012`) |
| **Apéndice B** | Cada caso aparece como escenario de aceptación en alguna especificación |
| **Escenario de aceptación** | Al menos una prueba automatizada o un `partida.log` que lo ejercita, citando el requisito |
| **Tarea** | Referencia los requisitos que atiende |
| **Defensa** | Se escoge un requisito al azar: escenario → tarea → código → prueba |

## Historial, deriva y bitácora de LLM

| Regla | Descripción |
|---|---|
| **Especificación antes del código** | El historial de Git debe mostrar la especificación confirmada antes de los cambios de código |
| **Si la especificación estaba mal** | Se corrige primero la especificación y luego el código, en confirmaciones separadas |
| **Deriva** | Una especificación desactualizada respecto del programa entregado se penaliza |
| **Bitácora** | Cada comando de spec-kit con texto propio es un prompt a un LLM y se registra en `PROMPTS_LLM.md` |

## Extensiones, presets y flujos de trabajo (Spec Kit)

| Mecanismo | Para qué sirve |
|---|---|
| **Integration** | Conectar o cambiar de agente de programación |
| **Extension** | Agregar un comando, control de calidad o proceso completo |
| **Preset** | Adaptar plantillas, comandos o metodología; imponer estándares |
| **Workflow** | Automatizar prompts, comandos y tareas |
| **Bundle** | Instalar una configuración curada para un rol o equipo |
| **Catalog** | Descubrir componentes de la comunidad |

* Extensiones incluidas: `specify extension add bug` (corrección de errores) y `specify extension add assess` (evaluación de ideas).

# Entregables y evaluación del Proyecto 2

## Estructura mínima del repositorio

```
.specify/memory/constitution.md
specs/<NNN-capacidad>/spec.md
specs/<NNN-capacidad>/plan.md
specs/<NNN-capacidad>/tasks.md
DECISIONES.md
PROMPTS_LLM.md
README.md
```

| Documento | Contenido |
|---|---|
| **README** | Versión de spec-kit, agente utilizado, comandos nuevos (`--verificar`, `--forzar`, `--checkpoint-cada`, `--replay … --hasta`) y cómo ejecutar las pruebas de aceptación |
| **DECISIONES.md** | Una sección por problema: problema, alternativas, decisión, complejidad, evidencia empírica y límites; enlaza a spec y plan e indica si la decisión final coincide con el plan |
| **PROMPTS_LLM.md** | Bitácora de prompts, incluidos los comandos de spec-kit |

## Interfaz mínima

* Ver el mapa conocido.
* Ejecutar `ir a <sala>` y ver por qué se detuvo el viaje.
* Consultar la línea de tiempo con `historia <t>` e `historia #k`.
* Ver el reporte de resolubilidad al iniciar la partida.
* Mostrar los costos de las salidas de la sala actual y distinguir a los cazadores.

## Evaluación

| Rubro | Peso dentro del proyecto |
|---|:--:|
| **Especificaciones, constitución y proceso spec-kit** | 20 % |
| **Terreno, cazador e invalidación de rutas** | 20 % |
| **Niebla de guerra e «ir a»** | 10 % |
| **Verificación de resolubilidad** | 15 % |
| **Línea de tiempo y puntos de control** | 15 % |
| **Documento de Decisiones de Diseño** | 10 % |
| **Rendimiento** | 10 % |

## Defensa

* Se escoge un requisito al azar y se recorre su trazabilidad: escenario, tarea, código y prueba.
* Se pide un cambio pequeño a una regla: primero se modifica la especificación y luego el código.
* Cualquier integrante debe poder explicar cualquier especificación.

## Preguntas para arrancar (no se responden por escrito)

| Tema | Pregunta guía |
|---|---|
| **Cazadores** | Treinta cazadores persiguen al mismo jugador: ¿cuántas búsquedas hacen falta realmente por ciclo? |
| **Invalidación** | Una puerta se cierra lejos de todos los cazadores: ¿qué rutas siguen siendo válidas y cómo se sabe sin recalcular? |
| **Desempate** | ¿Qué diferencia hay entre encontrar *una* ruta y encontrar *la* ruta que exige el desempate? |
| **Antorcha** | ¿Qué información mínima se registra para revertir la exploración de cinco salas? |
| **Resolubilidad** | ¿Qué hace la verificación con las puertas que encontró cerradas antes de tener la llave? |
| **Puntos de control** | Con `K = 1` la consulta es instantánea y con `K` infinito no hay copias: ¿dónde está el punto razonable y cómo se mide? |
| **Spec-kit** | ¿Qué escribir en `spec.md` que un agente no pueda deducir del enunciado, y qué no debería escribirse allí? |
| **Dependencias** | Si el agente propone `heapq` en `plan.md`, ¿en qué fase se detecta y por quién? |
