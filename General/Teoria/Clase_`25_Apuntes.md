Cluster Kubernetes / Docker

ks cluster config --cluster (ID) --admin

get pods -n
get services -n
port-forward service id-service -n 
get secret -n

Definicion de archivos mostrados en el CLI hechos con YAML

# Topological Sorting

Problemas relacionados con orden

Ejwmwplo: Grafo con el mapa de todos los cursos de la carrera

Permite en base a un grafo de dependencias, ordenar los elementos

Resolver problemas que tienen que ver con dependencias

Necesario Orden (Requisito)

* Nodo K -> Nodo J;  Donde no se accede a J sin anter pasar primero por K

pip install networkx <- libc <- xyz (Dependency Hell)

DAG (Orden topológico solo se puede utilizar usando este tipo de grafo) (Debe ser dirigido no ciclico)

* D -> Directed
* A -> Acyclic
* G -> Graph

Para realizar el ordenamiento topológico, se debe de utilizar un recorrido DFS

* A -> C
* B -> C
* C -> D -> E
* D -> E -> F
* E -> H
* F -> H
* H -> ∅

Hay requisito especial, se deben de verificar todos los vertices, existen varias soluciones posibles.

Empezar por nodos sin dependencias

Utilizando el ejemplo anterior.

Dead End. Cambio necesario para que funcione este ordenamiento.

Utilizando una lista enlazada o vector como estructura con tamaño 7

Visita en el pop

* Se empieza desde nodo sin dependencias
* Avanza normal con DFS
* Cuando encuentra Dead end, se ingresa al final del vector o en la última posición disponible
* Se regresa al nodo anterior y se comprueban nuevas adyacencias.
* Repetir con cada dead end encontrado

Uno de los posibles resultados finales:

|Resultado 1|B|A|C|D|F|E|H|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
|Resultado 2|A|B|C|D|F|E|H|
|Resultado 3|B|A|C|D|E|F|H|



