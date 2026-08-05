# Lenguajes interpretados

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

# Comandos
```
Start a new repo:
git init

Clone an existing repo:
git clone <url>

Add untracked file or unstaged changes:
git add <file>

Add all untracked files and unstaged changes:
git add .

Choose which parts of a file to stage:
git add -p

Move file:
git mv <old> <new>

Delete file:
git rm <file>

Tell Git to forget about a file without deleting it:
git rm --cached <file>

Unstage one file:
git reset <file>

Unstage everything:
git reset

Check what you added:
git status

Make a commit (and open text editor to write message):
git commit

Make a commit:
git commit -m 'message'

Commit all unstaged changes:
git commit -am 'message'

Switch branches:
git switch <name>
OR
git checkout <name>

Create a branch:
git switch -c <name>
OR
git checkout -b <name>

List branches:
git branch

List branches by most recently committed to:
git branch --sort=-committerdate

Delete a branch:
git branch -d <name>

Force delete a branch:
git branch -D <name>

Diff all staged and unstaged changes:
git diff HEAD

Diff just staged changes:
git diff --staged

Diff just unstaged changes:
git diff

Show diff between a commit and its parent:
git show <commit>

Diff two commits:
git diff <commit> <commit>

Diff one file since a commit:
git diff <commit> <file>

Show a summary of a diff:
git diff <commit> --stat
git show <commit> --stat

Delete unstaged changes to one file:
git restore <file>
OR
git checkout <file>

Delete all staged and unstaged changes to one file:
git restore --staged --worktree <file>
OR
git checkout HEAD <file>

Delete all staged and unstaged changes:
git reset --hard

Delete untracked files:
git clean

'Stash' all staged and unstaged changes:
git stash

"Undo" the most recent commit (keep your working directory the same):
git reset HEAD^

Squash the last 5 commits into one:
git rebase -i HEAD~5

Undo a failed rebase:
git reflog BRANCHNAME
git reset --hard <commit>

Change a commit message (or add a file you forgot):
git commit --amend

Look at a branch's history:
git log main
git log --graph main
git log --oneline

Show every commit that modified a file:
git log <file>

Show every commit that modified a file, including before it was renamed:
git log --follow <file>

Find every commit that added or removed some text:
git log -G banana

Show who last changed each line of a file:
git blame <file>

Combine with rebase:
git switch banana
git rebase main

Combine with merge:
git switch main
git merge banana

Combine with squash merge:
git switch main
git merge --squash banana
git commit

Bring a branch up to date with another branch (aka "fast-forward merge"):
git switch main
git merge banana

Copy one commit onto the current branch:
git cherry-pick <commit>

Get the version of a file from another commit:
git checkout <commit> <file>
OR
git restore <file> --source <commit>

Add a remote:
git remote add <name> <url>

Push the main branch to the remote origin:
git push origin main

Push the current branch to its remote "tracking branch":
git push

Push a branch that you've never pushed before:
git push -u origin <name>

Force push:
git push --force-with-lease

Push tags:
git push --tags

Fetch changes (but don't change any of your local branches):
git fetch origin main

Fetch changes and then rebase your current branch:
git pull --rebase

Fetch changes and then merge them into your current branch:
git pull origin main
OR
git pull

Set a config option:
git config user.name 'Your Name'

Set option globally:
git config --global ...

Add an alias:
git config alias.st status

See all possible config options:
man git-config
```


