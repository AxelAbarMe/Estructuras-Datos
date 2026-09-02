# 11. Comparativas entre algoritmos de ordenamiento

### Burbuja
- **Comparaciones:** $(n^2 - n) / 2$ en todos los casos (sin optimización) o $n - 1$ en el mejor caso (con bandera de intercambio).
- **Intercambios:** $0$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Información clave:** Algoritmo adaptativo si se usa bandera de control. Es ineficiente debido al alto número de intercambios adyacentes en el peor caso.

### Selección
- **Comparaciones:** $(n^2 - n) / 2$ en todos los casos.
- **Intercambios:** $0$ (Mejor caso), $n - 1$ (Peor caso).
- **Información clave:** Es ideal cuando el costo de escritura/intercambio en memoria es muy alto (ej. memorias Flash), ya que realiza como máximo $n - 1$ intercambios. No es adaptativo ni estable.

### Inserción
- **Comparaciones:** $n - 1$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Intercambios / Desplazamientos:** $0$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Información clave:** Sumamente eficiente para arreglos pequeños o casi ordenados. Sirve de base para algoritmos híbridos como Timsort.

### Quicksort
- **Comparaciones:** $O(n \log n)$ (Mejor y caso promedio), $(n^2 - n) / 2$ (Peor caso).
- **Intercambios:** $O(n \log n)$ en promedio.
- **Información clave:** El rendimiento depende críticamente de la selección del pivote. Utilizar la mediana agrega $O(n)$ adicional por nivel, mientras que seleccionar un elemento aleatorio reduce drásticamente la probabilidad del peor caso manteniendo un rendimiento óptimo en la práctica. In-place respecto a los datos, pero requiere $O(\log n)$ espacio en la pila de llamadas.

### Mergesort
- **Comparaciones:** Entre $\frac{1}{2} n \log_2 n$ y $n \log_2 n - n + 1$.
- **Asignaciones / Copias de memoria:** $O(n \log n)$ debido a los arreglos auxiliares de mezcla.
- **Información clave:** Garantiza siempre $O(n \log n)$ independientemente de la distribución de los datos. No es in-place ($O(n)$ de espacio extra). Ideal para listas enlazadas y ordenamiento externo de archivos masivos.

### Heapsort
- **Comparaciones:** $\approx 2n \log_2 n$ en el peor caso.
- **Intercambios:** $O(n \log n)$ en el proceso de extracción de la raíz.
- **Información clave:** Combina lo mejor del peor caso de Mergesort ($O(n \log n)$ garantizado) con el consumo de memoria de Selección ($O(1)$ espacio extra). No es estable ni adaptativo.

### Counting Sort
- **Comparaciones:** $0$ (Algoritmo no basado en comparaciones).
- **Operaciones totales:** $O(n + k)$, donde $k$ es el rango de los valores ($max - min + 1$).
- **Información clave:** Supera la barrera del $O(n \log n)$, pero requiere $O(n + k)$ espacio adicional. Solo es práctico si el rango $k$ no es significativamente mayor que $n$.

### Radix Sort
- **Comparaciones:** $0$ (Algoritmo no basado en comparaciones).
- **Operaciones totales:** $O(d \cdot (n + k))$, donde $d$ es la cantidad de dígitos/posiciones y $k$ la base numérica (ej. 10 para decimales).
- **Información clave:** Procesa los datos por posiciones (LSD) utilizando Counting Sort como subrutina. Requiere que la subrutina sea estrictamente estable para preservar el orden de las pasadas previas.

---

> **Diferencia de eficiencia en escrituras:** Selección es mejor que Inserción y Burbuja cuando existen limitaciones en escrituras de disco/memoria, debido a que en el peor de los casos realiza solo $n - 1$ intercambios, mientras que Inserción y Burbuja realizan $\frac{n^2 - n}{2}$.

> **Estrategias de pivote en Quicksort:** El funcionamiento y balanceo de las particiones depende del pivote:
> - *Mediana real:* Garantiza particiones equilibradas pero agrega un costo adicional de $O(n)$ por nivel.
> - *Pivote aleatorio:* Tiene un costo computacional despreciable y logra un rendimiento cercano al caso óptimo en la práctica.
