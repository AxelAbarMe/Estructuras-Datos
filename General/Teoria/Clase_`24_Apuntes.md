## 4 Conectar las sedes mediante expansión mínima

El árbol de expansión mínima conecta todos los nodos, evita ciclos y minimiza la suma de los pesos seleccionados. El cuaderno aplica Kruskal a G, cuyos pesos son geodésicos. Un árbol conectado con ocho nodos debe tener siete aristas. Su objetivo es reducir el costo total de conexión, no construir un itinerario para visitar todas las sedes.

### Procedimiento de Kruskal

1. Ordene las 28 aristas de menor a mayor peso.

2. Comience con cada nodo en un componente separado.

3. Acepte una arista cuando una dos componentes diferentes. Si sus extremos ya están conectados, descártela porque produciría un ciclo.

4. Deténgase cuando se acepten siete aristas y compruebe el resultado con minimum_spanning_tree.


## 7 Encontrar un camino mínimo con Dijkstra

Dijkstra encuentra un camino de menor suma de pesos entre un origen y un destino dentro del grafo considerado. Los pesos deben ser finitos y no negativos. En este apartado se utiliza H y, por tanto, el costo representa kilómetros geodésicos. El algoritmo no exige visitar todos los campus.

### Procedimiento guiado

1. Establezca distancia provisional 0 para el origen e infinito para los demás nodos.

2. Seleccione, mediante la cola de prioridad, el nodo pendiente de menor distancia provisional y confirme su valor.

3. Para cada vecino, calcule una propuesta sumando la distancia hasta el nodo actual y el peso de la arista.

4. Si la propuesta es menor, actualice la distancia y el predecesor del vecino. Esta actualización se denomina relajación.

5. Repita hasta confirmar el destino o agotar los nodos alcanzables. Reconstruya el camino siguiendo los predecesores en sentido inverso.

En el código, pendientes es la cola de prioridad; distancias almacena los mejores costos conocidos; predecesor permite reconstruir el camino; confirmados evita procesar de nuevo nodos ya resueltos. La tabla seguimiento_dijkstra registra cada confirmación. Un valor inf indica que todavía no se ha encontrado un camino, no una distancia física infinita.
