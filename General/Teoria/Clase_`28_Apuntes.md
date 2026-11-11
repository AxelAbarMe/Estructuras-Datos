# =========================================
# SEGMENTO 26: PRÁCTICA DE EXAMEN
# =========================================

# Práctica de examen

| Ejercicio | Tema | Qué se pide |
|:--:|---|---|
| **1** | Árboles AVL y Red-Black | Construir el árbol resultante de la secuencia |
| **2** | Árboles AVL y Red-Black | Construir el árbol resultante de la secuencia |
| **3** | Tabla hash | Vector resultante con Direct Chaining, Linear Probing, Quad Probing y Double Hashing |
| **4** | Grafo ponderado | BFS, DFS, matriz de adyacencia, lista de adyacencia y ordenamiento topológico |
| **5** | Grafo dirigido | BFS, DFS, matriz de adyacencia, lista de adyacencia y ordenamiento topológico |

---

## Ejercicio 1: Árboles AVL y Red-Black

Considere la siguiente secuencia de entrada de elementos que se insertan en un árbol AVL y en un Red-Black:

* `13, 24, 5, 56, 90, 1, 17, 22, 25, 8, 31, 27, 4`

Construya el árbol resultante para cada uno.

### Respuesta

```
                    24
          ┌─────────┴─────────┐
         13                   56
      ┌───┴───┐           ┌───┴───┐
      5       22         27       90
    ┌─┴─┐   ┌─┘        ┌─┴─┐
    1   8   17        25   31
    └─┐
      4
```

| Nodo | Hijo izquierdo | Hijo derecho |
|:--:|:--:|:--:|
| **24** | 13 | 56 |
| **13** | 5 | 22 |
| **56** | 27 | 90 |
| **5** | 1 | 8 |
| **22** | 17 | — |
| **27** | 25 | 31 |
| **1** | — | 4 |

---

## Ejercicio 2: Árboles AVL y Red-Black

Considere la siguiente secuencia de entrada de elementos que se insertan en un árbol AVL y en un Red-Black:

* `20, 9, 5, 2, 39, 48, 90, 85, 66, 50, 8, 4, 30, 27`

Construya el árbol resultante para cada uno.

### Respuesta

```
                      48
            ┌─────────┴─────────┐
            9                   85
       ┌────┴────┐          ┌───┴───┐
       5         30        66       90
     ┌─┴─┐     ┌─┴─┐     ┌─┘
     2   8    20   39    50
     └─┐      └─┐
       4        27
```

| Nodo | Hijo izquierdo | Hijo derecho |
|:--:|:--:|:--:|
| **48** | 9 | 85 |
| **9** | 5 | 30 |
| **85** | 66 | 90 |
| **5** | 2 | 8 |
| **30** | 20 | 39 |
| **66** | 50 | — |
| **2** | — | 4 |
| **20** | — | 27 |

---

## Ejercicio 3: Tabla hash

Considere la siguiente secuencia de elementos que se insertan en una tabla hash implementada como un vector de 13 elementos (los índices van del 0 al 12):

* `14, 2, 24, 38, 25, 36, 5, 18, 26`

| Función | Definición |
|---|---|
| **Hash principal** | `f(key) = 1 + key % 12` |
| **Hash secundario (Double Hashing)** | `f2(key) = 2 + key % 10` |

Genere el vector resultante después de realizar la inserción de los elementos de la secuencia utilizando:

* Direct Chaining
* Linear Probing
* Quad Probing
* Double Hashing

### Respuesta: Direct Chaining

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Contenido** | — | 24 → 36 | 25 | 14 → 2 → 38 → 26 | — | — | 5 | 18 | — | — | — | — | — |

### Respuesta: Linear Probing

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Valor** | — | 24 | 25 | 14 | 2 | 38 | 36 | 5 | 18 | 26 | — | — | — |

### Respuesta: Quad Probing

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Valor** | — | 24 | 25 | 14 | 2 | 36 | 5 | 38 | 18 | — | — | — | 26 |

### Respuesta: Double Hashing

| Índice | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Valor** | 38 | 24 | 25 | 14 | 18 | — | 5 | 2 | — | 36 | — | 26 | — |

---

## Ejercicio 4: Grafo ponderado

Considere el siguiente grafo:

```
        7
   A ─────────> E
   │ \           \ 11
   │  \ 6         v
22 │   ───> C ───> F
   │         6    ^ ^
   │  16          │ │ 13
   v   ───> G     │ │
   B     \  16    │ │
   │ \    v       │ │
   │  ─────> D ───┘ │
   │    7           │
   └────── 9 ───────┘
```

| Origen | Destino | Peso |
|:--:|:--:|:--:|
| **A** | B | 22 |
| **A** | C | 6 |
| **A** | E | 7 |
| **A** | G | 16 |
| **B** | D | 7 |
| **B** | F | 9 |
| **C** | F | 6 |
| **D** | F | 13 |
| **E** | F | 11 |
| **G** | D | 16 |

Se pide:

* Recorrido BFS y DFS comenzando desde el vértice `A`. Las aristas de cada vértice se procesan en orden alfabético.
* Matriz de adyacencia.
* Lista de adyacencia.
* Ordenamiento topológico.

### Respuesta: recorridos desde `A`

| Recorrido | Resultado |
|---|---|
| **BFS** | `A – B – C – E – G – D – F` |
| **DFS** | `A – B – D – F – C – E – G` |

### Respuesta: matriz de adyacencia

| | **A** | **B** | **C** | **D** | **E** | **F** | **G** |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **A** | 00 | 22 | 6 | 00 | 7 | 00 | 16 |
| **B** | 00 | 00 | 00 | 7 | 00 | 9 | 00 |
| **C** | 00 | 00 | 00 | 00 | 00 | 6 | 00 |
| **D** | 00 | 00 | 00 | 00 | 00 | 13 | 00 |
| **E** | 00 | 00 | 00 | 00 | 00 | 11 | 00 |
| **F** | 00 | 00 | 00 | 00 | 00 | 00 | 00 |
| **G** | 00 | 00 | 00 | 16 | 00 | 00 | 00 |

### Respuesta: costos mínimos desde `A`

| | **A** | **B** | **C** | **D** | **E** | **F** | **G** |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **A** | 0 | 22 | 6 | 29 | 7 | 12 | 16 |

---

## Ejercicio 5: Grafo dirigido

Considere el siguiente grafo:

```
                A
              ^   ^
             /     \
            B ────> C
           / ^ \    ^ ^
          v  |  v  /   \
   D ───> ...  E ──     G
```

| Origen | Destinos |
|:--:|---|
| **B** | A, C, E |
| **C** | A |
| **D** | B, E, F |
| **E** | C, G |
| **F** | B, E, G |
| **G** | C |
| **A** | — |

Se pide:

* Recorrido BFS y DFS comenzando desde el vértice `D`. Las aristas de cada vértice se procesan en orden alfabético.
* Matriz de adyacencia.
* Lista de adyacencia.
* Ordenamiento topológico.

### Respuesta: recorridos desde `D`

| Recorrido | Resultado |
|---|---|
| **BFS** | `D – B – E – F – A – C – G` |
| **DFS** | `D – B – A – C – E – G – F` |

### Respuesta: matriz de adyacencia

| | **A** | **B** | **C** | **D** | **E** | **F** | **G** |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **A** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **B** | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| **C** | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **D** | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| **E** | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| **F** | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| **G** | 0 | 0 | 1 | 0 | 0 | 0 | 0 |

---

## Resumen de la práctica

| Ejercicio | Resultado clave |
|:--:|---|
| **1** | Raíz `24`; subárbol izquierdo con raíz `13` y derecho con raíz `56` |
| **2** | Raíz `48`; subárbol izquierdo con raíz `9` y derecho con raíz `85` |
| **3** | Cuatro vectores de 13 posiciones: Direct Chaining, Linear Probing, Quad Probing y Double Hashing |
| **4** | BFS `A – B – C – E – G – D – F`; DFS `A – B – D – F – C – E – G` |
| **5** | BFS `D – B – E – F – A – C – G`; DFS `D – B – A – C – E – G – F` |