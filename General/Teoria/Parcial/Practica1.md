# Exámenes Prácticos de Estructuras de Datos – II Parcial

**Alcance:** solo el material entregado. Se excluyen Docker y Kubernetes y el Segmento 27.

**Convenciones (las de la clase):**
- La altura se mide en aristas (hoja = 0, árbol vacío = −1).
- Las rotaciones LL, RR, LR y RL se nombran por el lugar de inserción respecto al nodo "x".
- Las llaves de texto se comparan alfabéticamente.
- Las adyacencias se procesan de menor a mayor.
- En Red-Black, una rotación doble cuenta como 2 rotaciones.
- Cada examen tiene 25 preguntas intercaladas, 18 de ellas simulaciones con datos concretos.
- Las respuestas están en el solucionario de cada examen.

---

# Examen Práctico 1

### Pregunta 1 (Grafos)
Grafo dirigido con adyacencias en orden alfabético:

```
A: B, D     B: C, E     C: F     D: E     E: F     F: G     G: (ninguna)
```

¿Qué secuencia produce un **DFS** desde `A`?

- A) A, B, D, C, E, F, G
- B) A, B, C, F, G, E, D
- C) A, B, C, F, G, D, E
- D) A, D, E, F, G, B, C
- E) A, B, E, F, G, C, D

---

### Pregunta 2 (AVL)
Se insertan en un AVL, en este orden: `50, 30, 70, 20, 40, 35`. ¿Cuál es el **recorrido por niveles (BFS)** del árbol final?

- A) 40, 30, 50, 20, 35, 70
- B) 30, 20, 50, 40, 70, 35
- C) 35, 30, 50, 20, 40, 70
- D) 50, 40, 70, 30, 20, 35
- E) 50, 30, 70, 20, 40, 35

---

### Pregunta 3 (Hashing – Quadratic Probing)
Tabla de 7 posiciones, `h(k) = k % 7`, `pos = (h(k) + i²) % 7`. Se insertan en orden `12, 13, 26, 19, 44`. ¿Cómo queda la tabla (índices 0 a 6)?

- A) `[26, 19, 44, –, –, 12, 13]`
- B) `[–, 19, 44, –, 26, 12, 13]`
- C) `[19, –, 26, 44, –, 12, 13]`
- D) `[26, –, 19, –, 44, 12, 13]`
- E) `[26, –, 19, 44, –, 12, 13]`

---

### Pregunta 4 (Backtracking – N Reinas)
Se usa el código de la clase (columnas de `0` a `n-1`, filas llenadas en orden, `es_segura` revisa columna y diagonales) con `n = 5`. ¿Cuál es la **primera solución** que se agrega a `soluciones` (`columnas[f]` = columna de la fila `f`)?

- A) `[0, 3, 1, 4, 2]`
- B) `[0, 2, 1, 4, 3]`
- C) `[0, 2, 4, 3, 1]`
- D) `[1, 3, 0, 2, 4]`
- E) `[0, 2, 4, 1, 3]`

---

### Pregunta 5 (Red-Black)
Se insertan en un Red-Black: `10, 20, 30, 15, 25`. ¿Qué nodos quedan **rojos** en el árbol final?

- A) 15, 25, 30
- B) 10, 15, 25, 30
- C) 15, 20, 25
- D) 15, 25
- E) 10, 30

---

### Pregunta 6 (Árboles binarios – Recorridos)
```
          M
        /   \
       D     R
        \   / \
         H P   T
        /   \
       F     Q
```
¿Cuál es el recorrido **Pos-Orden**?

- A) D, F, H, M, P, Q, R, T
- B) F, H, D, P, Q, T, R, M
- C) F, H, D, Q, P, T, R, M
- D) H, F, D, Q, P, T, R, M
- E) F, D, H, Q, P, T, R, M

---

### Pregunta 7 (Grafos – Orden topológico)
Grafo dirigido: `A→C, B→C, B→D, C→E, D→E, D→F, E→G, F→G`. Se usa el algoritmo de la clase (DFS que registra el nodo al terminar y llena el vector desde la última posición). Los vértices y los vecinos se procesan en orden alfabético y se empieza en `A`. ¿Qué resultado produce?

- A) B, D, F, A, C, E, G
- B) A, B, C, D, E, F, G
- C) G, E, C, A, F, D, B
- D) A, C, E, G, B, D, F
- E) D, B, F, A, C, E, G

---

### Pregunta 8 (Hashing – Factor de carga)
Una tabla de 13 posiciones usa un factor de carga límite de **0.85**, como en la clase. ¿Cuál es el máximo de elementos que puede guardar sin superar el límite (y por lo tanto sin necesitar rehashing)?

- A) 12
- B) 13
- C) 10
- D) 11
- E) 8

---

### Pregunta 9 (BST – Borrado)
Se insertan en un BST: `8, 3, 10, 1, 6, 14, 4, 7, 13`. Luego se borra `3` con el `_delete` de la clase. ¿Cuál es el **Pre-Orden** resultante?

- A) 8, 1, 6, 4, 7, 10, 14, 13
- B) 8, 4, 1, 6, 7, 10, 14, 13
- C) 8, 6, 1, 4, 7, 10, 14, 13
- D) 8, 4, 1, 6, 4, 7, 10, 14, 13
- E) 1, 4, 6, 7, 8, 10, 13, 14

---

### Pregunta 10 (Grafos ponderados – Dijkstra)
Grafo dirigido y ponderado:

```
A→B (4)   A→C (1)   C→B (2)   B→D (1)   C→D (5)   D→E (3)
```
Distancias mínimas desde `A` hacia `(B, C, D, E)`:

- A) (4, 1, 5, 8)
- B) (3, 1, 6, 9)
- C) (3, 1, 5, 8)
- D) (3, 1, 4, 3)
- E) (3, 1, 4, 7)

---

### Pregunta 11 (AVL vs Red-Black)
Se insertan `1, 2, 3, 4, 5, 6, 7` (ascendente) en un AVL y en un Red-Black, contando rotaciones individuales. ¿Qué afirmación es correcta?

- A) AVL: raíz 4 con 4 rotaciones. RB: raíz 2 con 3 rotaciones.
- B) AVL: raíz 4 con 4 rotaciones. RB: raíz 4 con 3 rotaciones.
- C) AVL: raíz 2 con 4 rotaciones. RB: raíz 2 con 3 rotaciones.
- D) AVL: raíz 4 con 3 rotaciones. RB: raíz 2 con 3 rotaciones.
- E) AVL: raíz 4 con 4 rotaciones. RB: raíz 2 con 5 rotaciones.

---

### Pregunta 12 (Hashing – Direct Chaining)
`h(k) = k % 5`, Direct Chaining, cada llave se agrega **al final** de su lista. Se insertan `15, 21, 36, 6, 10, 26, 11`. Si se busca **una vez cada llave** (una búsqueda exitosa por llave), ¿cuántas comparaciones se hacen en total?

- A) 28
- B) 21
- C) 18
- D) 15
- E) 12

---

### Pregunta 13 (Backtracking – Poda y espacio de búsqueda)
```python
def gen(n, opciones, parcial, res):
    if len(parcial) == n:
        res.append("".join(parcial)); return
    for c in opciones:
        if not parcial or parcial[-1] != c:      # poda
            parcial.append(c)
            gen(n, opciones, parcial, res)
            parcial.pop()
```
Con `n = 3` y `opciones = ["a","b","c","d"]`, ¿cuántas llamadas a `gen` se hacen **en total** (incluida la inicial)?

- A) 85
- B) 64
- C) 36
- D) 53
- E) 52

---

### Pregunta 14 (Grafos ponderados – Kruskal)
Grafo no dirigido con aristas: `A-B 4, A-C 2, B-C 5, B-D 10, C-D 3, C-E 8, D-E 7`. ¿Cuál es el **peso total del MST**?

- A) 14
- B) 16
- C) 17
- D) 21
- E) 19

---

### Pregunta 15 (AVL – Factor de balance)
```
          50
        /    \
      30      70
     /  \       \
   20    40      80
  /                \
10                  90
```
Calculando el FB de cada nodo, ¿cuál es el nodo "x" a corregir y qué rotación se aplica?

- A) x = 50, rotación doble
- B) x = 70, rotación doble
- C) x = 80, rotación simple a la izquierda
- D) x = 50, rotación simple a la izquierda
- E) x = 70, rotación simple a la izquierda (RR)

---

### Pregunta 16 (Árboles – Reconstrucción)
Un árbol binario tiene Pre-Orden `7, 3, 1, 5, 4, 9, 8` y En-Orden `1, 3, 4, 5, 7, 8, 9`. ¿Cuál es su **Pos-Orden**?

- A) 1, 4, 5, 3, 8, 9, 7
- B) 1, 3, 4, 5, 7, 8, 9
- C) 1, 4, 5, 3, 9, 8, 7
- D) 1, 5, 4, 3, 8, 9, 7
- E) 7, 3, 1, 5, 4, 9, 8

---

### Pregunta 17 (Hashing – Double Hashing)
Tabla de 11 posiciones, `h(k) = k % 11`, `h2(k) = 3 - k % 3`, `pos = (h(k) + h2(k)·i) % 11`. Se insertan en orden `22, 33, 44, 14, 25`. ¿En qué posiciones quedan **44 y 25**, respectivamente?

- A) (2, 4)
- B) (4, 7)
- C) (1, 5)
- D) (1, 6)
- E) (6, 5)

---

### Pregunta 18 (Grafos – Representaciones)
Un grafo **no dirigido**, sin lazos, tiene 1000 vértices y 3000 aristas. Se guarda en una matriz de adyacencia (0/1). ¿Qué porcentaje de las casillas vale `0`?

- A) 99.7 %
- B) 99.0 %
- C) 97.0 %
- D) 99.9 %
- E) 99.4 %

---

### Pregunta 19 (Árbol binario general – Borrado)
Árbol binario general (por niveles): `1; 2, 3; 4, 5, 6` (4 y 5 son hijos de 2; 6 es hijo izquierdo de 3). Se aplica el `delete(2)` de la clase (BFS con tuplas `(nodo, padre)`). ¿Cuál es el recorrido por niveles resultante?

- A) 1, 2, 3, 4, 5
- B) 1, 6, 3, 4, 5
- C) 1, 4, 3, 5, 6
- D) 1, 3, 4, 5, 6
- E) 1, 5, 3, 4, 6

---

### Pregunta 20 (Orden topológico – Detección de ciclos)
Se usa `orden_topologico` de la clase (estados 0/1/2, lanza `ValueError` si encuentra un nodo "en proceso"). ¿Con cuál grafo lanza `ValueError`?

- A) `{"A":["B","C"], "B":["C"], "C":[]}`
- B) `{"A":["B","C"], "B":["D"], "C":["D"], "D":[]}`
- C) `{"A":["C"], "B":["C"], "C":[]}`
- D) `{"A":["B"], "B":["C"], "C":["D"], "D":["B"]}`
- E) `{"A":["B"], "B":[], "C":["B"]}`

---

### Pregunta 21 (AVL – Borrado)
```
                8
            /       \
          5           11
        /   \        /   \
       3     7     10     12
      / \   /     /
     2   4 6     9
    /
   1
```
Se borra `12` de este AVL. ¿Cuántas rotaciones se necesitan y qué llave queda como raíz?

- A) 2 rotaciones; raíz 5
- B) 1 rotación; raíz 8
- C) 2 rotaciones; raíz 8
- D) 3 rotaciones; raíz 5
- E) 0 rotaciones; raíz 8

---

### Pregunta 22 (Python – Encapsulamiento)
```python
class Tree:
    def __init__(self): self.root = None
    def __recorrer(self, nodo): return nodo
    def recorrer(self):  return self.__recorrer(self.root)

t = Tree()
t.recorrer()                 # (1)
t.__recorrer(None)           # (2)
t._Tree__recorrer(None)      # (3)
```
¿Qué ocurre?

- A) Las tres líneas se ejecutan sin error
- B) (1) funciona; (2) y (3) lanzan `AttributeError`
- C) (1) funciona; (2) lanza `AttributeError`; (3) funciona
- D) (1) lanza `AttributeError`; (2) y (3) funcionan
- E) (1) y (2) funcionan; (3) lanza `AttributeError`

---

### Pregunta 23 (Árboles – Altura)
Un árbol binario tiene **40 nodos**. Con la convención de la clase (hoja = 0), ¿cuáles son su **altura mínima y máxima** posibles?

- A) 6 y 40
- B) 5 y 39
- C) 5 y 40
- D) 6 y 39
- E) 4 y 39

---

### Pregunta 24 (BST – Verificación)
Una función `local_ok` retorna `False` si algún nodo tiene hijo izquierdo `>=` o hijo derecho `<=` que él, comparando **solo con sus hijos directos** (recursivamente). Notación `nodo(izq, der)`, `-` = vacío. ¿Para cuál árbol `local_ok` retorna `True` **aunque no sea un BST**?

- A) `8( 3(1,6), 10(-,14) )`
- B) `8( 3(1,6), 10(9,14) )`
- C) `8( 3(2,1), 10 )`
- D) `8( 10(3,-), - )`
- E) `8( 3(1,9), 10 )`

---

### Pregunta 25 (Complejidad – BST vs AVL)
Se insertan las llaves `1, 2, 3, …, 1000` en ese orden, primero en un BST y luego en un AVL. ¿Qué afirmación es correcta?

- A) Ambos terminan con altura ≈ 10, porque el BST también se equilibra al insertar en orden.
- B) BST: altura 999 y búsqueda O(log n). AVL: altura ≈ 10 y búsqueda O(log n).
- C) BST: altura 999 e inserción total O(n log n). AVL: altura 999 pero con rotaciones.
- D) BST: altura 999, búsqueda O(n) e inserción total O(n²). AVL: altura O(log n) e inserción total O(n log n).
- E) BST: altura 999 e inserción total O(n log n). AVL: inserción total O(n²) por las rotaciones.

---

## Solucionario – Examen 1

**P1 – B.**
- DFS: A→B→C→F→G, que es un callejón sin salida. Se retrocede a B y se visita E (F ya está visitado). Se retrocede a A y se visita D (E ya está visitado).
- A) es el BFS.
- C) olvida volver a B para visitar E.
- D) recorre las adyacencias en orden inverso.
- E) en B toma E antes que C (por ejemplo, apilando sin invertir).

**P2 – A.**
- Antes de `35` el árbol está balanceado: `50(30(20,40),70)`.
- Al insertar `35` (hijo izquierdo de 40) queda FB(50) = 3 − 1 = 2. La inserción fue en el subárbol derecho del hijo izquierdo, que es el caso RL de la clase.
- Se rota a la izquierda en 30, y 40 sube con 30 como hijo izquierdo. Luego se rota a la derecha en 50.
- Resultado: `40(30(20,35), 50(-,70))`.
- Niveles: 40, 30, 50, 20, 35, 70.
- B) usa una sola rotación derecha en 50, y deja a 30 con FB = −2.
- C) sube el nodo insertado (35) como raíz.
- D) solo hace la primera rotación del par.
- E) no balancea.

**P3 – C.**
- 12→5 y 13→6.
- 26 (h=5): prueba 5, 6 y `5+4=9%7=2`, queda en 2.
- 19 (h=5): prueba 5, 6, 2 y `5+9=14%7=0`, queda en 0.
- 44 (h=2): está ocupado por 26, prueba `2+1=3`, queda en 3.
- A) es Linear Probing.
- B) resta `i²`.
- D) usa un salto `2i`.
- E) intercambia 19 y 26.

**P4 – E.**
- Fila 0 usa col 0.
- Fila 1: col 0 y 1 están atacadas, col 2 es segura.
- Fila 2: col 0, 1, 2 y 3 están atacadas, col 4 es segura.
- Fila 3: col 1 es segura.
- Fila 4: col 3 es segura.
- Resultado: `[0,2,4,1,3]`. Se genera en orden lexicográfico por columnas.
- A) y D) son soluciones válidas, pero aparecen después.
- B) y C) tienen ataques diagonales (por ejemplo, fila 2 col 1 con fila 1 col 2).

**P5 – D.**
1. 10 es la raíz negra.
2. 20 es rojo.
3. 30: tío NULL, Caso 2 RR. Rotación izquierda en 10, y queda 20(N) con 10(R) y 30(R).
4. 15: padre 10 rojo y tío 30 rojo, Caso 1. 10 y 30 pasan a negro, 20 pasa a rojo y luego se repinta de negro.
5. 25 entra rojo bajo 30 (negro).
- Rojos finales: {15, 25}.
- A) olvida pintar de negro el tío.
- B) nunca aplica el Caso 1.
- C) olvida repintar la raíz.
- E) se detiene tras la rotación.

**P6 – C.**
- Pos-Orden: Izq, Der, Raíz.
- Subárbol D: F, H, D.
- Subárbol R: Q, P, T, R.
- Después viene M.
- A) es el En-Orden.
- B) visita P antes que su hijo derecho Q.
- D) visita H antes que su hijo F.
- E) visita D antes que su hijo derecho H.

**P7 – A.**
- DFS(A): C, E, G. G se coloca en la posición 7, E en la 6, C en la 5, A en la 4.
- DFS(B): C ya está visitado. Se visita D y luego F (G ya está visitado). F va en la 3, D en la 2, B en la 1.
- Resultado: B, D, F, A, C, E, G.
- B) es el orden alfabético, que es inválido porque D va antes que F.
- C) es el orden de finalización sin invertir.
- D) es el orden de visita.
- E) coloca D antes que B, y B→D lo prohíbe.

**P8 – D.**
- 11/13 = 0.846 ≤ 0.85.
- 12/13 = 0.923 > 0.85.
- A) es el redondeo hacia arriba de 13·0.85 = 11.05.
- B) es la tabla llena.
- C) deja 3 posiciones libres sin criterio.
- E) aplica la regla 2/3 de Python.

**P9 – B.**
- 3 tiene dos hijos (1 y 6). El sucesor en-orden es el menor del subárbol derecho: 6→4.
- Se copia 4 en el nodo y se borra el 4 (hoja).
- Árbol: `8(4(1,6(-,7)), 10(-,14(13)))`.
- A) usa el predecesor (1), cosa que el código no hace.
- C) reemplaza por el hijo derecho y reubica mal el izquierdo.
- D) no borra el sucesor, así que queda duplicado.
- E) es el En-Orden.

**P10 – E.**
- A=0. Se confirma C=1 y B se relaja a min(4, 1+2)=3.
- Se confirma B=3 y D=3+1=4 (mejor que C→D=6).
- Se confirma D=4 y E=7.
- A) usa el camino directo y no relaja B por C.
- B) toma D por C→D directo.
- C) no propaga la mejora de B a D.
- D) toma como distancia solo el peso de la última arista.

**P11 – A.**
- AVL: rotaciones al insertar 3, 5, 6 y 7. Son 4 simples, y queda el árbol perfecto con raíz 4.
- RB: 3 → Caso 2 (RR), 4 → Caso 1, 5 → RR, 6 → Caso 1, 7 → RR. Quedan 3 rotaciones y la raíz es 2 (con 4 rojo).
- B) supone el mismo árbol en RB.
- C) confunde la raíz del AVL.
- D) pierde una rotación.
- E) cuenta los 2 recoloreos del Caso 1 como rotaciones.

**P12 – C.**
- Lista 0: 15→10, con costos 1 y 2, suman 3.
- Lista 1: 21→36→6→26→11, con costos 1+2+3+4+5 = 15.
- Total: 18.
- A) supone todas las llaves en una sola lista (1+…+7).
- B) supone 3 comparaciones por llave.
- D) cuenta solo la lista 1.
- E) es un conteo parcial.

**P13 – D.**
- Nivel 0: 1 llamada.
- Nivel 1: 4.
- Nivel 2: 4·3 = 12.
- Nivel 3: 4·3·3 = 36.
- Total: 53.
- A) es sin poda (1+4+16+64).
- B) cuenta solo las hojas sin poda.
- C) cuenta solo las hojas con poda.
- E) omite la llamada inicial.

**P14 – B.**
- Se ordenan las aristas: AC 2, CD 3, AB 4, BC 5, DE 7, CE 8, BD 10.
- Se aceptan AC, CD y AB. BC se rechaza por formar ciclo. Se acepta DE.
- Son 4 aristas y el total es 16.
- A) deja la arista de E sin conectar.
- C) usa CE (8) en vez de DE.
- D) acepta BC, que forma ciclo.
- E) toma BD, que también cierra un ciclo y deja a E fuera.

**P15 – E.**
- FB(10)=0, FB(20)=1, FB(40)=0, FB(30)=1.
- FB(90)=0, FB(80)=−1, FB(70)=0−2=−2, FB(50)=3−3=0.
- El primer nodo desbalanceado subiendo desde 90 es 70. 90 quedó en el subárbol derecho del hijo derecho, así que es RR: rotación simple a la izquierda.
- A) y D) eligen la raíz, que tiene FB=0.
- B) usa rotación doble.
- C) elige 80, que tiene FB=−1.

**P16 – A.**
- Raíz 7.
- Izquierda: 3, con hijo izquierdo 1 y derecho 5, que tiene a 4 como hijo izquierdo.
- Derecha: 9 con hijo izquierdo 8.
- Pos-Orden: 1, 4, 5, 3, 8, 9, 7.
- B) es el En-Orden.
- C) pone 9 antes que 8.
- D) intercambia 4 y 5.
- E) es el Pre-Orden.

**P17 – C.**
- 22→0.
- 33: h2=3, pos 3.
- 44: h2=1, pos 1.
- 14: está en 3 (ocupada), h2=1, pos 4.
- 25: está en 3 (ocupada), h2=2, pos 5.
- A) es Linear.
- B) es Quadratic.
- D) toma h2(25)=3.
- E) toma h2(44)=3.

**P18 – E.**
- La matriz tiene 10⁶ casillas.
- Es simétrica, así que hay 6000 unos y 994 000 ceros, es decir 99.4 %.
- A) olvida la simetría.
- B), C) y D) son estimaciones sin cálculo.

**P19 – B.**
- BFS: target=2 y last=6 con padre 3.
- Se copia 6 en el target. `3.right is last` es falso, así que `3.left=None`.
- Árbol: 1; 6, 3; 4, 5.
- A) elimina el último nodo sin copiar la llave.
- C) copia el hijo izquierdo.
- D) desplaza todo como si fuera un arreglo.
- E) copia otro nodo.

**P20 – D.**
- En D, B→C→D→B encuentra a B "en proceso" (estado 1), y eso es un ciclo.
- A) y B) tienen aristas hacia nodos ya terminados (estado 2). B es un rombo, no un ciclo.
- C) y E) son acíclicos.

**P21 – A.**
- Al borrar 12, 11 queda con FB=2 y su hijo izquierdo 10 tiene un hijo izquierdo (9). Es el caso LL, rotación derecha en 11, y el subárbol baja a altura 2.
- Entonces 8 tiene FB=4−2=2 con hijo izquierdo 5 (FB=1), otro LL. Se rota a la derecha en 8.
- Son 2 rotaciones en cascada y la raíz es 5.
- B) y E) ignoran la cascada.
- C) olvida cambiar la raíz.
- D) cuenta de más.

**P22 – C.**
- `__recorrer` sufre name mangling y se renombra a `_Tree__recorrer`.
- (1) funciona porque se llama dentro de la clase.
- (2) falla, porque fuera de la clase ese atributo no existe.
- (3) funciona, porque la privacidad es solo una convención.
- A), B), D) y E) ignoran el mangling.

**P23 – B.**
- Altura mínima: ⌊log₂40⌋ = 5. La altura 4 solo admite 31 nodos y la 5 admite 63.
- Altura máxima: n−1 = 39.
- A) cuenta niveles en vez de aristas.
- C) y D) mezclan convenciones.
- E) usa una altura mínima imposible.

**P24 – E.**
- En E, 3(1,9) cumple localmente (1<3<9) y 8 cumple (3<8<10).
- Pero 9 está en el subárbol izquierdo de 8 y 9 > 8, así que no es un BST.
- A) y B) son BST válidos.
- C) y D) fallan localmente, así que `local_ok` devuelve `False`, lo cual es correcto.

**P25 – D.**
- BST: cada inserción recorre toda la cadena, la altura es 999 y la suma es O(n²).
- AVL: la altura es O(log n) (≤ 1.44·log₂n ≈ 14) y el total es O(n log n).
- A) y B) suponen que el BST se equilibra.
- C) y E) invierten las complejidades.

---