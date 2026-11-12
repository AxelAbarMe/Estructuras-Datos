# Examen Práctico 2

### Pregunta 1 (AVL – Rotación doble)
Se insertan en un AVL: `25, 15, 35, 45, 40`. ¿Cuál es el **recorrido por niveles** final?

- A) 25, 15, 45, 35, 40
- B) 35, 25, 45, 15, 40
- C) 25, 15, 35, 45, 40
- D) 25, 15, 40, 35, 45
- E) 40, 25, 45, 15, 35

---

### Pregunta 2 (Grafos – DFS no dirigido)
Grafo no dirigido (adyacencias en orden alfabético):

```
A: B, C      B: A, D, E     C: A, E, F     D: B, G
E: B, C, G   F: C           G: D, E
```
¿Qué secuencia produce un **DFS desde A**?

- A) A, B, D, G, E, C, F
- B) A, B, C, D, E, F, G
- C) A, C, F, E, G, D, B
- D) A, B, E, C, F, G, D
- E) A, B, D, E, G, C, F

---

### Pregunta 3 (Hashing – Linear Probing y borrado)
Tabla de 8 posiciones, `h(k) = k % 8`, Linear Probing. Se insertan `16, 24, 8, 17` y luego se borra `24` **marcándola con lápida**. Al buscar `17`, ¿cuántas posiciones se examinan hasta encontrarla?

- A) 1 posición
- B) 2 posiciones
- C) 3 posiciones (índices 1, 2 y 3)
- D) 4 posiciones (índices 0, 1, 2 y 3)
- E) No se encuentra, porque la lápida corta la búsqueda

---

### Pregunta 4 (Backtracking – Permutaciones)
```python
def perm(parcial, usados, n, res):
    if len(parcial) == n:
        res.append(parcial[:]); return
    for x in range(1, n + 1):
        if x not in usados:                  # poda
            parcial.append(x); usados.add(x)
            perm(parcial, usados, n, res)
            parcial.pop(); usados.remove(x)
```
Con `n = 3`, ¿cuántas llamadas a `perm` se realizan en total (incluida la inicial)?

- A) 15
- B) 16
- C) 40
- D) 10
- E) 6

---

### Pregunta 5 (Red-Black)
Se insertan en un Red-Black: `10, 5, 7, 3, 12`. ¿Qué enunciado describe correctamente el resultado (rotaciones individuales)?

- A) Raíz 7; rojos {5, 10, 3, 12}; 2 rotaciones; ningún Caso 1.
- B) Raíz 7; rojos {3, 12}; 1 rotación; un Caso 1.
- C) Raíz 5; rojos {3, 7, 12}; 1 rotación; ningún Caso 1.
- D) Raíz 7 (roja); rojos {3, 7, 12}; 2 rotaciones; un Caso 1.
- E) Raíz 7; rojos {3, 12}; 2 rotaciones; un Caso 1.

---

### Pregunta 6 (Grafos – Orden topológico)
Grafo dirigido, declarado en este orden de vértices: `P, Q, R, S, T, U`. Aristas: `P→Q, P→R, Q→S, R→S, T→R, S→U`. Con el algoritmo de la clase (DFS alfabético, el nodo se coloca al terminar, vector llenado desde el final), ¿qué resultado produce?

- A) P, Q, R, S, T, U
- B) T, P, R, Q, S, U
- C) T, P, Q, R, S, U
- D) U, S, Q, R, P, T
- E) P, T, R, Q, S, U

---

### Pregunta 7 (BST)
Se insertan en un BST: `15, 6, 23, 4, 7, 71, 5, 50`. ¿Cuál es el **Pos-Orden**?

- A) 5, 4, 7, 6, 50, 71, 23, 15
- B) 4, 5, 7, 6, 50, 71, 23, 15
- C) 5, 4, 7, 6, 71, 50, 23, 15
- D) 15, 6, 4, 5, 7, 23, 71, 50
- E) 4, 5, 6, 7, 15, 23, 50, 71

---

### Pregunta 8 (Hashing – Double Hashing)
Tabla de 10 posiciones, `h(k) = k % 10`, `h2(k) = 1 + k % 4`, `pos = (h(k) + h2(k)·i) % 10`. Se insertan en orden `31, 41, 51, 22, 62, 12`. ¿En qué posiciones quedan `41, 51, 62, 12` (en ese orden)?

- A) (2, 3, 5, 6)
- B) (2, 5, 6, 8)
- C) (3, 5, 6, 4)
- D) (3, 5, 8, 4)
- E) (3, 5, 8, 6)

---

### Pregunta 9 (Grafos ponderados – Dijkstra)
Grafo no dirigido:

```
A-B 7   A-C 1   B-C 2   B-D 1   B-E 6   C-D 5   D-E 3
```
Con Dijkstra desde `A`, ¿en qué orden se **confirman** los nodos y cuál es la distancia final a `E`?

- A) A, C, B, D, E; d(E) = 9
- B) A, B, C, D, E; d(E) = 7
- C) A, C, B, D, E; d(E) = 7
- D) A, C, D, B, E; d(E) = 9
- E) A, C, B, E, D; d(E) = 7

---

### Pregunta 10 (Árbol binario general – Inserción por niveles)
Árbol: raíz `A`; hijos `B` y `C`; `B` tiene hijos `D` y `E`; `C` tiene solo hijo izquierdo `F`. Se aplican, en orden, `insert("G")` e `insert("H")` con el algoritmo de inserción por niveles de la clase. ¿Cuál es el padre de `H` y la altura final?

- A) Padre E; altura 3
- B) Padre F; altura 3
- C) Padre D; altura 4
- D) Padre C; altura 2
- E) Padre D; altura 3

---

### Pregunta 11 (Diccionarios)
¿Cuál de las siguientes sentencias lanza `TypeError`?

- A) `d = {(1, 2): "x"}`
- B) `d = {frozenset({1, 2}): "x"}`
- C) `d = {(1, [2]): "x"}`
- D) `d = {"a": [1, 2]}`
- E) `d = {"a": 1, "a": 2}`

---

### Pregunta 12 (Backtracking – N Reinas)
En `n_reinas(4)`, el estado es `columnas = [0, 3, 1]` y se está en la fila 3. ¿Qué ocurre?

- A) Ninguna columna es segura en la fila 3. Se hace `pop` de la col 1 (fila 2), allí no quedan opciones y tampoco en la fila 1 (3 era la última). Se retrocede hasta la fila 0 y continúa con la columna 1.
- B) Se coloca la reina en la fila 3, columna 2, y se obtiene la solución `[0, 3, 1, 2]`.
- C) Se concluye que `n = 4` no tiene solución, porque la columna 0 de la fila 0 falló.
- D) Se hace `pop` solo de la fila 2, se prueba la columna 2 (segura) y se continúa desde ahí.
- E) Tras el primer `pop` se cambia de inmediato la reina de la fila 0 a la columna 1.

---

### Pregunta 13 (AVL – Varios nodos desbalanceados)
Un AVL contiene `9(4(2,7), 15(12(11), 20))`. Se inserta `10`. ¿Qué ocurre?

- A) Rotación simple a la izquierda en 9 (la raíz, porque FB = −2).
- B) Rotación doble en 15.
- C) Rotación simple a la derecha en 12 y luego rotación simple a la izquierda en 9.
- D) Una sola rotación simple a la derecha en 12 (LL); el árbol queda balanceado.
- E) Rotación doble en 12 (izquierda en 11 y derecha en 12).

---

### Pregunta 14 (Grafos – Complejidad de recorridos)
Grafo dirigido con V = 500 y E = 800. ¿Cuál es el orden de magnitud aproximado de operaciones de un BFS con **lista** y con **matriz** de adyacencia?

- A) Lista: 800; matriz: 250 000
- B) Lista: 1 300; matriz: 250 000
- C) Lista: 1 300; matriz: 500
- D) Lista: 250 000; matriz: 1 300
- E) Lista: 1 300; matriz: 400 000

---

### Pregunta 15 (Hashing – Quadratic Probing)
Tabla de 10 posiciones, `h(k) = k % 10`, `pos = (h(k) + i²) % 10`. Se insertan `15, 25, 35, 45, 5`. ¿En qué posición queda `5` y cuántas posiciones se examinan?

- A) Posición 9; 5 posiciones
- B) Posición 1; 4 posiciones
- C) Posición 2; 5 posiciones
- D) Posición 4; 4 posiciones
- E) Posición 1; 5 posiciones

---

### Pregunta 16 (Árboles – Pre-Orden iterativo)
```
        1
      /   \
     2     3
    / \   /
   4   5 6
```
Se ejecuta `pre_orden_iterativo` de la clase (pila; apila primero el hijo derecho). Justo después de imprimir el `2`, ¿cómo está la pila (fondo → tope)?

- A) `[3, 5, 4]`
- B) `[3, 4, 5]`
- C) `[3, 2]`
- D) `[4, 5, 3]`
- E) `[5, 4]`

---

### Pregunta 17 (Red-Black – Propiedades)
```
          13(N)
        /       \
     8(R)       17(N)
    /    \          \
  1(N)  11(N)       25(N)
```
Los hijos vacíos son NULL negros. ¿Qué propiedad Red-Black **se viola**?

- A) La raíz es roja.
- B) Los caminos desde la raíz hasta los NULL no tienen la misma cantidad de nodos negros.
- C) Hay dos nodos rojos consecutivos.
- D) Los hijos NULL deberían ser rojos.
- E) No se viola ninguna: es un Red-Black válido.

---

### Pregunta 18 (Grafos ponderados – Prim)
Grafo no dirigido: `A-B 5, A-C 2, B-C 6, B-D 1, C-D 9, C-E 8, D-E 4`. Con **Prim iniciando en A**, ¿en qué orden se agregan las aristas y cuál es el peso total?

- A) BD, AC, DE, AB; 12
- B) AC, AB, BC, DE; 17
- C) AC, AB, BD, CE; 16
- D) AC, AB, BD, DE; 12
- E) AB, BD, DE, AC; 12

---

### Pregunta 19 (Backtracking – Subconjuntos)
```python
def sumas(items, objetivo):
    res = []
    def bt(inicio, parcial, suma):
        if suma == objetivo:
            res.append(parcial[:]); return
        for i in range(inicio, len(items)):
            if suma + items[i] <= objetivo:         # poda
                parcial.append(items[i])
                bt(i + 1, parcial, suma + items[i])
                parcial.pop()
    bt(0, [], 0)
    return res
```
Con `items = [2, 4, 6, 9]` y `objetivo = 15`, ¿qué devuelve `res` (en orden)?

- A) `[[6, 9], [2, 4, 9]]`
- B) `[[2, 4, 9]]`
- C) `[[2, 4, 9], [6, 9]]`
- D) 8 secuencias (incluye permutaciones como `[4, 2, 9]` y `[9, 6]`)
- E) `[[6, 9]]`

---

### Pregunta 20 (Orden topológico – Trazas)
```python
grafo = {"A":["B"], "B":["C","D"], "C":["E"], "D":["E"], "E":[], "F":["A"]}
print(orden_topologico(grafo))     # función de la clase
```
¿Qué imprime?

- A) `['A','B','C','D','E','F']`
- B) `['F','A','B','C','D','E']`
- C) `['E','C','D','B','A','F']`
- D) `['A','F','B','D','C','E']`
- E) `['F','A','B','D','C','E']`

---

### Pregunta 21 (BST vs AVL)
Se insertan `10, 20, 30, 40, 50` en ese orden en un BST y en un AVL. Indique (altura del BST; altura del AVL; rotaciones del AVL):

- A) 4; 2; 2
- B) 5; 3; 2
- C) 4; 2; 1
- D) 4; 3; 2
- E) 4; 4; 0

---

### Pregunta 22 (Hashing y seguridad)
Dos usuarios eligen la misma contraseña y el sistema guarda su SHA-256. ¿Qué afirmación es correcta?

- A) Sin salt los dos hash serían distintos gracias al efecto avalancha.
- B) Si el atacante obtiene el hash, puede recuperar la contraseña invirtiendo SHA-256 con la llave.
- C) Sin salt ambos hash serían iguales, lo que facilita un ataque de diccionarios; un salt aleatorio por usuario produce hash distintos.
- D) Que dos contraseñas distintas den el mismo SHA-256 es una colisión normal que se resuelve con encadenamiento.
- E) Hashear la contraseña garantiza confidencialidad igual que la encriptación.

---

### Pregunta 23 (Spec-Driven Development)
En un proyecto con Spec Kit se descubre que `plan.md` contiene la regla «un usuario no puede tener más de 3 libros prestados», que no aparece en `spec.md`. ¿Qué corresponde hacer?

- A) Dejarla en `plan.md`, porque es una decisión técnica.
- B) Agregarla a `spec.md` como requisito funcional con su escenario de aceptación, y luego revisar `plan.md` y `tasks.md`.
- C) Borrarla del plan y codificarla directamente en el código sin documentarla.
- D) Moverla a `constitution.md`.
- E) Ejecutar `/speckit.implement` para que el agente la adopte tal como está.

---

### Pregunta 24 (Python – dataclass)
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

a = Node(5); b = Node(5)
print(a == b, a is b)
a.left = Node(3)
print(a == b)
```
¿Qué imprime?

- A) `False False`, luego `False`
- B) `True False`, luego `True`
- C) `True True`, luego `False`
- D) `True False`, luego `False`
- E) `False False`, luego `True`

---

### Pregunta 25 (AVL vs Red-Black – Conteo)
En una práctica, un AVL hizo 5 rotaciones simples y 11 dobles. Un Red-Black hizo 4 casos "línea" (Caso 2, 1 rotación) y 3 casos "triángulo" (Caso 2, 2 rotaciones). ¿Cuántas rotaciones individuales hizo cada uno (AVL y RB)?

- A) 16 y 7
- B) 27 y 7
- C) 16 y 10
- D) 22 y 12
- E) 27 y 10

---

## Solucionario – Examen 2

**P1 – D.**
- Al insertar 40, el nodo 35 queda con FB = 0 − 2 = −2.
- 40 está en el subárbol izquierdo del hijo derecho (45), que es el caso LR de la clase.
- Se rota a la derecha en 45 (queda 40→45) y luego a la izquierda en 35.
- Árbol: `25(15, 40(35,45))`.
- A) usa una sola rotación izquierda en 35, y deja el FB en 2.
- B) rota en la raíz, que no es el nodo x.
- C) no balancea.
- E) es un AVL válido, pero sube 40 como raíz sin pasar por las rotaciones que corresponden.

**P2 – A.**
- A→B→D→G→E→C→F.
- En E se prueba B (visitado), luego C, y desde C se llega a F.
- B) es el BFS.
- C) usa vecinos en orden inverso.
- D) en B salta D y elige E.
- E) mezcla BFS y DFS, cambia de rama antes de agotarla.

**P3 – C.**
- Inserciones: 16→0, 24→1, 8→2 (pasa por 0 y 1) y 17→3 (hash 1, ocupadas 1 y 2).
- Al borrar 24, el índice 1 queda con lápida.
- Para buscar 17 se examinan 1 (lápida, se continúa), 2 (la llave 8) y 3 (encontrada).
- A) y B) ignoran las colisiones.
- D) empieza en 0, aunque el hash de 17 es 1.
- E) es lo que pasaría si se dejara la posición vacía, pero con lápida la búsqueda continúa.

**P4 – B.**
- Nivel 0: 1 llamada.
- Nivel 1: 3.
- Nivel 2: 3·2 = 6.
- Nivel 3: 6.
- Total: 16.
- A) omite la llamada inicial.
- C) es sin poda (1+3+9+27).
- D) corta el conteo en el nivel 2.
- E) cuenta solo las soluciones.

**P5 – E.**
- 10 es la raíz y 5 es rojo.
- 7 (triángulo, tío NULL): doble rotación (izq en 5, der en 10), y queda 7(N) con 5(R) y 10(R). Son 2 rotaciones.
- 3: padre 5 y tío 10 rojos, Caso 1. 5 y 10 pasan a negro y 7 se repinta de negro.
- 12 entra rojo bajo 10, que es negro.
- Final: `7(N); 5(N), 10(N); 3(R), 12(R)`.
- A) nunca recolorea.
- B) cuenta la doble como una.
- C) trata el triángulo como línea.
- D) olvida repintar la raíz.

**P6 – B.**
- DFS(P): Q, S, U. U va al final de la posición 6, luego S, luego Q.
- Se vuelve a P y se visita R (S ya visitado), después P.
- Se sigue con T (R ya visitado).
- Resultado: T, P, R, Q, S, U.
- A) pone T después de R.
- C) es válido, pero sale al visitar los vecinos en orden inverso.
- D) es el orden de finalización sin invertir.
- E) es válido, pero no es lo que produce este algoritmo.

**P7 – A.**
- Subárbol 6: 4 tiene a 5 como hijo derecho, y 7 es hoja. Pos-Orden: 5, 4, 7, 6.
- Subárbol 23: 71 tiene a 50 como hijo izquierdo. Pos-Orden: 50, 71, 23.
- Después viene 15.
- B) pone 4 antes de su hijo 5.
- C) pone 71 antes de 50.
- D) es el Pre-Orden.
- E) es el En-Orden.

**P8 – D.**
- 31→1.
- 41→1 (ocupada), h2=2, pos 3.
- 51→1, h2=4, pos 5.
- 22→2.
- 62→2 (ocupada), h2=3: 5 (ocupada), 8 (libre).
- 12→2, h2=1: 3 (ocupada), 4 (libre).
- A) es Linear.
- B) es Quadratic.
- C) en 62 pasa a la siguiente posición libre linealmente.
- E) usa h2(12)=4 y cae en 6.

**P9 – C.**
- Se confirma A(0), luego C(1) y B(3, mejor que 7).
- Con B(3), D=4 y E=9. Se confirma D(4) y E se mejora a 7.
- Se confirma E(7).
- A) toma el camino directo B→E.
- B) usa el orden alfabético.
- D) confirma D antes de B con una distancia desactualizada.
- E) confirma E antes de que se mejore.

**P10 – E.**
- G: A y B están completos. En C el hijo izquierdo F existe y el derecho no, así que G queda como hijo derecho de C.
- H: C ya está completo. En D el hijo izquierdo es libre, así que H queda como hijo izquierdo de D (profundidad 3, altura 3).
- A) E es hijo derecho de B y aparece después de D.
- B) F ya tiene su lugar y D se revisa antes que F.
- C) cuenta niveles en vez de aristas.
- D) C ya estaba completo.

**P11 – C.**
- La tupla contiene una lista, que no es hashable, así que lanza `TypeError`.
- A) y B) son llaves válidas (tupla de inmutables y frozenset).
- D) tiene un valor lista, y los valores pueden ser cualquier tipo.
- E) repite la llave "a", y el valor se reemplaza (queda `{"a": 2}`).

**P12 – A.**
- Fila 3 con `[0,3,1]`: col 0 y col 1 están ocupadas (misma columna), col 2 está en diagonal con (2,1), col 3 está en la misma columna que (1,3). No hay columna segura.
- Fila 2: col 2 está en diagonal con (0,0) y col 3 en la misma columna que (1,3). Se agotan las opciones.
- Fila 1: la columna 3 era la última opción. Se retrocede a la fila 0 y se pasa a la columna 1.
- B) la columna 2 está atacada.
- C) confunde un callejón sin salida con ausencia de solución (n=4 sí tiene 2).
- D) la columna 2 está atacada.
- E) se salta los retrocesos intermedios.

**P13 – D.**
- Con 10 se desbalancean 12 (FB=2), 15 (FB=2) y 9 (FB=−2).
- Se corrige siempre el x más bajo: 12, con inserción en la izquierda de su hijo izquierdo, caso LL.
- Al rotar a la derecha en 12, 11 queda con hijos 10 y 12, y los nodos 15 y 9 quedan balanceados.
- A) y C) corrigen nodos más altos.
- B) usa un nodo y un tipo de rotación equivocados.
- E) aplica una rotación doble a un caso simple.

**P14 – B.**
- Lista: V+E = 1 300.
- Matriz: V² = 250 000.
- A) ignora V.
- C) confunde el costo de la matriz con V.
- D) invierte los costos.
- E) calcula V·E.

**P15 – E.**
- 15→5, 25→6, 35→5, 6 y `5+4=9`, 45→5, 6, 9 y `5+9=14→4`.
- 5: prueba 5, 6, 9, 4 (ocupadas) y `5+16=21→1`. Queda en 1 tras 5 posiciones examinadas.
- A) es Linear.
- B) no cuenta la posición inicial.
- C) calcula mal el módulo.
- D) olvida que el 4 está ocupado por el 45.

**P16 – A.**
- Pila `[1]`. Se saca 1 y se apila 3 y luego 2, quedando `[3, 2]`.
- Se saca 2 y se imprime. Se apilan 5 y luego 4, quedando `[3, 5, 4]` (tope: 4).
- B) apila el izquierdo primero.
- C) es el estado antes de sacar el 2.
- D) y E) pierden o reordenan elementos.

**P17 – B.**
- Caminos con nodos negros: 13→8→1: 2 negros. 13→8→11: 2. 13→17→NULL: 2. 13→17→25: **3**. No coinciden.
- No hay violaciones de las propiedades 2 y 6 (la raíz es negra y el rojo 8 tiene hijos negros).
- A) la raíz es negra.
- C) no hay rojos consecutivos.
- D) los NULL son negros.
- E) es inválido por la altura negra.

**P18 – D.**
- Prim: desde A toma AC(2). Luego AB(5) (BC=6, CD=9 son mayores).
- Del conjunto {A,B,C}: BD(1), y después DE(4) en lugar de CE(8).
- Total 12.
- A) es el orden de Kruskal.
- B) incluye BC, que forma ciclo.
- C) toma CE en vez de DE.
- E) tiene los mismos pesos, pero no es el orden de Prim iniciando en A.

**P19 – C.**
- El `for` con `inicio` va en orden de índices.
- Se explora [2,4,...]; 6 da 12 y 9 queda podado (21 > 15). Con 9 se llega a [2,4,9]=15, que se guarda primero.
- Luego se prueba [2,6,...], [2,9], etc., que no suman 15.
- Después [4,...]. Finalmente [6,9]=15, que se guarda segundo.
- A) invierte el orden.
- B) y E) pierden una solución.
- D) ocurriría sin el parámetro `inicio`.

**P20 – E.**
- DFS(A): B, C, E. E queda en la posición 6, C en la 5.
- Se vuelve a B y se visita D (E ya está terminado). D en la 4, B en la 3, A en la 2.
- F al final, en la posición 1.
- Resultado: `[F, A, B, D, C, E]`.
- A) es el orden original.
- B) es válido, pero sale al visitar vecinos en orden inverso.
- C) es el orden de finalización.
- D) coloca A antes que F, y F→A lo prohíbe.

**P21 – A.**
- BST: cadena, altura 4.
- AVL: insertar 30 provoca una rotación simple en 10 (queda `20(10,30)`). Insertar 50 provoca otra en 30, y queda `20(10, 40(30,50))`: 2 rotaciones y altura 2.
- B) cuenta niveles.
- C) pierde una rotación.
- D) altura equivocada.
- E) AVL sin rotaciones.

**P22 – C.**
- Hash determinista: la misma entrada da el mismo hash.
- El salt aleatorio hace que dos contraseñas iguales den hashes distintos y dificulta el ataque de diccionarios.
- A) niega el determinismo.
- B) el hash es unidireccional.
- D) en hashing criptográfico las colisiones deben ser prácticamente imposibles.
- E) el hash sirve para integridad y autenticación, no para confidencialidad.

**P23 – B.**
- `spec.md` responde qué y por qué. `plan.md` responde cómo.
- Una regla de negocio debe vivir en `spec.md` (con su FR y escenario). Después se actualizan plan y tareas, y `/speckit.analyze` ayuda a verificar.
- A) mezcla reglas de negocio con tecnología.
- C) provoca deriva.
- D) la constitución contiene principios del proyecto, no requisitos de una funcionalidad.
- E) propaga el error al código.

**P24 – D.**
- `@dataclass` genera `__eq__` por valor.
- Primero: `a == b` es `True` (mismos campos) y `a is b` es `False`.
- Después de `a.left = Node(3)`, `a.left != b.left` (None), así que `a == b` es `False`.
- A) y E) suponen comparación por identidad.
- B) cree que la igualdad no cambia.
- C) confunde `==` con `is`.

**P25 – E.**
- AVL: 5·1 + 11·2 = 27.
- RB: 4·1 + 3·2 = 10.
- A) y C) cuentan cada doble como una rotación.
- B) y D) combinan un AVL con un RB de otra práctica (7 = 4+3 sin ponderar, 22 y 12 son de las secuencias 1 y 2).