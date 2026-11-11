# =========================================
# SEGMENTO 19: HASHING Y SEGURIDAD INFORMÁTICA
# =========================================

Tomar un valor cualquiera `key`, donde se pasa por alguna función `hash(key)`, que puede obtener algún resultado tal que `#a22a35CTv`

* Se tiene una key que es el `texto plano`, `mensaje` o `llave` que sirve para el mapeo respectivo. Siempre es único por llave
* Hash es una función matemática compleja (algoritmos de números primos, factoriales, etc.)
* El resultado puede llegar a llamarse: `message digest`, `digest`, `hash`, `hash value`.
* Una misma entrada **siempre** produce el mismo resultado (la función es **determinista**).

> Los tiempos de insertar, borrar y buscar todos son **O(1).**

## Términos básicos

| Término | Qué es | Ejemplo |
|---|---|---|
| **Key** | Texto plano, mensaje o llave que se quiere mapear. Es única por llave | `23`, `"apple"` |
| **Función hash** | Función matemática que transforma la key en un resultado | `hash(k) = k % 10` |
| **Hash value** | Resultado de aplicar la función (también llamado `digest`, `message digest` o `hash`) | `#a22a35CTv` |
| **Tabla hash** | Espacio de memoria donde se guardan los valores, con posiciones para el mapeo | Vector de 10 posiciones |
| **Bucket / Slot** | Cada posición de la tabla donde se puede guardar un valor | Posición `3` |
| **Colisión** | Dos keys distintas que caen en la misma posición | `46` y `666` en la posición `6` |
| **Key Space** | Rango de valores posibles que puede tomar una key | `100000000` a `999999999` |
| **Factor de carga** | Relación entre elementos guardados y posiciones de la tabla (`n / m`) | 5 elementos en 10 posiciones = `0.5` |

## Flujo general

| Paso | Qué se hace |
|---|---|
| **1** | Se recibe la `key` (texto plano, mensaje o llave) |
| **2** | Se aplica la función `hash(key)` |
| **3** | Se obtiene el `hash value` (o la posición en la tabla) |
| **4** | Se usa ese resultado para insertar, borrar o buscar |

## Propiedades del hashing

* **One Way**: Se tiene el texto original y se convierte en un hash value, pero no se puede realizar la operación inversa para obtener el mensaje.
* **Único para entradas distintas**: Se tiene un mensaje y se obtiene el hash, no hay ningún mensaje posible que genere el mismo hash obtenido del mensaje #1. Siempre se generan hash diferentes de entradas distintas. **(Fingerprint)**
* El **resultado** siempre tiene la misma longitud: Si ingresan mensaje `a` y un PDF de 1000 páginas, ambos siempre tendrán la misma longitud

| Propiedad | Qué significa | Ejemplo |
|---|---|---|
| **One Way** | No se puede volver del hash al mensaje original | `hash("hola")` → `#a22a35CTv`, pero de `#a22a35CTv` no se obtiene `"hola"` |
| **Único (Fingerprint)** | Entradas distintas generan hash distintos | Mensaje #1 y mensaje #2 → hash diferentes |
| **Longitud fija** | El resultado siempre mide lo mismo sin importar la entrada | `a` y un PDF de 1000 páginas → misma longitud |
| **Determinista** | La misma entrada siempre da el mismo hash | `hash("hola")` hoy y mañana → mismo resultado |
| **Efecto avalancha** | Un cambio mínimo en la entrada cambia el hash por completo | `hola` y `Hola` → hash totalmente distintos |
| **Rápido de calcular** | Obtener el hash de cualquier entrada es eficiente | Fundamental para lograr O(1) |

* En las **tablas hash** (estructuras de datos) la unicidad es ideal pero no absoluta: como hay más keys posibles que posiciones, **pueden ocurrir colisiones**.
* En el **hashing criptográfico** (SHA-256, por ejemplo) encontrar dos entradas con el mismo hash es computacionalmente inviable, por eso se usa como **fingerprint**.

## Características de una buena función hash

| Característica | Descripción |
|---|---|
| **Uniformidad** | Distribuye las keys de forma pareja en toda la tabla, evitando que se acumulen en pocas posiciones |
| **Eficiencia** | Se calcula en tiempo constante |
| **Determinismo** | Misma key, misma posición |
| **Pocas colisiones** | Minimiza que keys distintas caigan en la misma posición |
| **Usa toda la tabla** | Cualquier posición puede ser el resultado |

## Cómo se aplican en las estructuras de datos

> Un diccionario de Python (`dict`) es una tabla hash

La mayoría de hash se implementan usando vectores por la memoria contigua. Una tabla hash es el espacio de memoria donde se guardan, siempre tienen posiciones para poder realizar el mapeo.

| Aspecto | Descripción |
|---|---|
| **Estructura usada** | Vectores (arreglos), por la memoria contigua |
| **Tabla hash** | Espacio de memoria donde se guardan los valores |
| **Posiciones** | Siempre existen, para poder realizar el mapeo |
| **Ejemplo en Python** | `dict` y `set` |

```python
# Función hash de ejemplo:

def hash(k):
    return k % 10
```

Con valores de ejemplo: 23, 30, 17, 8, 46

### Cálculo de cada posición

| Key | Operación | Posición |
|---|---|---|
| 23 | `23 % 10` | 3 |
| 30 | `30 % 10` | 0 |
| 17 | `17 % 10` | 7 |
| 8 | `8 % 10` | 8 |
| 46 | `46 % 10` | 6 |

### Tabla Hash del ejemplo anterior ingresado

| Posición | Valor |
|:--:|:--:|
| 0 | 30 |
| 1 |  |
| 2 |  |
| 3 | 23 |
| 4 |  |
| 5 |  |
| 6 | 46 |
| 7 | 17 |
| 8 | 8 |
| 9 |  |

En el ejemplo anterior, al querer insertar el 666, el resultado de la posición es el `6` que ya está ocupado por lo que se genera una colisión.

### Operaciones sobre la tabla

| Operación | Cómo funciona | Tiempo |
|---|---|---|
| **Insertar** | Se calcula `hash(key)` y se guarda en esa posición | O(1) |
| **Buscar** | Se calcula `hash(key)` y se revisa esa posición | O(1) |
| **Borrar** | Se calcula `hash(key)` y se libera esa posición | O(1) |

* Se llega directo a la posición sin recorrer los demás elementos, a diferencia de un arreglo desordenado (O(n)) o un árbol balanceado (O(log n)).
* En el **peor caso** (todas las keys colisionan en una misma posición) los tiempos degradan a **O(n)**; por eso importa tener una buena función hash.

## Key Space

* **Key Space**: El rango de valores posibles que puede tomar almacenar o mapear todos los valores posibles.

En el caso de las cédulas de los estudiantes en Costa Rica, con valores de 100000000 hasta 999999999 ocuparía el valor máximo del `Key Space` debido a que no se conoce quienes serán los que matricularán los cursos, por lo que se debe tomar el valor máximo de 1000000000. Esto provoca que podría tomar hasta 40GB de memoria, lo que provocaría crash en cualquier servidor.

Para aproximarse a un caso más probable de los matriculados, al trabajar con 500k casos el costo de memoria se reduce, pero siempre existe la posibilidad de colisiones.

| Escenario | Tamaño de la tabla | Memoria | Colisiones |
|---|---|---|---|
| **Key Space completo** (cédulas) | 1000000000 posiciones | Hasta 40GB (crash en cualquier servidor) | Ninguna, cada cédula tiene su posición |
| **Caso probable** (matriculados) | ~500k posiciones | Mucho menor | Posibles |

* Entre **menos memoria** se use, **más probabilidad de colisiones**; entre **más memoria**, menos colisiones pero mayor costo.
* Este balance entre memoria y colisiones es el problema central del diseño de tablas hash.

## Colisiones

* Ocurre cuando `hash(k1) == hash(k2)` pero `k1 != k2`.
* Es inevitable cuando el Key Space es mayor que el tamaño de la tabla.

| Técnica | Idea | Resumen |
|---|---|---|
| **Encadenamiento (chaining)** | Cada posición guarda una lista con todas las keys que caen allí | La posición `6` guardaría `46 → 666` |
| **Direccionamiento abierto (open addressing)** | Si la posición está ocupada, se busca otra libre dentro de la misma tabla | `666` pasaría a la posición `7`, `8`... hasta encontrar una libre |

* **Rehashing**: cuando el factor de carga es muy alto, se crea una tabla más grande y se reinsertan todas las keys.

> Viernes: Manejo de Colisiones

# Seguridad Informática

## Pilares de un sistema seguro

| Pilar | Idea principal | Herramienta |
|---|---|---|
| **Confidencialidad** | Solo quien está autorizado puede leer la información | Encriptación |
| **Integridad** | La información no fue modificada | Hashing |
| **Autentificación** | Se verifica la identidad de quien accede | Contraseñas, hash, factores múltiples |
| **Disponibilidad** | El sistema y los datos están accesibles cuando se necesitan | Respaldos, redundancia |

1. **Confidencialidad**
   * **Encriptación**: Se toma un texto plano y se pasa por una función de encriptación `encrypt(x)`, para obtener un texto cifrado (`$1aA21363HTd`)
   * Si se puede volver al valor original en encriptación, realizando un proceso de desencriptación.
   * Se diferencia del hashing en que la encriptación **sí es reversible** y el hashing **no**.

| Operación | Reversible | Resultado | Uso |
|---|---|---|---|
| **Encriptación** | Sí (con la llave) | Texto cifrado, de longitud variable | Confidencialidad |
| **Hashing** | No | Hash value, de longitud fija | Integridad |

2. **Integridad**
   * **Hashing**: Se toma un texto plano, se aplica la función hash(x) y se obtiene el hash value de dicho mensaje (`26z$zAaBc`)
   * **Ataque de diccionarios**: Obtener el hash de una lista de palabras comunes y combinaciones de caracteres y compararlos con los hash extraídos en la red.
   * Un ejemplo de la integridad utilizando hash es cuando se envía un mensaje encriptado, se aplica el hash y se envía por internet, el mensaje recibido por el servidor se verifica usando el hash y si cambio, no se aprueba. Si se cambia el valor original no se puede debido a que está encriptado y finalmente, si desencriptan el mensaje original, este tiene métodos para cambiar el hash si se desencripta antes de llegar al servidor.

| Paso | Qué ocurre |
|---|---|
| **1** | Se toma el mensaje y se encripta |
| **2** | Se aplica el hash y se envía junto con el mensaje por internet |
| **3** | El servidor recibe el mensaje y calcula su hash |
| **4** | Se compara el hash calculado con el recibido |
| **5** | Si **coinciden**, se aprueba; si **cambió**, no se aprueba |

   * **Salt**: Dato aleatorio que se agrega a la contraseña antes de aplicar el hash, para que dos contraseñas iguales produzcan hash distintos y el ataque de diccionarios sea más difícil.

3. **Autentificación**
   * Verificar que quien accede es realmente quien dice ser.
   * Las contraseñas no se guardan en texto plano: se guarda su **hash value**, y al iniciar sesión se calcula el hash de lo ingresado y se compara con el guardado.
   * Se complementa con factores adicionales (código por mensaje, aplicación autenticadora, huella).

4. **Disponibilidad**
   * Garantizar que el sistema y la información estén accesibles cuando se necesiten.
   * Amenazas comunes: ataques de **denegación de servicio (DoS)**, fallas de hardware y pérdida de datos.
   * Medidas: respaldos, redundancia de servidores y monitoreo.

## Algoritmos de hash comunes

| Algoritmo | Longitud del resultado | Uso | Estado |
|---|---|---|---|
| **MD5** | 128 bits | Verificar archivos | Inseguro para criptografía |
| **SHA-1** | 160 bits | Antiguo en certificados y control de versiones | Inseguro para criptografía |
| **SHA-256** | 256 bits | Integridad, firmas, blockchain | Seguro |
| **bcrypt / Argon2** | Variable | Guardar contraseñas (son lentos a propósito) | Seguro |

## Resumen de conceptos

| Concepto | Hashing en estructuras de datos | Hashing en seguridad |
|---|---|---|
| **Objetivo** | Acceso rápido por key (O(1)) | Integridad y autentificación |
| **Resultado** | Posición en la tabla | Hash value / digest |
| **Colisiones** | Aceptables y se manejan | Deben ser prácticamente imposibles |
| **Ejemplo** | `dict` de Python | SHA-256 de un mensaje |
