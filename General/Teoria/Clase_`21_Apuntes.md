# Hashing

Tomar un valor cualquiera `key`, donde se pasa por alguna función `hash(key)`, que puede obtener algún resultado tal que `#a22a35CTv`

* Se tiene una key que es el `texto plano`, `mensaje` o `llave` que sirve para el mapeo respectivo.
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
|1||
|2||
|3|23|
|4||
|5||
|6|46|
|7|17|
|8|8|
|9||

En el ejemplo anterior, al querer insertar el 666, el resultado de la posición es el `6` ya está ocupado por lo que se genera una colisión.

> Viernes: Manejo de Colisiones
