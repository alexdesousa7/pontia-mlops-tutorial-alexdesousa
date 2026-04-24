# Modulo 04 - DevOps Ejercicio: Pontia MLOps Tutorial 

Este proyecto implementa un flujo completo de **Integración Continua**, **Entrenamiento de Modelo (Build)** y **Despliegue (Deploy)** utilizando:

- GitHub Actions (CI/CD)
- Render (Hosting de la API)
- FastAPI (servicio web)
- RandomForest (modelo ML)
- Infrastructure as Code (IaC) mediante `render.yml`

El objetivo es demostrar un pipeline MLOps funcional, automatizado y reproducible.

---

# 👥 Integrantes del Grupo

- **Manuel Pérez** (@Manuel.Pérez.IA0226)  
- **Jose Alexander** (@Jose.Alexander.IA0226)  
- **Joaquín Castro** (@joaquin.castro.IA0226)  
- **Marvin Farith** (@Marvin.Farith.IA0226)  

---

# 📁 Estructura del Proyecto

```
pontia-mlops-tutorial-alexdesousa/
│
├── .github/
│   └── workflows/
│       ├── integration.yml        # Pipeline de integración continua
│       ├── build.yml              # Entrenamiento y registro del modelo
│       └── deploy.yml             # Despliegue en Render
│
├── data/
│   └── raw/
│       ├── .gitkeep
│       ├── adult.data             # Dataset original
│       ├── adult.names            # Descripción del dataset
│       ├── adult.test             # Dataset de test
│       ├── Index
│       └── old.adult.names
│
├── deployment/
│   ├── app/
│   │   ├── main.py                # API FastAPI
│   │   └── model_handler.py       # Carga del modelo en producción
│   └── requirements.txt           # Dependencias del servicio en Render
│
├── model_tests/
│   ├── __init__.py
│   └── test_model.py              # Tests de performance e integración del modelo
│
├── models/
│   ├── .gitkeep
│   ├── encoders.pkl               # Codificadores entrenados
│   ├── model.pkl                  # Modelo RandomForest entrenado
│   └── scaler.pkl                 # Escalador entrenado
│
├── scripts/
│   └── register_model.py          # Registro del modelo como artefacto
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # Carga y preprocesamiento de datos
│   ├── evaluate.py                # Evaluación del modelo
│   ├── main.py                    # Entrenamiento principal
│   └── model.py                   # Definición del modelo ML
│
├── unit_tests/
│   ├── __init__.py
│   ├── test_data_loader.py        # Tests unitarios del data loader
│   ├── test_evaluate.py           # Tests unitarios de evaluación
│   └── test_model.py              # Tests unitarios del modelo
│
├── .gitignore
├── pytest.ini
├── README.md
├── render.yml                     # Infrastructure as Code (Render Blueprint)
└── requirements.txt               # Dependencias del proyecto

```

---

# 🚦 Pipelines del Proyecto

## 1️⃣ Integration — CI
Se ejecuta en cada Pull Request hacia `main`.

Incluye:
- Instalación de dependencias
- Ejecución de tests
- Pipeline completa aunque los tests fallen (pero marca error)
- Bloqueo de merge si no pasa el status check

**Objetivo:** validar calidad antes de integrar.

---

## 2️⃣ Build — Entrenamiento y Registro del Modelo
Se ejecuta en cada push a `main`.

Incluye:
- Descarga del dataset
- Entrenamiento del modelo RandomForest
- Guardado del modelo
- Ejecución de tests de integración y performance
- Registro del modelo como artefacto
- Creación automática de un Release en GitHub

**Objetivo:** generar un modelo versionado y reproducible.

---

## 3️⃣ Deploy — Despliegue en Render
Se ejecuta manualmente desde GitHub Actions.

Incluye:
- Envío de webhook a Render
- Render reconstruye la imagen
- Render despliega la API FastAPI
- El servicio queda accesible públicamente

**Objetivo:** publicar la API del modelo.

---

# 🌐 API en Render

La API está desplegada en Render como un servicio web Python.

Endpoints principales:

- `GET /` → mensaje de bienvenida  
- `POST /predict` → recibe datos y devuelve predicción del modelo

---

# 🛠️ Infrastructure as Code (IaC) — `render.yml`

Este archivo permite recrear el servicio en Render sin usar la interfaz gráfica.

```yaml
services:
  - type: web
    name: pontia-mlops-tutorial-alexdesousa
    env: python
    region: frankfurt
    plan: free
    rootDir: deployment
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port 8080
    envVars:
      - key: GITHUB_REPO
        value: "alexdesousa7/pontia-mlops-tutorial-alexdesousa"
```

**Qué define:**
- Servicio web Python  
- Región Frankfurt  
- Plan Free  
- Comandos de build y start  
- Variable de entorno necesaria para el deploy  
- Directorio raíz del servicio  

---

# 🔄 Simulación de Rollback

Para realizar un rollback del modelo o del servicio:

### Opción A — Rollback de Release (modelo)
1. Ir a GitHub → Releases  
2. Seleccionar un release anterior (ej: `model-12`)  
3. Descargar el modelo  
4. Reemplazar el modelo actual  
5. Ejecutar nuevamente el workflow de Deploy  

### Opción B — Rollback de código
1. Ir a GitHub → Commits  
2. Seleccionar un commit estable  
3. Crear una rama desde ese commit  
4. Hacer un PR hacia `main`  
5. Mergear  
6. Ejecutar Deploy  

### Opción C — Rollback desde Render
1. Render → Deploys  
2. Seleccionar un deploy anterior  
3. Pulsar “Rollback to this version”  

---

# 👥 Pull Requests y Code Reviews

El repositorio incluye:
- PR para Integration  
- PR para Build  
- PR para Deploy  
- Cada PR con su respectivo Code Review (“Looks good to me”)  

Cumpliendo así el requisito mínimo de 3 PRs revisados.

---

# ✔️ Estado Final del Proyecto

| Componente | Estado |
|-----------|--------|
| Integration | ✔️ OK |
| Build | ✔️ OK |
| Deploy | ✔️ OK |
| API funcionando | ✔️ OK |
| IaC con render.yml | ✔️ OK |
| PRs y CRs | ✔️ OK |

---

# 📬 Repositorio

**Modulo 04 DevOps — Pontia MLOps Tutorial**  
Repositorio: [https://github.com/alexdesousa7/pontia-mlops-tutorial-alexdesousa](https://github.com/alexdesousa7/pontia-mlops-tutorial-alexdesousa)
```
