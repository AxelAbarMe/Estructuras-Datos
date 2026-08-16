from maze import MAZE

def find_exit(maze, x, y, path=None):
    if path is None:
        path = []

    # Agregamos el print aquí para ver la ruta en cada paso recursivo:
    print(path)
    
    # Out of bounds or wall
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == "X":
        return []
    
    # Found exit
    if maze[x][y] == "E":
        return [path + [(x, y)]]

    # Already visited 
    if (x, y) in path: 
        return []
    # Con comentar estas dos lineas, el programa se rompe,
    # empieza a imprimir repetidamente los mismos 
    # pares de coordenadas rebotando de ida y vuelta.
    # RecursionError: maximum recursion depth exceeded while getting the repr of an object

    all_solutions = [] # Para el desafio de mostrar todas las soluciones
    
    # Explore neighbors (down, right, up, left)
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        
        # new_path = find_exit(maze, x+dx, y+dy, path + [(x, y)])
        # if new_path:
        #    return new_path
        
        solutions = find_exit(maze, x+dx, y+dy, path + [(x, y)])
        all_solutions.extend(solutions)

    return all_solutions

if __name__ == "__main__":
    # solution = find_exit(MAZE, 0, 0)
    # print("Solution:", solution)
    
    solutions = find_exit(MAZE, 0, 0)
    print(f"Se encontraron {len(solutions)} solución(es):")
    for sol in solutions:
        print(sol)
