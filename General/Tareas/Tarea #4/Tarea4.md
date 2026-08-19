# Tarea 4
## Recursión

**Instrucciones**

---

### 1. Binario a Decimal (Recursivo)

Escriba una función recursiva que reciba por parámetro un número binario y lo convierta en su equivalente a decimal. La función recibe como parámetro un objeto de tipo `int` y retorna también un objeto de tipo `int`. No es necesario que valide la entrada (se asume que se envía el parámetro correctamente). Solamente se trabaja con enteros positivos.

```
Entrada: 1111
Salida: 15
```

---

### 2. Decimal a Binario (Recursivo)

Escriba una función recursiva que reciba por parámetro un número decimal y lo convierta en su equivalente en binario. La función recibe como parámetro un objeto de tipo `int` y retorna también un objeto de tipo `int`. Solamente se trabaja con enteros positivos.

```
Entrada: 15
Salida: 1111
```

---

### 3. División Recursiva

Escriba una función recursiva que calcule la división de dos números. La función recibe dos parámetros de tipo `int`: el dividendo y el divisor. La función retorna el cociente de ambos.

```
Entrada: 10, 2
Salida: 5
```

---

### 4. Invertir un Número (Recursivo)

Escriba una función recursiva que reciba por parámetro un número decimal entero positivo y lo invierta. La función recibe como parámetro un objeto de tipo `int` y retorna también un objeto de tipo `int`, con el número invertido. **No trabaje con objetos de tipo string.**

```
Entrada: 1234
Salida: 4321
```

---

### 5. Contar Ocurrencias de un Carácter (Recursivo)

Escriba una función recursiva que reciba por parámetro un string y un carácter, y retorne la cantidad de ocurrencias del carácter dentro del string dado.

---

### 6. Permutaciones de un String (Recursivo)

Para una cadena de caracteres dada, implemente una función que calcule todas las posibles permutaciones de ella. La salida del programa puede ser un vector de tipo string, con cada una de las cadenas.

**Ejemplo:**

* Entrada: `"abc"`
* Salida: `['abc', 'acb', 'bac', 'bca', 'cab', 'cba']`

---

## Observaciones

> **Nota importante:** Esta tarea se revisará de manera automática. Así que cada ejercicio debe recibir por parámetro el valor que se quiere calcular desde la línea de comandos, y solamente se debería imprimir en pantalla el resultado (no incluya ningún texto antes o después).

**Ejemplo:**

```bash
python3 conversion.py 1111
15
```
