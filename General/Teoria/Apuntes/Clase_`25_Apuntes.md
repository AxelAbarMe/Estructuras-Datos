# =========================================
# SEGMENTO 23: SPEC-DRIVEN DEVELOPMENT (SDD) Y SPEC KIT
# =========================================

# Desarrollo dirigido por especificaciones (SDD)

El **Spec-Driven Development (SDD)** es una metodología donde la **especificación** es el artefacto principal y el código es su resultado. Primero se define **qué** se quiere construir y **por qué**; después se decide **cómo**, y solo al final se genera el código.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Especificación** | Descripción del comportamiento esperado, sin detalles técnicos | «Un usuario puede crear un libro y recibe su identificador» |
| **Plan** | Decisiones técnicas que cumplen la especificación | Lenguaje, estructuras, módulos, contratos |
| **Tareas** | Pasos pequeños y verificables derivados del plan | «Crear el modelo `Libro` y su prueba» |
| **Implementación** | Código producido a partir de las tareas | Archivos fuente y pruebas |
| **Fuente de verdad** | El documento que manda cuando hay dudas | La especificación, no el código |

* En el desarrollo tradicional el código manda y la documentación queda atrás; en SDD **la especificación manda** y el código se deriva de ella.
* Es especialmente útil al trabajar con **agentes de programación (LLM)**: un prompt vago produce código impredecible, mientras que una especificación clara produce resultados verificables.

> Un error en la especificación se convierte en un error en el código. Por eso se revisa cada documento **antes** de pasar a la siguiente fase.

## ¿Por qué importa el SDD?

| Problema del desarrollo sin especificación | Cómo lo atiende el SDD |
|---|---|
| **El agente adivina** requisitos que no se dijeron | Los requisitos quedan escritos y se aclaran antes de programar |
| **Decisiones técnicas mezcladas con reglas del producto** | `spec.md` (qué) se separa de `plan.md` (cómo) |
| **No se sabe por qué el código hace lo que hace** | Cada decisión queda documentada y enlazada a un requisito |
| **Cambios que rompen lo anterior** | Los principios del proyecto se aplican en todas las fases |
| **Resultados distintos en cada intento** | Entradas estructuradas generan salidas más consistentes |
| **Código sin pruebas ni criterio de aceptación** | Cada escenario de aceptación se convierte en tarea y en prueba |

| Aspecto | Sin SDD | Con SDD |
|---|---|---|
| **Punto de partida** | Prompt libre al agente | Especificación revisada |
| **Documentación** | Se escribe al final (o nunca) | Se escribe primero y guía el código |
| **Revisión** | Solo del código | De especificación, plan, tareas y código |
| **Cambios de regla** | Se edita el código directamente | Se edita la especificación y luego el código |
| **Trazabilidad** | Difícil de reconstruir | Requisito → tarea → código → prueba |

## Principios del SDD

| Principio | Descripción |
|---|---|
| **Qué antes que cómo** | La especificación describe el comportamiento, no la tecnología |
| **Intención explícita** | Lo que no se escribe, el agente lo deduce (y puede deducirlo mal) |
| **Ambigüedad resuelta temprano** | Se aclaran las dudas antes de planificar |
| **Revisión humana en cada fase** | El agente propone; las personas validan |
| **Verificabilidad** | Todo requisito debe poder comprobarse con una prueba o escenario |
| **Iteración** | Si algo falla, se corrige primero el documento y luego el código |

# Spec Kit

**Spec Kit** es un toolkit de código abierto de GitHub que da a los agentes de programación **procesos estructurados, plantillas reutilizables y resultados documentados**. Su proceso principal es el SDD: convierte una especificación en un plan, el plan en tareas y las tareas en código.

| Aspecto | Descripción |
|---|---|
| **Qué es** | Conjunto de plantillas, comandos y scripts para trabajar con SDD |
| **Cómo se usa** | Mediante la herramienta de línea de comandos `specify` y comandos `/speckit.*` dentro del agente |
| **Quién escribe el código** | El agente de programación, guiado por los documentos que genera Spec Kit |
| **Qué produce** | Documentos en Markdown versionables junto con el código |
| **Código abierto** | Repositorio oficial: `github.com/github/spec-kit` |

> Spec Kit **no programa por sí mismo**: organiza el proceso y las plantillas para que el agente trabaje con contexto claro.

## Procesos disponibles

| Necesidad | Proceso | Resultado |
|---|---|---|
| **Construir una funcionalidad o aplicación** | Spec-Driven Development (en el núcleo) | Especificación llevada por planificación, implementación y convergencia |
| **Diagnosticar y reparar un comportamiento roto** | Bug fixing (extensión) | Causa evaluada, corrección acotada y verificación registrada |
| **Decidir si una idea merece inversión** | Idea assessment (extensión) | Decisión respaldada con evidencia: go, clarify o stop |
| **Adoptar o crear otro proceso** | Proceso propio | Proceso armado con primitivas reutilizables |

## Requisitos

| Requisito | Descripción |
|---|---|
| **Python** | 3.11 o superior |
| **uv** | Gestor de paquetes y herramientas de Python; instala `specify` |
| **Git** | Spec Kit crea un repositorio y una rama por funcionalidad |
| **Agente de programación** | Claude Code, GitHub Copilot, Gemini CLI u otro compatible |
| **Node.js** | Solo si el agente se distribuye por npm (por ejemplo, Gemini CLI) |
| **Terminal** | Bash en Linux/macOS; CMD o PowerShell en Windows |

## Instalación

```bash
# Instalar la herramienta desde el repositorio oficial, con versión fija
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
uv tool update-shell

# Verificar
specify version
specify check
```

| Paso | Qué se hace | Para qué |
|:--:|---|---|
| **1** | Instalar Git, Python, uv y (si aplica) Node.js | Tener los requisitos |
| **2** | Instalar y autenticar el agente de programación | Que pueda ejecutar los comandos `/speckit.*` |
| **3** | `uv tool install specify-cli --from git+...@vX.Y.Z` | Instalar `specify` en una versión concreta |
| **4** | `uv tool update-shell` | Agregar la herramienta al `PATH` |
| **5** | Cerrar y reabrir la terminal | Que el `PATH` se recargue |
| **6** | `specify version` y `specify check` | Confirmar que todo está instalado |

* **Siempre se fija la versión** (`@vX.Y.Z`) para que todas las personas del equipo usen la misma y los resultados sean reproducibles.
* Se instala desde el **repositorio oficial de GitHub**; los paquetes con nombre similar en PyPI no son el Spec Kit oficial.
* En **Windows**, los scripts auxiliares son de PowerShell; puede ser necesario permitir su ejecución una vez:

```bash
powershell -Command "Set-ExecutionPolicy -Scope CurrentUser RemoteSigned"
```

| Problema común | Causa probable | Solución |
|---|---|---|
| `specify` no se reconoce | El `PATH` no se recargó | Cerrar y reabrir la terminal; ejecutar `uv tool update-shell` |
| Los comandos `/speckit.*` no aparecen | Integración mal instalada o agente abierto en otra carpeta | Reiniciar el agente dentro de la carpeta del proyecto |
| Error de límite de solicitudes (403) al inicializar | Límite de la API de GitHub | Esperar o autenticarse con un token de GitHub |
| Scripts `.ps1` bloqueados | Política de ejecución de PowerShell | Permitir scripts locales para el usuario |

## Inicializar un proyecto

```bash
specify init <nombre-proyecto> --integration <agente> --script ps
# o dentro de una carpeta existente:
specify init --here --integration <agente>
```

| Opción | Qué hace |
|---|---|
| **`<nombre-proyecto>`** | Crea una carpeta nueva con la estructura de Spec Kit |
| **`--here`** | Inicializa en la carpeta actual |
| **`--integration <agente>`** | Instala los comandos para el agente elegido (`claude`, `copilot`, `gemini`, etc.) |
| **`--script ps` / `--script sh`** | Usa scripts auxiliares de PowerShell o de Bash |

* Versiones anteriores usaban la opción `--ai`; las actuales usan `--integration`.
* Inicializar también crea un repositorio Git si no existe.

### Estructura generada

```
proyecto/
├── .specify/
│   ├── memory/
│   │   └── constitution.md      ← principios del proyecto
│   ├── scripts/                 ← scripts auxiliares (ps / sh)
│   └── templates/               ← plantillas de spec, plan y tasks
├── .<agente>/commands/          ← comandos /speckit.* del agente
└── specs/
    └── 001-nombre/              ← se crea con /speckit.specify
        ├── spec.md
        ├── plan.md
        ├── research.md
        ├── data-model.md
        ├── contracts/
        └── tasks.md
```

| Carpeta o archivo | Función |
|---|---|
| **`.specify/memory/`** | Memoria permanente del proyecto (la constitución) |
| **`.specify/templates/`** | Plantillas que el agente rellena en cada fase |
| **`.specify/scripts/`** | Automatizan ramas, rutas y verificaciones |
| **`.<agente>/commands/`** | Definición de los comandos que el agente reconoce |
| **`specs/<NNN-nombre>/`** | Una carpeta por funcionalidad, numerada |

* `.specify/` y los comandos del agente **se versionan** en el repositorio.

## Flujo de trabajo

El proceso se ejecuta **en orden**, dentro del agente. Cada fase produce un documento que se **lee y corrige** antes de pasar a la siguiente.

| Paso | Comando | Qué hace | Produce |
|:--:|---|---|---|
| **1** | `/speckit.constitution` | Una sola vez: define los principios del proyecto | `.specify/memory/constitution.md` |
| **2** | `/speckit.specify` | Describe **qué** debe hacer la funcionalidad y **por qué** | `specs/<NNN-nombre>/spec.md` |
| **3** | `/speckit.clarify` | Detecta ambigüedades y las resuelve con preguntas | `spec.md` actualizada |
| **4** | `/speckit.plan` | Define **cómo** se implementará: tecnología, estructuras, módulos | `plan.md`, `research.md`, `data-model.md`, `contracts/` |
| **5** | `/speckit.tasks` | Descompone el plan en tareas verificables | `tasks.md` |
| **6** | `/speckit.analyze` | Revisa la consistencia entre especificación, plan y tareas | Reporte (no modifica archivos) |
| **7** | `/speckit.implement` | Ejecuta las tareas y genera el código y las pruebas | Código |

* En el README de Spec Kit, el flujo base es: `constitution` → `specify` → `plan` → `tasks` → `implement` → `converge`, repitiendo `implement` y `converge` hasta que se reporte `Converged`.
* `/speckit.specify` crea una **rama de Git** nueva por funcionalidad (por ejemplo, `001-nombre`).
* Se recomienda **hacer una confirmación (commit) después de cada fase** para ver cómo evolucionan los documentos.

### Qué hace cada fase y por qué existe

| Fase | Propósito | Error que evita |
|---|---|---|
| **Constitución** | Fijar reglas que valen para todo el proyecto | Decisiones inconsistentes entre funcionalidades |
| **Especificación** | Poner por escrito el comportamiento esperado | Que el agente invente requisitos |
| **Clarificación** | Convertir dudas en decisiones registradas | Ambigüedades que se vuelven errores |
| **Plan** | Elegir y justificar la solución técnica | Mezclar reglas de negocio con tecnología |
| **Tareas** | Dividir el trabajo en pasos pequeños y comprobables | Cambios enormes difíciles de revisar |
| **Análisis** | Detectar contradicciones y huecos antes de programar | Descubrir inconsistencias cuando ya existe el código |
| **Implementación** | Producir el código siguiendo las tareas | Código sin relación con los requisitos |

## Constitución del proyecto

La **constitución** es un documento con los principios no negociables del proyecto. Se escribe una sola vez y los agentes la **leen en cada fase**.

| Tipo de principio | Ejemplos |
|---|---|
| **Calidad de código** | Estilo, tipado, estructura de módulos |
| **Pruebas** | Cobertura mínima, pruebas antes o junto con el código |
| **Dependencias** | Bibliotecas permitidas y prohibidas |
| **Arquitectura** | Separación de capas, patrones obligatorios |
| **Rendimiento y seguridad** | Límites medibles, manejo de secretos |
| **Proceso** | Especificación antes del código, confirmaciones por fase |

* Si un plan o una tarea contradice la constitución, el error es de quien revisó, no del agente.
* Sirve para que una segunda funcionalidad sea **consistente** con la primera sin repetir las reglas.

## ¿Qué va en cada artefacto?

| Artefacto | Contiene | No contiene |
|---|---|---|
| **`constitution.md`** | Principios y restricciones del proyecto | Requisitos de una funcionalidad concreta |
| **`spec.md`** | Historias de usuario, escenarios de aceptación, requisitos funcionales numerados, casos límite | Nombres de tecnologías, clases o módulos |
| **`plan.md`** | Tecnología elegida, alternativas, estructura del proyecto, decisiones | Reglas nuevas que no estén en `spec.md` |
| **`research.md`** | Investigación y justificación de decisiones técnicas | Requisitos del producto |
| **`data-model.md`** | Entidades, campos y relaciones | Código de implementación |
| **`contracts/`** | Interfaces externas (por ejemplo, definición de endpoints) | Lógica interna |
| **`tasks.md`** | Tareas pequeñas, ordenadas y verificables, con dependencias | Tareas sin requisito asociado |

### Estructura de una buena especificación

| Sección | Función |
|---|---|
| **Historias de usuario** | Describen qué quiere lograr la persona usuaria |
| **Escenarios de aceptación** | Formato «dado / cuando / entonces» que se puede comprobar |
| **Requisitos funcionales** | Lista numerada con identificadores estables (`FR-001`, `FR-002`…) |
| **Casos límite** | Entradas inválidas, vacíos, duplicados, errores |
| **Criterios de éxito** | Resultados medibles que indican que la funcionalidad está lista |
| **Clarificaciones** | Preguntas y respuestas registradas por `/speckit.clarify` |

```markdown
### Escenario de aceptación
- **Dado** un recurso que no existe
- **Cuando** se solicita por su identificador
- **Entonces** el sistema responde con un error de «no encontrado»

**FR-004**: El sistema DEBE rechazar solicitudes con campos obligatorios vacíos.
```

> `spec.md` responde **qué** y **por qué**; `plan.md` responde **cómo**. Mezclarlos es el error más frecuente.

## Trazabilidad

| Elemento | Regla |
|---|---|
| **Requisito funcional** | Tiene un identificador estable que no cambia |
| **Escenario de aceptación** | Se comprueba con al menos una prueba automatizada |
| **Tarea** | Cita los requisitos que atiende |
| **Prueba** | Cita el requisito que verifica |
| **Cadena completa** | Requisito → escenario → tarea → código → prueba |

* `/speckit.analyze` ayuda a detectar requisitos sin tarea, tareas sin requisito y contradicciones.

## Buenas prácticas con el agente

| Práctica | Razón |
|---|---|
| **Leer cada documento generado** | El agente puede equivocarse o inventar detalles |
| **Corregir antes de avanzar** | Un error temprano se arrastra a todas las fases |
| **No activar la aprobación automática** | Revisar lo que el agente edita o ejecuta es parte del proceso |
| **Confirmar (commit) después de cada fase** | Permite comparar y revertir |
| **Corregir primero la especificación** | Si el comportamiento es incorrecto, se arregla el documento y luego el código |
| **Escribir texto propio en `/speckit.specify`** | Lo que el agente no puede deducir debe decirse explícitamente |
| **Revisar dependencias propuestas** | El agente puede proponer bibliotecas que la constitución prohíbe |
| **Nunca poner claves o secretos** | Ni en prompts, ni en documentos, ni en confirmaciones |

## Deriva de la especificación

| Concepto | Descripción |
|---|---|
| **Deriva** | La especificación deja de describir lo que el programa realmente hace |
| **Causa típica** | Cambiar el código sin actualizar los documentos |
| **Consecuencia** | Los documentos pierden valor como fuente de verdad |
| **Prevención** | Modificar primero la especificación, después el plan y las tareas, y por último el código |

## Extensiones, presets y flujos de trabajo

| Mecanismo | Para qué sirve |
|---|---|
| **Integration** | Conectar o cambiar de agente de programación |
| **Extension** | Agregar un comando, control de calidad o proceso completo |
| **Preset** | Adaptar plantillas, comandos o metodología; imponer estándares |
| **Workflow** | Automatizar prompts, comandos y tareas |
| **Bundle** | Instalar una configuración curada para un rol o equipo |
| **Catalog** | Descubrir componentes de la comunidad |

```bash
specify extension add bug      # corrección de errores
specify extension add assess   # evaluación de ideas
```

## Limitaciones

| Limitación | Comentario |
|---|---|
| **Depende de la calidad de la especificación** | Una especificación pobre produce un plan y un código pobres |
| **Más lento al inicio** | Escribir y revisar documentos toma tiempo antes de ver código |
| **Puede ser excesivo** | Para cambios triviales o scripts desechables no compensa |
| **El agente no es determinista** | Dos ejecuciones pueden diferir; por eso se revisa cada resultado |
| **Requiere disciplina** | Los documentos deben mantenerse al día con el código |

## Resumen de SDD y Spec Kit

| Idea | Resumen |
|---|---|
| **SDD** | La especificación es la fuente de verdad; el código se deriva de ella |
| **Spec Kit** | Toolkit de código abierto con plantillas, scripts y comandos para aplicar SDD |
| **Instalación** | `uv tool install specify-cli --from git+...@vX.Y.Z` con versión fija |
| **Inicialización** | `specify init` crea `.specify/`, los comandos del agente y las plantillas |
| **Flujo** | constitution → specify → clarify → plan → tasks → analyze → implement |
| **Constitución** | Principios del proyecto que se aplican en todas las fases |
| **`spec.md` vs `plan.md`** | Qué y por qué frente a cómo |
| **Trazabilidad** | Requisito → escenario → tarea → código → prueba |
| **Revisión humana** | Cada documento se lee y corrige antes de continuar |
| **Deriva** | Se evita corrigiendo primero la especificación y luego el código |