# LLM, RAG, MCP, Skills y Spec-Driven Development

---

# 1. El Modelo Base: LLM (Large Language Model)

* El **LLM** es el "cerebro" central: un modelo de lenguaje que razona, entiende texto y genera respuestas.
* Por sí solo, un LLM tiene limitaciones importantes:
  * **Conocimiento congelado:** solo sabe lo que vio en su entrenamiento (tiene un *cutoff* de fecha).
  * **No tiene memoria persistente** entre conversaciones (a menos que se le dé explícitamente).
  * **No puede ejecutar acciones** en el mundo real (no manda correos, no consulta bases de datos, no llama APIs) a menos que se le conecte a algo externo.
* Para resolver estas limitaciones, en el diagrama aparecen **4 mecanismos complementarios**: RAG, Memory, MCP (con Tools/APIs) y Skills. No compiten entre sí, cada uno resuelve un problema distinto:
  * **RAG** responde: *"¿qué sabe el modelo?"* (conocimiento externo/actualizado)
  * **MCP + Tools** responde: *"¿qué puede hacer el modelo?"* (acciones/ejecución)
  * **Skill** responde: *"¿cómo debe razonar/proceder el modelo?"* (procedimiento reutilizable)
  * **Memory** responde: *"¿qué debe recordar el modelo entre interacciones?"* (contexto persistente)

---

# 2. RAG (Retrieval-Augmented Generation)

## ¿Qué es?
* Es una técnica que le da al LLM **acceso a información externa y actualizada** sin necesidad de reentrenarlo.
* Analogía técnica: RAG es como una **inyección de dependencias "Just-In-Time"** — en vez de "hornear" todo el conocimiento dentro de los pesos del modelo, se le "inyecta" la información justo cuando la necesita, en el momento de la consulta.

## ¿Cómo funciona? (flujo general)
1. Se toman documentos (PDFs, bases de conocimiento, wikis internas, etc.) y se dividen en fragmentos (*chunks*).
2. Cada fragmento se convierte en un **vector numérico** (embedding) que representa su significado semántico.
3. Estos vectores se guardan en una **base de datos vectorial** (ej. ChromaDB, Pinecone, FAISS).
4. Cuando el usuario hace una pregunta, esta también se convierte en vector y se busca cuáles fragmentos almacenados son más "parecidos" semánticamente (búsqueda por similitud, no por palabra exacta).
5. Los fragmentos más relevantes se inyectan como **contexto adicional** dentro del prompt que recibe el LLM.
6. El LLM genera la respuesta final combinando su razonamiento con esa información recuperada.

## ¿Por qué es necesario?
* Permite resolver el problema de **respuestas desactualizadas o alucinadas** (inventadas), ya que el modelo responde basándose en documentos reales y verificables.
* Es ideal para dominios específicos: políticas internas de una empresa, documentación técnica, normativa legal, etc., donde el LLM genérico no tiene ese conocimiento propietario.

## Limitación clave
* RAG únicamente **entrega conocimiento**, no le da al modelo la capacidad de **actuar** (no ejecuta nada, no llama servicios externos). Para eso existe MCP.

---

# 3. Memory (Memoria)

* Es el mecanismo que permite que el LLM **recuerde información entre interacciones** (dentro de una sesión larga o incluso entre sesiones distintas).
* En el diagrama, tanto **RAG** como **Memory** apuntan "hacia arriba" al LLM: ambos expanden lo que el modelo "sabe" en el momento de responder, la diferencia es la fuente:
  * RAG: conocimiento externo/documental, normalmente estático o semi-estático (documentos, bases de conocimiento).
  * Memory: información dinámica y contextual generada durante la propia interacción con el usuario (preferencias, historial de la conversación, decisiones previas).
* Administrar bien la memoria es parte de lo que en el diagrama se asocia a **System Thinking**: hay que decidir qué se recuerda, por cuánto tiempo, y cómo se resume para no saturar el contexto del modelo.

---

# 4. MCP (Model Context Protocol)

## Definición
* MCP es un **protocolo estándar** que actúa como una capa intermedia entre el LLM y el mundo exterior (herramientas, APIs, bases de datos, sistemas de archivos, etc.).
* En el diagrama: `LLM <-> MCP <-> [API] [API] [API]`. El MCP es literalmente el "traductor" o "puente" que expone capacidades externas de forma uniforme para que cualquier LLM las pueda usar sin tener que programar una integración distinta para cada servicio.

## Tools (Herramientas)
* Un **Tool** es una función concreta y ejecutable que el LLM puede invocar a través de MCP: por ejemplo, "consultar el clima", "leer un archivo", "hacer una consulta SQL", "enviar un mensaje a Slack".
* Cada Tool tiene:
  * Un **nombre** y una **descripción** (para que el LLM entienda cuándo usarla).
  * Un **esquema de parámetros de entrada** (qué información necesita para ejecutarse).
  * Un **resultado de salida** (lo que retorna al LLM tras ejecutarse).

## Open API
* En el diagrama aparece **"OPEN API"** señalando las herramientas expuestas.
* Esto hace referencia a que muchos servidores MCP exponen sus herramientas usando **especificaciones abiertas de API** (como el estándar OpenAPI/Swagger), lo cual permite que cualquier cliente compatible con MCP pueda "descubrir" automáticamente qué herramientas existen y cómo usarlas, sin necesidad de documentación adicional o integración manual.
* Esto es clave para la **interoperabilidad**: un mismo servidor MCP puede ser consumido por distintos LLMs o aplicaciones (Claude, ChatGPT, agentes personalizados) sin cambiar el código del servidor.

## ¿Por qué existe MCP?
* Antes de MCP, cada vez que se quería conectar un LLM a una herramienta externa había que programar una integración específica (un conector distinto por cada combinación de modelo + servicio).
* MCP estandariza esto: se programa el servidor de la herramienta **una sola vez**, y cualquier LLM compatible con el protocolo puede consumirla.
* Es la pieza que le da al LLM la capacidad de **actuar sobre el mundo real**, no solo de "hablar" sobre él.

---

# 5. SKILL (Habilidad)

## Definición
* Una **Skill** es un paquete reutilizable de **instrucciones, procedimientos y buenas prácticas** que le indica al LLM **cómo razonar o proceder** ante un tipo específico de tarea.
* Si RAG responde "¿qué sabe el modelo?" y MCP responde "¿qué puede hacer el modelo?", **Skill responde "¿cómo debe pensar/proceder el modelo?"**.

## Características
* No es simplemente un prompt largo: es una estructura organizada (por ejemplo, un archivo `SKILL.md` con instrucciones paso a paso, ejemplos, y restricciones) que el modelo consulta cuando detecta que la tarea actual coincide con esa habilidad.
* Puede indicarle al modelo **cuándo y cómo usar una herramienta (Tool)** de forma correcta — no basta con que la herramienta exista, hace falta que el modelo sepa el criterio adecuado para invocarla.
* Se puede combinar con RAG (una skill puede indicar "consulta esta base de conocimiento antes de responder") y con MCP (una skill puede decir "usa esta herramienta específica siguiendo estos pasos").

## Ejemplo conceptual
* Una Skill de "generación de reportes financieros" podría indicarle al modelo: qué estructura de documento usar, qué fórmulas aplicar, en qué orden presentar la información, y qué herramientas (Tools) invocar para obtener los datos actualizados.

---

# 6. Del Problema a la Solución: Intent / Outcome

En el diagrama aparece la secuencia:

```
Solución  ->  Problema
     |
   Intent
     |
 (Outcome)
```

* Esto representa un principio de ingeniería de software (y de diseño de sistemas con IA): **antes de pensar en la solución técnica, hay que tener absoluta claridad sobre el problema real y la intención (Intent) detrás de él**.
* **Intent (Intención):** qué es lo que realmente se quiere lograr, expresado en términos de negocio o necesidad real, no en términos de implementación técnica.
* **Outcome (Resultado esperado):** el resultado medible o verificable que confirma que el Intent se cumplió.
* Error común: saltar directamente a "la solución" sin haber comprendido bien "el problema" y su intención real — esto es precisamente lo que Spec-Driven Development busca evitar.

---

# 7. Spec-Driven Development (Desarrollo guiado por especificaciones)

## Idea central
* El ingeniero de software (o el equipo) primero busca capturar el **Intent** de manera **formal**, antes de escribir una sola línea de código.
* Se redacta una **especificación (spec)** detallada que se convierte en la **fuente de verdad** del desarrollo — tanto para desarrolladores humanos como para agentes de IA que vayan a generar el código.
* Esto es especialmente relevante en el contexto de desarrollo asistido por LLMs: una especificación clara reduce drásticamente la ambigüedad y evita que el modelo "alucine" funcionalidad no solicitada o incompleta.

## Fases / Capas del proceso (según el esquema de la pizarra)

En la pizarra se dibuja una secuencia de "capas" o "fases" que van formalizando la especificación, del 1 al 7 aproximadamente, con un ciclo de retroalimentación (SPEC -> SPEC) antes de llegar al código:

1. **Descripción general del problema** (Especificación general): en lenguaje natural, qué se quiere lograr y por qué.
2. **Refinamiento del alcance:** qué está dentro y qué está fuera del proyecto (scope).
3. **Definición formal de requerimientos:** entradas, salidas, restricciones, reglas de negocio — aquí se empieza a "formalizar" (por eso la pizarra dice `-> FORMAL`).
4. **Modelado de la solución:** arquitectura, contratos de datos, diagramas, posibles contratos de API (ej. especificación OpenAPI/Swagger) — todavía sin código.
5. **Validación de la especificación:** revisión cruzada (ciclo `SPEC -> SPEC` marcado en verde en la pizarra) para asegurar consistencia antes de construir nada; es común iterar varias veces en esta etapa.
6. **Implementación (Código):** recién en esta capa se empieza a escribir código, ya sea manualmente o con asistencia de un LLM guiado estrictamente por la spec.
7. **Verificación/Entrega:** se valida que el código cumple exactamente lo especificado (pruebas, revisión, despliegue).

> **Regla clave marcada en la pizarra:** "Hasta la capa 6 y 7 se hace el código; en la capa 3 y 4 se definen [los requerimientos/arquitectura]." Esto resalta que la mayor parte del esfuerzo intelectual debe invertirse en **definir bien el problema antes de programar**, no al revés.

## Relación con metodologías ágiles
* Spec-Driven Development no reemplaza las metodologías ágiles (Scrum, Kanban, etc.), sino que se integra con ellas: cada historia de usuario o tarea dentro de un sprint puede tener su propia mini-especificación antes de implementarse.
* **Desde el día 1, el proyecto vive en un repositorio de Git**: la especificación, los diagramas, y el código evolucionan juntos y de forma versionada, permitiendo trazabilidad completa entre "lo que se pidió" y "lo que se construyó".

## Diferencia con Test-Driven Development (TDD)
* En **Spec-Driven Development**, el punto de partida es una especificación en lenguaje natural o semi-formal que documenta la *intención* general del sistema.
* En **TDD**, el punto de partida es una prueba automatizada y ejecutable que valida un comportamiento puntual del código.
* Ambos enfoques buscan reducir la ambigüedad, pero en momentos distintos del ciclo de desarrollo: Spec-Driven actúa **antes** de escribir cualquier código; TDD actúa **durante** la escritura del código.

---

# 8. System Thinking (Pensamiento Sistémico)

## ¿Por qué aparece aquí?
* Cuando se trabaja con LLMs, MCP, RAG y Skills combinados, ya **no se está programando una función aislada, sino diseñando un sistema completo** con múltiples partes que interactúan entre sí (el modelo, las herramientas, la memoria, el conocimiento externo).
* **System Thinking** es la disciplina de pensar en el sistema completo — sus componentes, sus interacciones y sus efectos de conjunto — en lugar de optimizar cada pieza de forma aislada.

## Aplicación concreta (según la pizarra)
* **Manejar, coordinar y verificar** que lo que hace el LLM efectivamente corresponde a lo que se espera del sistema en su conjunto (no basta con que cada componente funcione bien por separado; hay que verificar que la orquestación entre LLM + MCP + RAG + Skills produce el resultado correcto de punta a punta).
* **Administrar los tokens:** los LLMs tienen una ventana de contexto limitada (cantidad máxima de tokens que pueden "ver" a la vez). Pensar en el sistema implica decidir:
  * Qué información realmente necesita estar en el contexto en cada momento (relevancia).
  * Cuándo usar RAG (para no meter documentos completos en el prompt) en lugar de pegar todo el texto.
  * Cuándo resumir o descartar historial de conversación para no saturar el contexto ni encarecer el costo de cada llamada (más tokens = más costo y más latencia).
  * Cómo dividir tareas grandes en pasos más pequeños para que cada llamada al LLM trabaje con un contexto manejable.

## Resumen de la mentalidad de System Thinking aplicada a IA
* No se trata solo de "¿el modelo responde bien a esta pregunta?", sino de: "¿el sistema completo (modelo + herramientas + memoria + conocimiento) se comporta de forma predecible, verificable y sostenible en el tiempo?"
* Esto conecta directamente con Spec-Driven Development: una buena especificación facilita que el sistema completo sea verificable, porque define de antemano qué comportamiento se espera de cada componente.

---

# 9. Resumen integrador (cómo se conecta todo)

```
                +-----------+
   RAG -------> |           | <------- Memory
   (sabe)       |    LLM    |          (recuerda)
                |           |
                +-----+-----+
                      |
                      v
                  +-------+
                  |  MCP  |  <-- protocolo estándar (Open API)
                  +---+---+
                      |
            +---------+---------+
            |         |         |
          [API]     [API]     [API]   <-- Tools concretas
```

* **Skill** actúa de forma transversal: le dice al LLM *cómo* usar todo lo anterior correctamente (cuándo consultar RAG, cuándo invocar qué Tool vía MCP, en qué orden y bajo qué criterios).
* **Spec-Driven Development** es la disciplina de ingeniería que asegura que, antes de construir este sistema (LLM + RAG + MCP + Skills), exista una especificación clara del **Intent** y el **Outcome** esperado.
* **System Thinking** es la mentalidad que permite coordinar, verificar y administrar (incluyendo el uso de tokens) que todo el conjunto funcione como un sistema coherente y no como piezas sueltas.

# 10. Uso y Gasto Óptimo de Tokens

## ¿Qué es un token?
* Un **token** es la unidad mínima de texto que un LLM procesa; no es lo mismo que una palabra ni que un carácter.
* En promedio (para idiomas como español o inglés): **1 token ≈ 3-4 caracteres**, o aproximadamente **0.75 palabras por token**.
* Todo lo que entra y sale del modelo se cobra y se limita en tokens: el **prompt del usuario**, el **historial de la conversación**, el **contenido inyectado por RAG**, las **definiciones de Tools/MCP** disponibles, y la **respuesta generada** por el modelo.

## ¿Por qué administrar los tokens es parte de System Thinking?
* Cada llamada a un LLM tiene una **ventana de contexto limitada** (ej. 128K, 200K tokens, etc., según el modelo). Si el sistema completo (LLM + RAG + MCP + Memory) no controla cuánto contexto mete en cada llamada, ocurre:
  * **Saturación del contexto:** información relevante se "pierde" o se trunca porque no cabe.
  * **Mayor costo económico:** la mayoría de proveedores cobran por cantidad de tokens de entrada y salida.
  * **Mayor latencia:** más tokens de entrada implican más tiempo de procesamiento antes de que el modelo empiece a responder.
  * **Degradación de la calidad de respuesta:** contextos muy largos y desordenados pueden hacer que el modelo pierda el foco de lo realmente importante (el llamado efecto "lost in the middle", donde la información en medio de un contexto muy largo tiende a ser menos aprovechada que la del inicio o el final).

## Estrategias para optimizar el consumo de tokens

### A. Reducir lo que entra al modelo
* **Usar RAG en vez de pegar documentos completos:** en lugar de meter un manual de 200 páginas en el prompt, se recuperan solo los 3-5 fragmentos más relevantes (chunking + embeddings + búsqueda semántica, ver sección de RAG).
* **Resumir el historial de conversación:** en conversaciones largas, resumir turnos anteriores en vez de reenviar todo el historial completo en cada llamada (técnica de *context compaction* o *rolling summary*).
* **Evitar redundancia en el prompt:** no repetir instrucciones ya dadas, no incluir ejemplos innecesarios si el modelo ya demuestra entender la tarea.
* **Limitar la cantidad de Tools/MCP expuestas al modelo en cada llamada:** cada Tool disponible agrega su definición (nombre, descripción, esquema de parámetros) al contexto; exponer 50 herramientas cuando solo se necesitan 5 desperdicia tokens y puede confundir al modelo sobre cuál usar.

### B. Reducir lo que produce el modelo
* **Pedir explícitamente el formato de salida** (ej. "responde solo con JSON", "máximo 3 líneas", "sin explicaciones adicionales") evita que el modelo genere texto de relleno innecesario.
* **Evitar pedir razonamiento extenso cuando no se necesita:** activar modos de "pensamiento profundo" (chain-of-thought extendido) solo cuando la tarea realmente lo amerita (problemas complejos), no para preguntas triviales.

### C. Elegir el modelo/tamaño adecuado para la tarea
* No toda tarea necesita el modelo más grande y costoso disponible; tareas simples (clasificación, extracción de datos, resúmenes cortos) pueden resolverse con modelos más pequeños y baratos, reservando los modelos más potentes para tareas que requieren mayor razonamiento.
* Esto es parte de una arquitectura de **enrutamiento de modelos** (*model routing*), donde un sistema decide qué modelo usar según la complejidad de cada solicitud.

### D. Cachear resultados repetidos
* Si una consulta a RAG, a una Tool externa (vía MCP), o incluso una respuesta completa del LLM se va a repetir con los mismos parámetros, conviene **cachear el resultado** en vez de volver a gastar tokens generándolo de nuevo (algunos proveedores ofrecen *prompt caching* para reutilizar partes fijas del contexto sin volver a cobrarlas completas).

---

# 11. Prompts Mejores (Prompt Engineering aplicado al sistema)

## Principios generales de un buen prompt
* **Claridad y especificidad:** decir exactamente qué se quiere, evitando ambigüedad. Un prompt vago genera una respuesta vaga.
* **Contexto suficiente pero no excesivo:** dar la información necesaria para que el modelo entienda la tarea, sin inflar el prompt con datos irrelevantes (relación directa con la sección anterior de tokens).
* **Formato de salida explícito:** indicar si se espera una lista, una tabla, JSON, código, un párrafo corto, etc.
* **Ejemplos (few-shot):** mostrar 1-3 ejemplos de entrada/salida deseada ayuda mucho más que explicar en abstracto lo que se quiere, especialmente en tareas de formato o estilo específico.
* **Pedir razonamiento paso a paso cuando la tarea es compleja:** frases como "razona paso a paso antes de responder" (chain-of-thought) mejoran la precisión en problemas lógicos o matemáticos, aunque consumen más tokens — se debe usar con criterio (ver sección de optimización).
* **Definir el rol o la persona cuando aporta valor real:** ("actúa como un revisor de código senior") ayuda a enmarcar el tono y el criterio de la respuesta, pero no debe abusarse si no cambia realmente el resultado.
* **Separar instrucciones de datos:** usar delimitadores claros (comillas triples, etiquetas XML, bloques de código) para que el modelo distinga entre "la instrucción" y "el contenido sobre el que debe trabajar". Esto reduce ambigüedad y errores de interpretación.
* **Especificar restricciones negativas cuando sea necesario:** no solo decir qué hacer, sino qué evitar ("no inventes datos que no estén en el documento", "no agregues explicaciones fuera del formato pedido").

## Relación con Spec-Driven Development
* Así como una buena especificación reduce la ambigüedad antes de programar, **un buen prompt es, en esencia, una mini-especificación** de lo que se espera del modelo en esa interacción puntual.
* Por eso, en sistemas que combinan **Skills + MCP + RAG**, el prompt final que recibe el LLM debería ser el resultado de ensamblar: la instrucción del usuario + el conocimiento relevante recuperado (RAG) + las herramientas disponibles (MCP) + el procedimiento a seguir (Skill) — todo esto de forma ordenada y sin ruido innecesario, aplicando los mismos principios de claridad y economía de tokens.

## Iteración y verificación (parte de System Thinking)
* Un prompt raramente es perfecto al primer intento: se debe **iterar y verificar** la salida contra el Outcome esperado (definido en la fase de Intent/Spec), ajustando el prompt, el contexto inyectado o las instrucciones de la Skill según los resultados observados.
* En sistemas de producción, esto se traduce en tener **pruebas o evaluaciones (evals)** sobre los prompts, similares en espíritu a las pruebas de unidad en TDD: se define un conjunto de casos de entrada con su resultado esperado, y se valida que el prompt (o el sistema completo LLM+RAG+MCP+Skill) produzca consistentemente el Outcome correcto antes de considerarlo "listo".

## Resumen rápido: buenas prácticas de prompting
* Ser específico en la instrucción y el formato de salida.
* Dar solo el contexto necesario (apoyarse en RAG para no saturar el prompt).
* Usar ejemplos cuando el formato o estilo importa.
* Pedir razonamiento explícito solo si la tarea lo justifica (por costo en tokens).
* Separar claramente instrucción vs. datos con delimitadores.
* Indicar restricciones (qué NO debe hacer el modelo).
* Iterar y validar contra el resultado esperado (Outcome), igual que se valida una especificación.
