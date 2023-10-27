# Proyecto Django GPT

Este es un proyecto Django para gestionar inventario de productos.

## Requisitos

Asegúrate de tener Python y Django instalados en tu entorno de desarrollo. Puedes instalar los requisitos ejecutando:

1.  ```bash
   pip install -r requirements.txt

## Configuración del Entorno Virtual

1. Es una buena práctica utilizar un entorno virtual para el desarrollo. Puedes crear uno ejecutando:

python -m venv venv

2. Activar el entorno virtual en Windows:

venv\Scripts\activate

3. Activar el entorno virtual en Linux/macOS:

source venv/bin/activate


## Configuracion del Proyecto

1. Clona el repositorio.

git clone https://github.com/tu-usuario/proyecto-django-gpt.git
cd proyecto-django-gpt

2. Aplica las migraciones:

python manage.py migrate

python manage.py makemigrations

3. Crea un superusuario para acceder al panel de administracion:

python manage.py createsuperuser

4. Inicia el servidor de desarrollo:

python manage.py runserver

## Uso
- Accede al panel de administración: http://127.0.0.1:8000/admin/
- Agrega, edita o elimina productos y categorías.
- Visualiza la lista de productos: http://127.0.0.1:8000/

## Funcionalidades

El **ADM DE EMPRESAS** es un sistema de gestión de inventario desarrollado con Django. Facilita la administración de productos, categorías y existencias en un entorno empresarial o comercial. Con una interfaz intuitiva, proporciona las siguientes funcionalidades clave:

- **Listar Productos:** Visualizar todos los productos disponibles con detalles relevantes.
- **Eliminar Producto:** Eliminar productos existentes del inventario.
- **Editar Producto:** Modificar información sobre productos existentes.
- **Crear Producto:** Agregar nuevos productos al inventario, especificando detalles como nombre, precio, stock y categoría.
