# Comparaciones

### Selección {Comparaciones:  $$\ \frac{n^{2} - n}{2}$$. Intercambios: 0 Mejor, n-1 Peor}
### Inserción {Comparaciones n-1. Intercambios: 0 Mejor,  $$\ \frac{n^{2} - n}{2}$$ Peor}

> Selección es mejor cuando hay limitaciones en escrituras de disco debido a que en el peor de los casos debe solamente realizar n-1 intercambios, mientras que selección realiza  $$\ \frac{n^{2} - n}{2}$$

> Funcionamiento de quicksort depende de la selección del pivote, 2 formas son: {Utilizar mediana, pero agrega O(n) adicional al quicksort} y {Utilizar elemento random que suele tener un rendimiento similar a la elección de la mediana}
