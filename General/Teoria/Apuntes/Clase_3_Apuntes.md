# 3: Lenguajes Interpretados, Git y Herramientas de Desarrollo

## Lenguajes interpretados

* Python
* JavaScript

El código fuente pasa por un intérprete (Virtual Machine Runtime). Esta es la primera diferencia entre un lenguaje interpretado y uno compilado: el intérprete toma una instrucción y genera, dependiendo de la arquitectura (x86-64 o ARM), el **Bytecode** (código máquina solamente de dicha instrucción). Esto se va a la RAM y se envía al CPU a ejecutar.

### Proceso

1. Lee la primera instrucción.
2. Genera el Bytecode.
3. Se dirige a la RAM (el intérprete ya está en memoria), luego al CPU, y se ejecuta.
4. Repetir el paso 1.

### Diferencias, pros y contras

* El lenguaje compilado es más rápido, ya que el interpretado debe realizar todo el proceso previo, mientras que el compilado envía directo de RAM hacia CPU.
* Ventaja del intérprete: es más simple, pero no llega al mismo rendimiento que uno compilado.
* Ventaja del intérprete: corre el mismo código en diferentes arquitecturas (**portabilidad**). El compilado no funciona de esta manera, debido a que el código OBJ puede tener, por ejemplo, un `int x`, y la arquitectura x86-64 genera dicho valor `int` con tamaño de 4 bytes, pero en una arquitectura ARM el valor `int` tendrá un tamaño de 8 bytes.
  * Ejemplo: `x = 23457890130`. En ARM corre correctamente; en Intel ocurre desbordamiento de memoria.

> **Nota adicional:** algunos lenguajes usan un enfoque híbrido, llamado JIT (Just-In-Time compilation), donde el bytecode se compila a código nativo en tiempo de ejecución (ejemplo: la JVM de Java o el motor V8 de JavaScript), buscando acercarse al rendimiento de un compilado sin perder portabilidad.

---

## Git

### Control de versiones

| V1 | → | V2 | → | V3 | → | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

* Centralizar código en un repositorio donde cada programador tiene acceso a dicho código.
* Clonación local del código del repositorio.
* GitHub es el repositorio del código fuente que funciona basado en Git.
* Un **commit** es un historial del estado de los archivos en un momento dado (*snapshot*).
* Git registra solamente los cambios y copia los archivos según si se modifican, para ahorrar espacio.

### Push, Pull y Merge

* **Push**
* **Pull** → Fetch y Merge
* **Merge** → Merge y Rebase
* **Rebase** permite un control de versiones más limpio comparado con el merge.

**Rebase:**

| V1 | → | V2 | → | V3 | → | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

**Merge:**

| V1 | -v | | | → | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| | → | V2 | → | V3 | | |
| V1 | -^ | | | → | V4 |

### Branches

Línea de producción (Main o Master):

| V1 | ← | V2 | ← | V3 | ← | V4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

No se introduce el código hasta que este sea probado y aprobado, por lo que, para que los devs trabajen, se crean **branches**.

### CI/CD

CI/CD (automatizado): Apps | Procesos | QA (Calidad de Software) | Actualización automática de la APP | Es donde se crean los contenedores | Basado en Cloud Computing.

* **Pruebas de unidad (Unit Testing):** creación de funciones para probar la funcionalidad de código.

---

## Metodologías

### Spec-Driven Development

Basado en intención.

Es una metodología donde, antes de escribir código, se redacta una **especificación clara y detallada** de qué debe hacer el sistema (comportamiento esperado, entradas, salidas, restricciones), y dicha especificación se convierte en la fuente de verdad del desarrollo.

* El desarrollo (ya sea manual o asistido por herramientas de IA) se guía estrictamente por lo definido en la especificación, en lugar de improvisar sobre la marcha.
* Busca reducir la ambigüedad: si la intención no está clara desde el inicio, el código resultante tampoco lo estará.
* Es especialmente relevante en el contexto actual de desarrollo asistido por IA, donde una especificación bien redactada permite que un modelo genere código mucho más alineado con lo que realmente se necesita.
* Suele apoyarse en documentos como historias de usuario, diagramas o contratos de API (ejemplo: una especificación OpenAPI/Swagger) definidos **antes** de implementar.

> **Diferencia clave con Test-Driven Development:** en Spec-Driven Development el punto de partida es la *intención* o el *qué* debe hacer el sistema (documentado en lenguaje natural o semi-formal); en TDD el punto de partida es una *prueba automatizada* que valida el *comportamiento* esperado del código.

### Test-Driven Development

Metodología de desarrollo donde las pruebas se escriben **antes** que el código de producción, y dicho código se implementa únicamente con el objetivo de hacer pasar esas pruebas.

#### Ciclo Red-Green-Refactor

1. **Red:** Se escribe primero una prueba de unidad para una funcionalidad que aún no existe. Al ejecutarla, esta falla (color rojo), ya que el código correspondiente todavía no ha sido implementado.
2. **Green:** Se escribe el código mínimo necesario, sin optimizar ni sobre-diseñar, únicamente lo suficiente para que la prueba pase (color verde).
3. **Refactor:** Una vez que la prueba pasa, se mejora y limpia el código (nombres, duplicación, estructura), manteniendo la funcionalidad intacta; las pruebas ya existentes garantizan que no se rompa nada durante este proceso.

Este ciclo se repite por cada nueva funcionalidad o caso a cubrir.

* Se relaciona directamente con las **Pruebas de unidad (Unit Testing)** mencionadas dentro de un flujo de CI/CD: cada vez que se sube un cambio, estas pruebas se ejecutan automáticamente para detectar errores antes de llegar a producción.
* **Ventaja:** al tener pruebas desde el inicio, se genera una red de seguridad que facilita hacer cambios o refactorizaciones futuras con mayor confianza.
* **Desventaja:** puede aumentar el tiempo inicial de desarrollo, ya que exige escribir pruebas antes de tener funcionalidad real.

> **Diferencia clave con Spec-Driven Development:** en TDD el punto de partida es una prueba automatizada y ejecutable que valida un comportamiento específico del código; en Spec-Driven Development el punto de partida es una especificación en lenguaje natural o semi-formal que documenta la intención general del sistema, sin necesariamente ser ejecutable como prueba.
---

## Git — Línea de Comandos

```bash
// Clonar Git
git clone https://github.com/josecalvosuarez/estructuras-de-datos.git

// Visualizar directorios
dir

// Moverse entre directorios
cd estructuras-de-datos

// Abrir Visual Studio Code
code .
```

---

## Debugger

* **Breakpoints**
* **Run** → Ejecuta directo.
* **Debug** → Activa un flag (1 bit) en el CPU → Ejecuta paso a paso.
* **Step Over (F10)** → Ejecuta la función sin entrar a ella.
* **Step Into (F11)** → Si encuentra una llamada, ejecuta línea por línea dentro de ella.
* **Call Stack** → Indica el stack, las llamadas de las funciones.
* **Variables** → Indica el `.data` y `.bss`.
* **Watch** → Agrega expresiones en tiempo real.

---

## Comandos de Git

### Iniciar y clonar

```bash
# Start a new repo
git init

# Clone an existing repo
git clone <url>
```

### Staging y cambios

```bash
# Add untracked file or unstaged changes
git add <file>

# Add all untracked files and unstaged changes
git add .

# Choose which parts of a file to stage
git add -p

# Move file
git mv <old> <new>

# Delete file
git rm <file>

# Tell Git to forget about a file without deleting it
git rm --cached <file>

# Unstage one file
git reset <file>

# Unstage everything
git reset

# Check what you added
git status
```

### Commits

```bash
# Make a commit (and open text editor to write message)
git commit

# Make a commit
git commit -m 'message'

# Commit all unstaged changes
git commit -am 'message'
```

### Branches

```bash
# Switch branches
git switch <name>
OR
git checkout <name>

# Create a branch
git switch -c <name>
OR
git checkout -b <name>

# List branches
git branch

# List branches by most recently committed to
git branch --sort=-committerdate

# Delete a branch
git branch -d <name>

# Force delete a branch
git branch -D <name>
```

### Diffs

```bash
# Diff all staged and unstaged changes
git diff HEAD

# Diff just staged changes
git diff --staged

# Diff just unstaged changes
git diff

# Show diff between a commit and its parent
git show <commit>

# Diff two commits
git diff <commit> <commit>

# Diff one file since a commit
git diff <commit> <file>

# Show a summary of a diff
git diff <commit> --stat
git show <commit> --stat
```

### Restaurar y eliminar cambios

```bash
# Delete unstaged changes to one file
git restore <file>
OR
git checkout <file>

# Delete all staged and unstaged changes to one file
git restore --staged --worktree <file>
OR
git checkout HEAD <file>

# Delete all staged and unstaged changes
git reset --hard

# Delete untracked files
git clean

# 'Stash' all staged and unstaged changes
git stash
```

### Reescribir historial

```bash
# "Undo" the most recent commit (keep your working directory the same)
git reset HEAD^

# Squash the last 5 commits into one
git rebase -i HEAD~5

# Undo a failed rebase
git reflog BRANCHNAME
git reset --hard <commit>

# Change a commit message (or add a file you forgot)
git commit --amend
```

### Historial

```bash
# Look at a branch's history
git log main
git log --graph main
git log --oneline

# Show every commit that modified a file
git log <file>

# Show every commit that modified a file, including before it was renamed
git log --follow <file>

# Find every commit that added or removed some text
git log -G banana

# Show who last changed each line of a file
git blame <file>
```

### Rebase y Merge

```bash
# Combine with rebase
git switch banana
git rebase main

# Combine with merge
git switch main
git merge banana

# Combine with squash merge
git switch main
git merge --squash banana
git commit

# Bring a branch up to date with another branch (aka "fast-forward merge")
git switch main
git merge banana

# Copy one commit onto the current branch
git cherry-pick <commit>

# Get the version of a file from another commit
git checkout <commit> <file>
OR
git restore <file> --source <commit>
```

### Remotos

```bash
# Add a remote
git remote add <name> <url>

# Push the main branch to the remote origin
git push origin main

# Push the current branch to its remote "tracking branch"
git push

# Push a branch that you've never pushed before
git push -u origin <name>

# Force push
git push --force-with-lease

# Push tags
git push --tags

# Fetch changes (but don't change any of your local branches)
git fetch origin main

# Fetch changes and then rebase your current branch
git pull --rebase

# Fetch changes and then merge them into your current branch
git pull origin main
OR
git pull
```

### Configuración

```bash
# Set a config option
git config user.name 'Your Name'

# Set option globally
git config --global ...

# Add an alias
git config alias.st status

# See all possible config options
man git-config
```
