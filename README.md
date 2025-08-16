# API de Notas

Esta API RESTful permite gestionar notas de texto mediante operaciones CRUD (crear, leer, actualizar y eliminar) a través de endpoints HTTP. Está construida con Flask y sirve como ejemplo de un servicio backend sencillo para tu portafolio.

## Características

- Listar todas las notas.
- Obtener una nota por ID.
- Crear una nueva nota enviando título y contenido.
- Actualizar una nota existente.
- Eliminar una nota.
- Almacena los datos en memoria (no requiere base de datos).

## Requisitos

- Python 3.8+
- Flask 2.2 o superior

## Instalación

Clona el repositorio y crea un entorno virtual para instalar las dependencias:

```bash
git clone https://github.com/Dvstrada/api-notas.git
cd api-notas
python -m venv venv
source venv/bin/activate  # en Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
```

## Uso

Ejecuta la aplicación con:

```bash
python app.py
```

Con el servidor en ejecución, puedes probar los endpoints usando `curl` o Postman:

```bash
# Crear una nota
curl -X POST -H "Content-Type: application/json" -d '{"title":"Mi nota","content":"Contenido de prueba"}' http://localhost:5000/notes

# Obtener todas las notas
curl http://localhost:5000/notes

# Obtener una nota por ID (por ejemplo 1)
curl http://localhost:5000/notes/1

# Actualizar una nota
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Nuevo título","content":"Nuevo contenido"}' http://localhost:5000/notes/1

# Eliminar una nota
curl -X DELETE http://localhost:5000/notes/1
```

## Estructura del proyecto

- `app.py` – Aplicación Flask con las rutas y lógica de la API.
- `requirements.txt` – Lista de dependencias necesarias para el proyecto.
- `README.md` – Documentación y guía de uso de esta API.

## Licencia

Este proyecto está bajo la licencia MIT.
