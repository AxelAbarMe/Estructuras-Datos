# Modern software development

1. Lo que no cambia: La programación sigue siendo, en esencia, un conjunto de instrucciones para que las computadoras hagan algo. Eso es constante desde hace 25 años y seguirá siéndolo.

2. Desarrollo más rápido e iterativo: Antes el software se construía de forma monolítica: toda la aplicación como una sola pieza, y cualquier cambio obligaba a tocar el sistema completo (como remodelar una casa vieja).
Hoy se usan enfoques como DevOps y arquitecturas como microservicios, que permiten construir y lanzar funciones nuevas por separado, sin esperar meses.
Los contenedores empaquetan el código con todas sus dependencias, logrando que la aplicación corra igual en cualquier entorno (laptop, servidor físico, nube). Se compara con el juego del "teléfono descompuesto": escribir el mensaje en vez de susurrarlo evita distorsiones.

3. La infraestructura también evolucionó: Antes: servidores físicos propios, costosos y lentos de escalar.
Ahora: la nube permite "alquilar" cómputo, desplegar soluciones en minutos y escalar a miles de servidores con unos clics.
Analogía: comprar huevos en la tienda en vez de criar gallinas — dejar la infraestructura pesada a otros para enfocarse en innovar el "producto" (el software).

4. Cambios en procesos y cultura: Los equipos ya no trabajan en silos (desarrollo → operaciones → QA por turnos).
Ahora son más integrados y colaborativos, con metodologías como Agile, DevOps/DevSecOps y CI/CD, que permiten adaptarse rápido al mercado.

5. Conexión directa con el valor de negocio: El desarrollo moderno debe estar ligado a resultados de negocio (experiencia del cliente, ingresos). Si una práctica no aporta diferenciación, vale la pena cuestionar por qué se hace. También se destaca que "moderno" no significa desechar todo lo existente: a veces dejar sistemas legacy como están (si funcionan) es la decisión más eficiente.

### Conclusión del artículo: 
"Desarrollo de software moderno" no es una sola cosa, sino un reflejo de que hoy existen más opciones (nube, SaaS, low-code, serverless, contenedores, agile) para usar mejor los recursos de TI y entregar resultados con mayor velocidad y flexibilidad.


# "How to explain microservices in plain English"

Contexto: Antes, las aplicaciones se construían de forma monolítica: se empieza pequeño y se van agregando funciones hasta terminar en un "monstruo" donde todo está interconectado. Cambiar una parte puede romper el resto, y escalar significa simplemente añadir más servidores (caro e ineficiente).

Definición simple: Los microservicios son una forma de construir software dividiéndolo en servicios pequeños e independientes, cada uno enfocado en hacer una sola cosa bien, que se comunican entre sí mediante interfaces simples para lograr un objetivo de negocio.

### Analogías útiles de expertos consultados:

Como una fábrica: en vez de que una sola persona/máquina construya todo el auto, cada estación se especializa en una tarea (remachar, pintar, etc.).
Es "romper un objetivo grande en partes" que se resuelven de forma independiente.

### 4 ideas clave para explicarlo a no técnicos:

Es un enfoque flexible y eficiente para construir y operar software.
Divide aplicaciones grandes en piezas mucho más pequeñas e independientes entre sí.
Cada microservicio hace una sola cosa, y la hace bien.
Convierte un trabajo enorme (construir, desplegar, actualizar) en lotes más manejables y eficientes.

Nota adicional: Los microservicios suelen ir de la mano con contenedores y orquestación (ej. Kubernetes), siendo un enfoque natural para aplicaciones en la nube o SaaS.

# "How to explain DevOps in plain English"

DevOps nació hace más de una década como un hashtag y se convirtió en un movimiento cultural en TI. No es un producto ni una herramienta única, sino una filosofía que combina personas, procesos y automatización para entregar software más rápido y con mayor calidad.

### 6 formas de explicarlo (analogías de expertos):

- Movimiento cultural: Desarrollo (Dev) y Operaciones (Ops) coinciden en que el software solo genera valor cuando lo usa alguien, así que trabajan juntos para entregarlo con velocidad y calidad.
- Empodera a los desarrolladores: Les da propiedad total sobre el ciclo de vida de la aplicación (de principio a fin), eliminando confusión sobre quién es responsable de qué.
- Enfoque colaborativo: Simplemente, todos trabajan juntos para construir y entregar el software.
- Línea de ensamblaje: Cada equipo (base de datos, seguridad, interfaz) debe diseñar pensando en cómo encajan las piezas de los demás, igual que en una línea de producción automotriz.
- Receta de cocina: Combina tres "ingredientes" — personas, proceso y automatización — tomados de prácticas como Lean, Agile, SRE, CI/CD, ITIL, etc. El secreto está en las proporciones correctas.
- Equipos de carreras (NASCAR/F1): Como un equipo de pit-stop, se trabaja hacia atrás desde el objetivo final, se practica constantemente y se colabora en tiempo real para minimizar el impacto de errores. La velocidad, bien ejecutada, genera más seguridad, no menos.

¿Es DevOps un rol o una metodología?
Hay debate: algunos creen que "ingeniero DevOps" no debería ser un título porque DevOps es una forma de trabajar de toda la organización, no de una persona. Otros defienden el título porque señala una habilidad valiosa y escasa en el mercado. Datos citados: para 2020, la adopción de DevOps rondaba el 74% (con complementos), aunque encontrar y retener talento capacitado seguía siendo el mayor reto (58% y 48% de los encuestados, respectivamente).

# Que son las API
## Definición

API = Application Programming Interface (Interfaz de Programación de Aplicaciones)
Aplicación: software con una función o propósito específico
Interfaz: contrato/protocolo que define cómo se comunican dos aplicaciones (mediante solicitudes y respuestas)
En conjunto: una API permite que distintos sistemas se comuniquen entre sí

## Analogía no técnica (restaurante)

Reservación para 3 personas, quieres cambiarla a 6
Llamas al restaurante → el empleado (API) recibe tu solicitud y responde sí/no
Sin ese "empleado", tendrías que averiguar tú mismo mesas libres, capacidad de cocina, personal, etc. (trabajo innecesario y datos privados expuestos)
Restaurante = aplicación que ofrece un servicio
Tú = aplicación que solicita el servicio
Empleado = la API, el canal de comunicación

## Ejemplo técnico (Apple Weather)

Apple no crea estaciones meteorológicas propias (muy costoso)
Usa la API de un servicio como weather.com
Así accede a los datos solo de la forma que weather.com permite

## Cómo funcionan las Web APIs

Transmiten solicitudes y respuestas vía JSON o XML, normalmente por internet
Cada ciclo solicitud-respuesta = una "API call" (llamada a la API)

## Componentes de una solicitud (request)

URL del endpoint del servidor
Método de solicitud (usualmente HTTP)
El método indica la acción deseada

## Componentes de una respuesta (response) HTTP

Código de estado (ej. error 404 = URL no encontrada)
Encabezado (header)
Cuerpo de la respuesta (body): puede ser el recurso solicitado o mensajes específicos de la aplicación

## Idea clave final

Todo se reduce a: solicitud → respuesta (request → response)

# Monolith vs Microservices

# Arquitectura básica de una PC

# Compiladores vs Intérpretes

# Características de los Compiladores y los intérpretes

# Memory Segments in C/C++











