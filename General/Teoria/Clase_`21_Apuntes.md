# Hashing

Tomar un valor cualquiera `key`, donde se pasa por alguna función `hash(key)`, que puede obtener algún resultado tal que `#a22a35CTv`

* Se tiene una key que es el `texto plano`, `mensaje` o `llave` que sirve para el mapeo respectivo. Siempre es único por llave
* Hash es un función matemática compleja (Algoritmos de números primos, factoriales, etc.)
* El resultado puede llegar a llamarse: `message digest`,`digest`,`hash`,`hash value`.

> Los tiempos de insertar, borrar y buscar todos son **O(1).**

## Propiedades del hashing

* **One Way**: Se tiene el texto original y se convierte en un hash value, pero no se puede realizar la operación inversa para obtener el mensaje.
* **Único para entradas distintas**: Se tiene un mensaje y se obtiene el hash, no hay ningún mensaje posible que genere el mismo hash obtenido del mensaje #1. Siempre se generan hash diferentes de entradas distintas. **(Fingerprint)**
* El **resultado** siempre tiene la misma longitud: Si ingresan mensaje `a` y un PDF de 1000 páginas, ambos siempre tendrán la misma longitud

## Como se aplican en las estructuras de datos

> Un diccionario de Python (`dict`) es una tabla hash

La mayoría de hash se implementan usando vectores por la memoria contigua. Una tabla hash es el espacio de memoria donde se guardan, siempre tienen posiciones para poder realizar el mapeo.

```python
# Función hash de ejemplo:

  def hash(k):
    return r % 10
```

Con valores de ejemplo: 23,30,17,8,46

### Tabla Hash del ejemplo anterior ingresado

|0|30
|:--:|:--:|
|1|  |
|2|  |
|3|23|
|4|  |
|5|  |
|6|46|
|7|17|
|8|8 |
|9|  |

En el ejemplo anterior, al querer insertar el 666, el resultado de la posición es el `6` ya está ocupado por lo que se genera una colisión.

* **Key Space**: El rango de valores posibles que puede tomar almacenar o mapear todos los valores posibles.

En el caso de las cédulas de los estudiantes en Costa Rica, con valores de 100000000 hasta 999999999 ocuparía el valor máximo del `Key Space` debido a que no se conoce quienes serán los que matricularán los cursos, por lo que se debe tomar el valor máximo de 1000000000. Esto provoca que podría tomar hasta 40GB de memoria, lo que provocaria crash en cualquier servidor.

Para aproximarse a un caso más probable de los matriculados, al trabajar con 500k casos el costo de memoria se reduce, pero siempre existe la posibilidad de colisiones.

> Viernes: Manejo de Colisiones

# Seguridad Informática

## Pilares de un sistema seguro

1. **Confidencialidad**
   * **Encriptación**: Se toma un texto plano y se pasa por una función de encriptación `encrypt(x)`, para obtener un texto cifrado (`$1aA21363HTd`)
   * Si se puede volver al valor original en encriptación, realizando un proceso de desencriptación.
2. **Integridad**
   * **Hashing**: Se toma un texto plano, se aplica la función hash(x) y se obtiene el hash value de dicho mensaje (`26z$zAaBc`)
   * **Ataque de diccionarios**: Obtener el hash de una lista de palabras comunes y combinaciones de caracteres y compararlos con los hash extraídos en la red.
   * Un ejemplo de la integridad utilizando hash es cuando se envía un mensaje encriptado, se aplica el hash y se envía por internet, el mensaje recibido por el servidor se verifica usando el hash y si cambio, no se aprueba. Si se cambia el valor original no se puede debido a que está encriptado y finalmente, si desencriptan el mensaje original, este tiene métodos para cambiar el hash si se desencripta antes de llegar al servidor.
3. **Autentificación**
4. **Disponibilidad**
