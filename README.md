# final-eko-dk8s
Examen Final - Docker &amp; Kubernetes Security
---

# Examen Final – Docker & Kubernetes Security

Este proyecto despliega tres aplicaciones utilizando **Kubernetes**, con imágenes publicadas en **Docker Hub**. La arquitectura está compuesta por:

* **Frontend**
* **API (FastAPI)**
* **Base de Datos PostgreSQL**

El despliegue se realiza mediante **Deployments**, **Services**, **ConfigMaps** y **Secrets**, siguiendo buenas prácticas básicas de Kubernetes.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado:

* **Docker** (solo para desarrollo local o testing)
* **Kubernetes** (Minikube, Docker Desktop o clúster equivalente)
* **kubectl** correctamente configurado
* Acceso a Internet para descargar las imágenes desde **Docker Hub**

Verifica el clúster:

```bash
kubectl cluster-info
```

---

## Arquitectura del Proyecto

* Las **imágenes ya están publicadas en Docker Hub**, por lo que **no es necesario construirlas localmente**.
* La configuración sensible (credenciales de DB) se maneja con **Secrets**.
* La configuración no sensible se maneja con **ConfigMaps**.
* La comunicación entre servicios se realiza mediante **Services ClusterIP**.
* El acceso local se realiza mediante **kubectl port-forward**.

---

## Estructura del Proyecto

```plaintext
final-eko-k8s/
├─ README.md
├─ docker-compose.yml
├─ manifests/
│  ├─ frontend-deployment.yaml
│  ├─ frontend-service.yaml
│  ├─ api-deployment.yaml
│  ├─ api-service.yaml
│  ├─ database-deployment.yaml
│  ├─ database-service.yaml
│  ├─ configmap.yaml
│  └─ secret.yaml
├─ APILayer/
│  ├─ Dockerfile
│  ├─ app.py
│  └─ requirements.txt
├─ Frontend/
│  ├─ Dockerfile
│  ├─ app.py
│  ├─ requirements.txt
│  └─ templates/
│     └─ index.html
└─ Database/
   ├─ Dockerfile
   └─ init.sql


```

---

## Despliegue en Kubernetes

### 1. Clonar el repositorio

```bash
git clone https://github.com/SBELUCCI/final-eko-dk8s.git
cd final-eko-k8s
```

---

### 2. Crear Secrets y ConfigMaps

Estos recursos deben crearse **antes** de los deployments, ya que son consumidos por los pods.

```bash
kubectl apply -f manifests/secret.yaml
kubectl apply -f manifests/configmap.yaml
```

Verificación:

```bash
kubectl get secrets
kubectl get configmaps
```

---

### 3. Crear Deployments y Services

Aplica los manifiestos en el siguiente orden lógico:

#### Base de Datos PostgreSQL

```bash
kubectl apply -f manifests/database-deployment.yaml
kubectl apply -f manifests/database-service.yaml
```

#### API (FastAPI)

```bash
kubectl apply -f manifests/api-deployment.yaml
kubectl apply -f manifests/api-service.yaml
```

#### Frontend

```bash
kubectl apply -f manifests/frontend-deployment.yaml
kubectl apply -f manifests/frontend-service.yaml
```

---

### 4. Verificar el estado del despliegue

```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

Asegúrate de que todos los pods estén en estado **Running**.

---

## Acceso a las Aplicaciones (Port Forward)

Dado que los servicios son **ClusterIP**, el acceso se realiza mediante `kubectl port-forward`.

### Frontend

```bash
kubectl port-forward svc/frontend-service 3000:5000
```

Acceso desde el navegador:

```
http://localhost:3000
```

---

### API

```bash
kubectl port-forward svc/api-service 8081:5000
```

Acceso a la API:

```
http://localhost:8081
```

Ejemplo de endpoint:

```
http://localhost:8081/items
```

---

### Base de Datos PostgreSQL

```bash
kubectl port-forward svc/database-service 5432:5432
```

Puedes conectarte usando un cliente como `psql` o `pgAdmin`:

* **Host**: localhost
* **Puerto**: 5432
* **Credenciales**: definidas en `secret.yaml`

---

## Eliminación de Recursos

Para eliminar todo el despliegue:

```bash
kubectl delete -f manifests/
```

O de forma ordenada:

```bash
kubectl delete deployment frontend api database
kubectl delete service frontend-service api-service database-service
kubectl delete configmap app-config
kubectl delete secret app-secret
```

---

## Consideraciones de Seguridad

* Uso de **Secrets** para credenciales sensibles.
* Separación de configuración mediante **ConfigMaps**.
* Servicios expuestos solo internamente (**ClusterIP**).
* Acceso externo controlado mediante **port-forward**.
* Imágenes versionadas y almacenadas en **Docker Hub**.

---

## En conclusión:

Este proyecto demuestra un despliegue completo de una aplicación de tres capas en Kubernetes, aplicando conceptos clave de **contenedorización**, **orquestación** y **seguridad básica**. El uso de imágenes preconstruidas en Docker Hub simplifica el despliegue y permite enfocarse en la correcta configuración del clúster.


