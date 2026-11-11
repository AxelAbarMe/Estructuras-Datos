# =========================================
# SEGMENTO 24: DOCKER, KUBERNETES Y ORDENAMIENTO TOPOLÓGICO
# =========================================

# Contenedores y Docker

Un **contenedor** es un proceso aislado que se ejecuta con su propio sistema de archivos, red y recursos, pero **comparte el núcleo (kernel)** del sistema operativo anfitrión. **Docker** es la herramienta que permite construir, distribuir y ejecutar contenedores.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Imagen** | Plantilla de solo lectura con el programa, sus bibliotecas y su configuración | `python:3.11-slim` |
| **Contenedor** | Instancia en ejecución de una imagen | Un servicio web corriendo en el puerto 8000 |
| **Dockerfile** | Archivo de texto con las instrucciones para construir una imagen | `FROM`, `COPY`, `RUN`, `CMD` |
| **Registro (registry)** | Repositorio donde se almacenan y descargan imágenes | Docker Hub, GitHub Container Registry |
| **Volumen** | Almacenamiento que persiste fuera del contenedor | Base de datos que sobrevive a reinicios |
| **Red (network)** | Red virtual que comunica contenedores entre sí | Servicio web que se conecta a una base de datos |

> Un contenedor **no es una máquina virtual**: no incluye un sistema operativo completo, por eso arranca en segundos y consume mucho menos memoria.

## Contenedor frente a máquina virtual

| Aspecto | Máquina virtual | Contenedor |
|---|---|---|
| **Aislamiento** | Hardware virtualizado (hipervisor) | Procesos aislados por el kernel |
| **Sistema operativo** | Uno completo por cada VM | Comparte el kernel del anfitrión |
| **Tamaño** | Gigabytes | Megabytes |
| **Arranque** | Minutos | Segundos |
| **Portabilidad** | Media | Alta (la imagen lleva sus dependencias) |
| **Problema que resuelve** | Separar sistemas operativos completos | «En mi máquina sí funciona» |

## ¿Cómo funciona un contenedor?

El aislamiento no es magia: lo proporcionan funciones del kernel de Linux.

| Mecanismo | Función |
|---|---|
| **Namespaces** | Aíslan lo que el proceso *ve*: procesos (`pid`), red (`net`), sistema de archivos (`mnt`), nombre de equipo (`uts`), usuarios (`user`) |
| **cgroups** | Limitan lo que el proceso *consume*: CPU, memoria, entrada/salida |
| **Sistema de archivos por capas** | La imagen se compone de capas de solo lectura; el contenedor agrega una capa de escritura encima |
| **Runtime (`containerd`, `runc`)** | Componente que crea y ejecuta realmente el contenedor |

### Arquitectura de Docker

| Componente | Qué hace |
|---|---|
| **Cliente (`docker`)** | Comando que escribe el usuario |
| **Daemon (`dockerd`)** | Servicio en segundo plano que construye imágenes y administra contenedores |
| **API de Docker** | Canal por el que el cliente le envía órdenes al daemon |
| **Registro** | Origen y destino de las imágenes (`pull` y `push`) |

```
docker (cliente) ──> dockerd (daemon) ──> containerd ──> runc ──> contenedor
                          │
                          └──> Registro (Docker Hub) : pull / push
```

### Ciclo de vida

| Etapa | Comando | Qué ocurre |
|---|---|---|
| **Construir** | `docker build` | Se crea una imagen a partir del Dockerfile |
| **Descargar** | `docker pull` | Se obtiene una imagen del registro |
| **Ejecutar** | `docker run` | Se crea e inicia un contenedor |
| **Detener** | `docker stop` | Se envía la señal de terminación al proceso |
| **Eliminar** | `docker rm` | Se borra el contenedor (la imagen permanece) |
| **Publicar** | `docker push` | Se sube la imagen al registro |

* Las capas se **almacenan en caché**: si una instrucción del Dockerfile no cambió, Docker reutiliza su capa y no la reconstruye.
* Por eso conviene copiar primero lo que cambia poco (dependencias) y al final lo que cambia mucho (código).

## Instalación de Docker

| Requisito | Descripción |
|---|---|
| **Linux** | Docker Engine se instala directamente |
| **Windows** | Docker Desktop con WSL 2 activado |
| **macOS** | Docker Desktop |
| **Virtualización** | Debe estar habilitada en la BIOS/UEFI (Windows y macOS) |

```bash
# Ubuntu / Debian: instalación con el script oficial
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Permitir usar docker sin sudo (cerrar y abrir sesión después)
sudo usermod -aG docker $USER

# Verificar la instalación
docker --version
docker run hello-world
```

## Dockerfile

```dockerfile
# Imagen base
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Dependencias primero (aprovecha la caché de capas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código de la aplicación
COPY . .

# Variable de entorno y puerto documentado
ENV PUERTO=8000
EXPOSE 8000

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "main.py"]
```

| Instrucción | Qué hace |
|---|---|
| **`FROM`** | Define la imagen base |
| **`WORKDIR`** | Establece el directorio de trabajo |
| **`COPY`** | Copia archivos del anfitrión a la imagen |
| **`RUN`** | Ejecuta un comando **durante la construcción** y crea una capa |
| **`ENV`** | Define variables de entorno |
| **`EXPOSE`** | Documenta el puerto en el que escucha la aplicación (no lo publica) |
| **`CMD`** | Comando por defecto **al iniciar** el contenedor |
| **`ENTRYPOINT`** | Programa fijo que se ejecuta; `CMD` le aporta argumentos |

## Qué se configura en Docker

| Qué se configura | Cómo | Ejemplo |
|---|---|---|
| **Puertos** | `-p anfitrión:contenedor` | `-p 8080:8000` |
| **Variables de entorno** | `-e` o `--env-file` | `-e PUERTO=8000` |
| **Volúmenes** | `-v origen:destino` | `-v datos:/var/lib/datos` |
| **Redes** | `--network` | `--network mi-red` |
| **Límites de recursos** | `--memory`, `--cpus` | `--memory 512m` |
| **Reinicio automático** | `--restart` | `--restart unless-stopped` |
| **Daemon** | `/etc/docker/daemon.json` | Registros, driver de logs, directorio de datos |

* **Puerto publicado**: sin `-p`, el contenedor es alcanzable solo desde dentro de la red de Docker.
* **Volumen**: lo que se escribe dentro del contenedor **se pierde** al eliminarlo, salvo que esté en un volumen.

### Comandos más usados

| Comando | Qué hace |
|---|---|
| `docker build -t nombre:1.0 .` | Construye una imagen con etiqueta |
| `docker run -d -p 8080:8000 nombre:1.0` | Ejecuta en segundo plano publicando un puerto |
| `docker ps` / `docker ps -a` | Lista contenedores activos / todos |
| `docker logs -f <id>` | Sigue los registros de salida |
| `docker exec -it <id> sh` | Abre una terminal dentro del contenedor |
| `docker images` | Lista imágenes locales |
| `docker stop <id>` / `docker rm <id>` | Detiene / elimina un contenedor |
| `docker volume ls` | Lista volúmenes |

## Docker Compose

Herramienta para definir y ejecutar **varios contenedores** a la vez con un solo archivo YAML.

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "8080:8000"
    environment:
      - BD_HOST=bd
    depends_on:
      - bd

  bd:
    image: postgres:16
    environment:
      - POSTGRES_PASSWORD=secreto
    volumes:
      - datos:/var/lib/postgresql/data

volumes:
  datos:
```

| Comando | Qué hace |
|---|---|
| `docker compose up -d` | Crea e inicia todos los servicios |
| `docker compose down` | Detiene y elimina los servicios |
| `docker compose logs -f` | Sigue los registros de todos los servicios |

* Compose coloca los servicios en una red común: `api` alcanza a la base de datos con el nombre `bd`.
* Compose sirve para **un solo equipo**; para muchos equipos y alta disponibilidad se usa un orquestador como Kubernetes.

---

# Kubernetes

**Kubernetes** (K8s) es un **orquestador de contenedores**: automatiza el despliegue, el escalado y la recuperación de aplicaciones en contenedores sobre un conjunto de máquinas.

| Problema | Cómo lo resuelve Kubernetes |
|---|---|
| **Un contenedor se cae** | Lo reinicia o crea otro (autorreparación) |
| **Aumenta la carga** | Escala el número de réplicas |
| **Actualizar sin interrumpir** | Actualización gradual (*rolling update*) y reversión |
| **Muchos servicios que se comunican** | Descubrimiento de servicios y balanceo de carga |
| **Configuración y claves** | `ConfigMap` y `Secret` separados de la imagen |
| **Distribuir carga entre máquinas** | El planificador asigna cada Pod a un nodo con recursos |

> Idea central: el usuario **declara el estado deseado** («quiero 3 réplicas de esta imagen») y Kubernetes trabaja continuamente para que el estado real coincida con él.

## Arquitectura de un clúster

| Componente | Dónde | Función |
|---|---|---|
| **API Server** | Plano de control | Puerta de entrada: todo (CLI, componentes) pasa por él |
| **etcd** | Plano de control | Base de datos clave-valor con el estado completo del clúster |
| **Scheduler** | Plano de control | Decide en qué nodo se ejecuta cada Pod |
| **Controller Manager** | Plano de control | Compara estado deseado con estado real y corrige |
| **kubelet** | Cada nodo | Agente que crea y vigila los contenedores del nodo |
| **kube-proxy** | Cada nodo | Reglas de red para que los Services lleguen a los Pods |
| **Runtime de contenedores** | Cada nodo | Ejecuta los contenedores (`containerd`) |

```
          PLANO DE CONTROL                         NODOS (workers)
  ┌─────────────────────────────┐        ┌─────────────────────────────┐
  │ API Server ◄──► etcd        │        │ kubelet  kube-proxy         │
  │ Scheduler  Controller Mgr   │ ◄────► │ [Pod] [Pod] [Pod]           │
  └─────────────────────────────┘        └─────────────────────────────┘
              ▲
              │  kubectl (CLI del usuario)
```

## Objetos principales

| Objeto | Qué es | Detalle |
|---|---|---|
| **Pod** | Unidad mínima de ejecución | Uno o más contenedores que comparten red y almacenamiento; es **efímero** |
| **Deployment** | Gestiona un conjunto de Pods idénticos | Define réplicas, imagen y estrategia de actualización |
| **Service** | Punto de acceso estable a un grupo de Pods | Los Pods cambian de IP; el Service mantiene un nombre y una IP fija |
| **Namespace** | Partición lógica del clúster | Separa proyectos o ambientes (`-n <namespace>`) |
| **ConfigMap** | Configuración no sensible | Variables, archivos de configuración |
| **Secret** | Datos sensibles | Contraseñas, tokens, certificados |
| **Ingress** | Reglas de entrada HTTP/HTTPS desde fuera | Enrutamiento por dominio o ruta |
| **PersistentVolume / PVC** | Almacenamiento persistente | El Pod solicita almacenamiento mediante un *claim* |

### Tipos de Service

| Tipo | Alcance | Uso |
|---|---|---|
| **ClusterIP** | Solo dentro del clúster (por defecto) | Comunicación entre servicios internos |
| **NodePort** | Un puerto abierto en cada nodo | Pruebas y acceso básico externo |
| **LoadBalancer** | Balanceador del proveedor de nube | Exponer un servicio a internet |

## Instalación

| Herramienta | Para qué sirve |
|---|---|
| **`kubectl`** | CLI para comunicarse con cualquier clúster (siempre necesaria) |
| **minikube** | Clúster local de un solo nodo para aprender |
| **kind** | Clúster local usando contenedores de Docker como nodos |
| **Clúster administrado** | Servicio de nube (EKS, GKE, AKS) o clúster del curso |

```bash
# Instalar kubectl (Linux)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client

# Clúster local de práctica con minikube (requiere Docker)
minikube start --driver=docker
kubectl get nodes
```

## Configuración de acceso: kubeconfig

`kubectl` sabe a qué clúster conectarse leyendo el archivo **kubeconfig** (por defecto `~/.kube/config`).

| Sección | Qué contiene |
|---|---|
| **`clusters`** | Dirección del API Server y su certificado |
| **`users`** | Credenciales (certificado, token) |
| **`contexts`** | Combinación clúster + usuario + namespace por defecto |
| **`current-context`** | Contexto que se usa actualmente |

```yaml
apiVersion: v1
kind: Config
clusters:
  - name: mi-cluster
    cluster:
      server: https://203.0.113.10:6443
      certificate-authority-data: <base64>
users:
  - name: admin
    user:
      token: <token>
contexts:
  - name: mi-contexto
    context:
      cluster: mi-cluster
      user: admin
      namespace: default
current-context: mi-contexto
```

| Comando | Qué hace |
|---|---|
| `kubectl config get-contexts` | Lista los contextos disponibles |
| `kubectl config use-context <nombre>` | Cambia de clúster |
| `kubectl config current-context` | Muestra el contexto activo |

## Conexión al clúster del curso

```bash
# Obtiene la configuración de acceso (kubeconfig) del clúster indicado por su ID,
# con credenciales de administrador
ks cluster config --cluster <ID> --admin
```

| Parte | Significado |
|---|---|
| **`ks cluster config`** | Genera la configuración de acceso al clúster |
| **`--cluster <ID>`** | Identificador del clúster al que se desea conectar |
| **`--admin`** | Solicita credenciales con permisos de administrador |

* Después de ejecutarlo, `kubectl` queda apuntando al clúster y ya se pueden consultar sus recursos.
* Un kubeconfig de administrador da control total: **no se comparte ni se sube al repositorio**.

## Comandos de consulta del CLI

| Comando | Qué hace |
|---|---|
| `kubectl get pods -n <namespace>` | Lista los Pods de un namespace |
| `kubectl get services -n <namespace>` | Lista los Services de un namespace |
| `kubectl port-forward service/<id>-service <local>:<remoto> -n <namespace>` | Redirige un puerto local hacia un Service del clúster |
| `kubectl get secret -n <namespace>` | Lista los Secrets de un namespace |

```bash
# Pods y servicios de un namespace
kubectl get pods -n mi-namespace
kubectl get services -n mi-namespace

# Acceder a un servicio del clúster desde localhost:8080
kubectl port-forward service/id-service 8080:80 -n mi-namespace

# Secrets: listar, ver y decodificar un valor
kubectl get secret -n mi-namespace
kubectl get secret mi-secreto -n mi-namespace -o yaml
kubectl get secret mi-secreto -n mi-namespace -o jsonpath='{.data.clave}' | base64 -d
```

| Opción | Qué hace |
|---|---|
| **`-n <namespace>`** | Indica el namespace; sin ella se usa el predeterminado |
| **`-o yaml`** | Muestra el objeto completo en YAML |
| **`-o wide`** | Agrega columnas como IP y nodo |
| **`port-forward`** | Túnel temporal; se cierra al terminar el comando |

* `port-forward` es para **depurar y probar**, no para exponer un servicio de forma permanente.
* Un Secret **no está cifrado**: sus valores están en `base64`, que es solo una codificación reversible.

## Archivos YAML: definición de los recursos

Todo lo que se consulta con el CLI está **definido en archivos YAML** (manifiestos). Se aplican con `kubectl apply -f archivo.yaml`.

| Campo | Qué indica |
|---|---|
| **`apiVersion`** | Versión de la API del objeto |
| **`kind`** | Tipo de objeto (`Deployment`, `Service`, `Secret`...) |
| **`metadata`** | Nombre, namespace y etiquetas (`labels`) |
| **`spec`** | Estado deseado del objeto |

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: id-app
  namespace: mi-namespace
spec:
  replicas: 3
  selector:
    matchLabels:
      app: id-app
  template:
    metadata:
      labels:
        app: id-app
    spec:
      containers:
        - name: web
          image: mi-usuario/mi-app:1.0
          ports:
            - containerPort: 8000
          env:
            - name: CLAVE
              valueFrom:
                secretKeyRef:
                  name: mi-secreto
                  key: clave
          resources:
            limits:
              memory: "256Mi"
              cpu: "500m"
```

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: id-service
  namespace: mi-namespace
spec:
  type: ClusterIP
  selector:
    app: id-app          # agrupa los Pods con esta etiqueta
  ports:
    - port: 80           # puerto del Service
      targetPort: 8000   # puerto del contenedor
```

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mi-secreto
  namespace: mi-namespace
type: Opaque
stringData:
  clave: "valor-secreto"
```

| Relación | Cómo se conecta |
|---|---|
| **Service → Pods** | Por `selector` y `labels`: el Service envía tráfico a los Pods con la etiqueta indicada |
| **Deployment → Pods** | La plantilla `template` define los Pods que mantiene |
| **Pod → Secret** | Mediante `secretKeyRef` o montando el Secret como archivo |

### Comandos de gestión

| Comando | Qué hace |
|---|---|
| `kubectl apply -f archivo.yaml` | Crea o actualiza los recursos del archivo |
| `kubectl delete -f archivo.yaml` | Elimina los recursos del archivo |
| `kubectl describe pod <pod> -n <ns>` | Detalle y eventos de un Pod (útil para errores) |
| `kubectl logs <pod> -n <ns>` | Registros de salida del contenedor |
| `kubectl exec -it <pod> -n <ns> -- sh` | Terminal dentro del Pod |
| `kubectl scale deployment <nombre> --replicas=5 -n <ns>` | Cambia el número de réplicas |
| `kubectl rollout undo deployment <nombre> -n <ns>` | Revierte la última actualización |

## Docker frente a Kubernetes

| Aspecto | Docker | Kubernetes |
|---|---|---|
| **Qué hace** | Construye y ejecuta contenedores | Orquesta contenedores en muchos equipos |
| **Alcance** | Un equipo | Un clúster de nodos |
| **Escalado y recuperación** | Manual | Automático |
| **Configuración** | Dockerfile, `docker run`, Compose | Manifiestos YAML declarativos |
| **Relación** | Produce la imagen | Ejecuta la imagen |

## Resumen de contenedores

| Idea | Resumen |
|---|---|
| **Contenedor** | Proceso aislado con namespaces y cgroups, comparte el kernel |
| **Imagen** | Plantilla por capas, construida desde un Dockerfile |
| **Docker Compose** | Varios contenedores en un equipo con un YAML |
| **Kubernetes** | Orquestador que mantiene el estado deseado de un clúster |
| **Pod / Deployment / Service** | Ejecución, réplicas y acceso estable |
| **kubeconfig** | Archivo que indica a `kubectl` cómo conectarse al clúster |
| **YAML** | Formato en que se definen todos los recursos |
| **Secret** | Datos sensibles, codificados en `base64`, no cifrados |

---

# Ordenamiento Topológico (Topological Sorting)

Un **ordenamiento topológico** es una secuencia de todos los vértices de un grafo dirigido en la que, para cada arista `(K, J)`, el vértice `K` aparece **antes** que `J`. Sirve para resolver problemas donde existe un **orden de requisito**.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Dependencia** | Un elemento exige que otro ocurra antes | Nodo `K -> Nodo J`: no se accede a `J` sin pasar primero por `K` |
| **Orden topológico** | Lista de todos los nodos que respeta todas las dependencias | `B, A, C, D, F, E, H` |
| **Fuente** | Nodo sin dependencias (ninguna arista entra) | `A` y `B` |
| **Sumidero (*dead end*)** | Nodo sin salidas | `H -> ∅` |

* Ejemplo clásico: el grafo con el mapa de **todos los cursos de una carrera**; un curso solo se matricula si sus requisitos ya fueron aprobados.
* Otros usos: orden de compilación de módulos, orden de instalación de paquetes, planificación de tareas, orden de evaluación de fórmulas en una hoja de cálculo.

## Dependencias y el «Dependency Hell»

```
pip install networkx  <-  libc  <-  xyz
```

* Instalar un paquete exige antes instalar sus dependencias, y estas a su vez las suyas.
* Cuando las dependencias son numerosas, entrecruzadas o incompatibles se habla de **Dependency Hell**.
* Un gestor de paquetes resuelve esto calculando un orden topológico de las dependencias.

## Requisito: el grafo debe ser un DAG

El ordenamiento topológico **solo existe** en un grafo con estas características:

| Letra | Significado | Descripción |
|:--:|---|---|
| **D** | *Directed* | Las aristas tienen dirección |
| **A** | *Acyclic* | No contiene ciclos |
| **G** | *Graph* | Es un grafo |

| Situación | Consecuencia |
|---|---|
| **Grafo con ciclo** | No existe orden: `A` exige a `B` y `B` exige a `A` |
| **Grafo no dirigido** | No hay noción de «antes» ni «después» |
| **DAG** | Existe al menos un orden topológico |

> Un ciclo de dependencias (`A -> B -> C -> A`) significa que nada puede comenzar primero: el problema **no tiene solución**.

## Implicaciones

| Implicación | Descripción |
|---|---|
| **Varias soluciones** | Pueden existir muchos órdenes válidos; depende del orden en que se visiten los vecinos |
| **Todos los vértices** | Se deben recorrer **todos** los nodos, incluso los que no son alcanzables desde el primero |
| **Inicio** | Se empieza por nodos sin dependencias, pero el recorrido se repite desde cada nodo no visitado |
| **Detección de ciclos** | Si durante el recorrido se encuentra un nodo que está en proceso, hay un ciclo y no hay orden |
| **No es único** | Dos resultados distintos pueden ser ambos correctos |
| **Determinismo** | Para obtener siempre el mismo resultado se necesita una regla de desempate (por ejemplo, orden alfabético) |

## Ejemplo de trabajo

| Nodo | Depende de (entra) | Sus salidas |
|:--:|---|---|
| **A** | — | `C` |
| **B** | — | `C` |
| **C** | `A`, `B` | `D` |
| **D** | `C` | `E`, `F` |
| **E** | `D` | `H` |
| **F** | `D` | `H` |
| **H** | `E`, `F` | `∅` |

```
A ──┐
    ├──> C ──> D ──┬──> E ──┐
B ──┘              │        ├──> H
                   └──> F ──┘
```

* `A -> C`, `B -> C`, `C -> D`, `D -> E`, `D -> F`, `E -> H`, `F -> H`, `H -> ∅`.
* Son **7 vértices**, por lo que el resultado ocupa un vector de tamaño 7.

## Cómo funciona: DFS con visita al salir (*post-orden*)

El ordenamiento topológico se obtiene con un recorrido **DFS**, con un cambio clave: el nodo se registra **cuando termina de procesarse** (en el *pop*), no cuando se descubre.

| Elemento | Descripción |
|---|---|
| **Estructura de resultado** | Lista enlazada o vector de tamaño `V` (aquí, 7) |
| **Posición de inserción** | Se llena **de atrás hacia adelante**: última posición disponible |
| **Momento de registro** | Cuando el nodo no tiene más vecinos sin visitar (*dead end*) |
| **Marcas de visita** | Los nodos visitados no se vuelven a procesar |

### Procedimiento

| Paso | Qué se hace |
|---|---|
| **1** | Comenzar desde un nodo sin dependencias |
| **2** | Avanzar normalmente con DFS por los vecinos no visitados |
| **3** | Al encontrar un *dead end* (nodo sin vecinos nuevos), colocarlo en la **última posición libre** del vector |
| **4** | Regresar al nodo anterior y comprobar si tiene nuevas adyacencias |
| **5** | Repetir el paso 3 con cada *dead end* encontrado |
| **6** | Cuando el DFS termina, iniciar otro desde cualquier nodo no visitado hasta cubrir **todos** los vértices |

> Por qué funciona: un nodo se coloca solo cuando **todos sus descendientes ya fueron colocados**, es decir, ya están a su derecha en el vector.

### Traza paso a paso (inicio en `A`, vecinos en orden alfabético)

| Paso | Acción | Vector (posiciones 1 a 7) |
|:--:|---|---|
| 1 | Visita `A -> C -> D -> E -> H` | `_ _ _ _ _ _ _` |
| 2 | `H` es *dead end*: va en la posición 7 | `_ _ _ _ _ _ H` |
| 3 | Regresa a `E`, sin vecinos nuevos: posición 6 | `_ _ _ _ _ E H` |
| 4 | Regresa a `D`, visita `F`; `H` ya visitado; `F` en posición 5 | `_ _ _ _ F E H` |
| 5 | `D` sin vecinos nuevos: posición 4 | `_ _ _ D F E H` |
| 6 | Regresa a `C`: posición 3 | `_ _ C D F E H` |
| 7 | Regresa a `A`: posición 2 | `_ A C D F E H` |
| 8 | `A` termina; se inicia un nuevo DFS desde `B`; `C` ya visitado; `B` en posición 1 | `B A C D F E H` |

## Resultados posibles

Uno de los posibles resultados finales; todos respetan las dependencias:

|Resultado 1|B|A|C|D|F|E|H|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
|Resultado 2|A|B|C|D|F|E|H|
|Resultado 3|B|A|C|D|E|F|H|

| Resultado | Cómo se obtiene |
|:--:|---|
| **1** | Se inicia por `A` y se visita `E` antes que `F` |
| **2** | Se inicia por `B` y luego `A`, con `E` antes que `F` |
| **3** | Se inicia por `A` y se visita `F` antes que `E` |

* Cambiar el nodo de inicio o el orden de los vecinos produce otro orden válido.
* `A` y `B` pueden intercambiarse porque no dependen entre sí; lo mismo ocurre con `E` y `F`.

## Segmento de código

```python
def orden_topologico(grafo):
    # grafo: {nodo: [vecinos]}
    n = len(grafo)
    resultado = [None] * n          # vector de tamaño V
    pos = n - 1                     # última posición disponible
    estado = {v: 0 for v in grafo}  # 0 = sin visitar, 1 = en proceso, 2 = terminado

    def dfs(u):
        nonlocal pos
        estado[u] = 1               # en proceso (está en la pila de llamadas)
        for v in grafo[u]:
            if estado[v] == 1:
                raise ValueError("El grafo tiene un ciclo: no hay orden topológico")
            if estado[v] == 0:
                dfs(v)
        estado[u] = 2               # terminado: dead end o sin vecinos nuevos
        resultado[pos] = u          # visita en el pop: se coloca al final
        pos -= 1

    for v in grafo:                 # cubre todos los vértices
        if estado[v] == 0:
            dfs(v)
    return resultado


grafo = {
    "A": ["C"], "B": ["C"],
    "C": ["D"],
    "D": ["E", "F"],
    "E": ["H"], "F": ["H"],
    "H": [],
}
print(orden_topologico(grafo))      # ['B', 'A', 'C', 'D', 'F', 'E', 'H']
```

| Estado | Significado | Uso |
|:--:|---|---|
| **0** | Sin visitar | Se debe explorar |
| **1** | En proceso | Si se encuentra de nuevo, hay un **ciclo** |
| **2** | Terminado | Ya está colocado en el resultado; se ignora |

## Complejidad

| Aspecto | Valor |
|---|---|
| **Tiempo** | `O(V + E)`: cada vértice y cada arista se procesan una vez |
| **Espacio** | `O(V)`: vector de resultado, estados y pila de recursión |
| **Estructura del grafo** | Lista de adyacencia (con matriz sería `O(V²)`) |

## Alternativa: algoritmo de Kahn

| Aspecto | Descripción |
|---|---|
| **Estrategia** | Retirar repetidamente los nodos sin dependencias |
| **Idea** | Calcular el grado de entrada de cada nodo; procesar los de grado `0` y restar el grado de sus vecinos |
| **Estructura clave** | Cola de nodos con grado de entrada `0` |
| **Detección de ciclo** | Si quedan nodos sin procesar, hay un ciclo |
| **Complejidad** | `O(V + E)` |

| Aspecto | DFS (post-orden) | Kahn |
|---|---|---|
| **Enfoque** | Recursivo, recorre en profundidad | Iterativo, por grados de entrada |
| **Orden de construcción** | De atrás hacia adelante | De adelante hacia atrás |
| **Detecta ciclos** | Nodo «en proceso» encontrado de nuevo | Quedan nodos sin procesar |

## Resumen de ordenamiento topológico

| Idea | Resumen |
|---|---|
| **Qué es** | Orden lineal de los nodos que respeta todas las dependencias |
| **Para qué sirve** | Cursos, paquetes, compilación, planificación de tareas |
| **Requisito** | Grafo dirigido y acíclico (DAG) |
| **Cómo se hace** | DFS que coloca cada nodo al terminar, llenando el vector desde el final |
| **Soluciones** | Varias válidas; no es único |
| **Ciclo** | No existe orden; se detecta con el estado «en proceso» |
| **Complejidad** | `O(V + E)` |