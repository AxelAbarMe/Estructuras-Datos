#  Lenguajes interpretados

- Python
- Javascript

El código fuente pasa por un intérprete (Virtual machine runtime). Primera diferencia entre lenguaje interpretado y compilado, el intérprete toma una instrucción y genera dependiendo de la arquitectura (x86 - 64 o ARM) el Bytecode (Código máquina solamente de dicha instrucción). Esto se va a RAM y se envía al CPU a ejecutar.

### Proceso

- Lee primera instrucción
- Genera Bytecode
- Se dirige a la RAM (Intérprete ya está en memoria), luego CPU y se ejecuta
- Repetir paso 1.

## Diferencias, pros y contras

- Lenguaje compilado es más rápido, ya que interpretado debe dirigirse a hacer todo el proceso previo, mientras que compilado envía directo de RAM hacia CPU.

- Ventaja de intérprete es que es más simple, pero no llega al mismo rendimiento que uno compilado.

- Ventaja intérprete es que corre el mismo código en diferentes arquitecturas (Portabilidad). Compilado no funciona de está manera, debido a que el código OBJ, puede tener por ejemplo un "int x" y la arquitectura x86 - 64 genera dicho valor int con tamaño de 4 Bytes, pero en una arquitectura ARM el valor int tendrá un tamaño de 8 Bytes.

- x = 23457890130. En ARM corre correctamente, en Intel ocurre desbordamiento de memoria.

# Git

### Control de versiones

| V1 | -> | V2 | -> | V3 | -> | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

- Centralizar código en un repositorio donde cada programador tiene acceso a dicho código.

- Clonación local de código del repositorio.

- Github es el repositorio del código fuente que funciona basado en Git.

- Commit es un historial del estado de los archivos en un momento dado (Snapshot).

- Git registra solamente los cambios y copia los archivos según si se modifican para almacenar espacio.

- Push

- Pull -> Fetch y Merge

- Merge -> Merge y Rebase

- Rebase permite un control de versiones más limpio comparado con el merge.

Rebase:
| V1 | -> | V2 | -> | V3 | -> | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

Merge:

| V1 | -v | | | -> |  V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| | -> | V2 | -> | V3 |  |  |
| V1 | -^ | |  | -> | V4 |

- Branches

Linea de producción (Main o bien [Master] )

| V1 | <- | V2 | <- | V3 | <- | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

No se introduce el código hasta que este sea probado y aprobado, por lo que para que los devs trabajen se crean branches.

- CI/CD (Automatizado) Apps | Procesos | QA (Calidad de Software) | Actualización automática de la APP | Es donde se crea los contenedores | Basado en Cloud Computing.

- Pruebas de unidad (Unit testing). Creación de funciones para probar funcionalidad de código.

### Comandos
##### Git clone URL

# Metodologias

## Spec-Drivin Development

Basado en intención

## Test-Drivin Development

# Git Command Line

```
// Clonar Git
git clone https://github.com/josecalvosuarez/estructuras-de-datos.git

//Visualizar directorios
dir

//Moverse entre directorios
cd estructuras-de-datos

//Abrir Visual Studio Code
code .
```
# Debugger

- Breakpoints.
- Run -> Ejecuta directo.
- Debug -> Activa flag (1 bit) en el CPU -> Ejecuta paso a paso.
- Step Over (F10) -> Ejecuta la función sin entrar a ella
- Step Into (F11) -> Si encuentra, ejecute linea por linea
- Call Stack -> Indica el stack, las llamadas de las funciones.
- Variables -> Indica el .data y .bss
- Watch -> Agrega expresiones en tiempo real


