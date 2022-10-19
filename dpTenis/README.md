# dptenisproy
Proyecto de prueba con limpieza de datos.
Para el desarrollo de esta aplicación se utilizaron los frameworks [Django](https://docs.djangoproject.com/en/4.1/) y [boostrap](https://getbootstrap.com/), y para backend se utilizó [Python](https://www.python.org/).

Como motor de base de datos se utiliza [SQlite3](https://www.sqlite.org/index.html), es una base de datos ligera que se instala por default con Django.

## Instalación

Para iniciar el servicio de manera local, se debe ejecutar el siguiente comando desde la carpeta principal:

```bash
python manage.py runserver
```
Esto iniciará el servicio de Django.

Para visualizar la aplicación, se escribe la siguiente dirección en cualquier navegador de internet:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Nota
En caso de que ocurra algún error, se deben ejecutar las siguientes instrucciones para habilitar los servicios:

1. Ejecutar el comando migrate para aplicar las configuraciones de la aplicación:
```bash
python manage.py migrate
```
En caso de que salga algún error al momento de la migración, instalar [pytz](https://pypi.org/project/pytz/), y volver a ejecutar la instrucción migrate del paso anterior:
```bash
pip install pytz
```

2. Ejecutar la instrucción makemigrations para iniciar la migración de los modelos como tablas en la base de datos:
```bash
python manage.py makemigrations
```

3. Ejecutar el el comando createsuperuser para crear un usuario para la administración de la aplicación y proporcionar la información solicitada
```bash
python manage.py createsuperuser
```
Nota: Puede dejar vacio el campo email.

4. En caso de que se le solicite, debe ejecutar el comando migrate del paso 1.

# Listado de archivos y carpetas

```bash
.
  *[dptenis](.) #Carpeta principal
    *[apps](./apps/) #carpeta que contiene las aplicaciones del proyecto
      *[dptenisapp](./apps/dptenisapp/) #aplicación django y python
        *[__pycache__]#carpeta creada por django
        *[migrations]#carpeta creada por django
        *[static](./apps/dptenisapp/static/) #carpeta que contiene los archivos consumibles por la aplicación
          *[css](./apps/dptenisapp/static/css/) #carpeta que contiene archivos de estilo
            *[dpteniscrud.css](./apps/dptenisapp/static/css/dpteniscrud.css) #archivo de estilos
          *[js](./apps/dptenisapp/static/js/) #carpeta que contiene archivos de javascript
            *[dpteniscrud.js](./apps/dptenisapp/static/js/dpteniscrud.js) #archivo de estilos
        *[templates](./apps/dptenisapp/templates/) #carpeta que contiene las plantillas html
          *[dpteniscrud.html](./apps/dptenisapp/templates/dpteniscrud.html) #plantilla que contiene el formulario para la captura de registros y las tablas que muestran la información de la base de datos
          *[editardist.html](./apps/dptenisapp/templates/editardist.html) #plantilla para modificar un registro de las tablas en la base de datos
          *[templatebase.html](./apps/dptenisapp/templates/templatebase.html) #plantilla base
        *[__init__.py] #archivo creado por django
        *[admin.py](./apps/dptenisapp/admin.py) #archivo creado por django que se utiliza para registrar los modelos de django utilizados por las tablas en la base de datos.
        *[apps.py](./apps/dptenisapp/apps.py) #archivo creado por django para la configuración de la app (se comenta el contenido ya que marca error al momento de iniciar el servicio)
        *[models.py](./apps/dptenisapp/models.py) #archivo que contiene los modelos utilizados por las tablas de la base de datos
        *[test.py] #archivo creado por django
        *[urls.py](./apps/dptenisapp/urls.py) #archivo donde se configuran las rutas de acceso para las diferentes vistas utilizadas por la aplicación.
        *[views.py](./apps/dptenisapp/views.py) #archivo que contiene las diferentes vistas y el CRUD principal de la aplicación, así como todos los scripts para realizar la limpieza de los datos.
    *[dptenis](./dpTenis/) #carpeta creada por django que contiene los archivos de configuración de la aplicación.
      *[__pycache__] #carpeta creada por django
      *[__init__.py] #archivo creado por django
      *[asgi.py] #archivo creado por django
      *[settings.py](./dpTenis/settings.py) #archivo creado por django, contiene la configuración base de la aplicación.
      *[urls.py](./dpTenis/urls.py) #archivo creado por django para configurar el acceso a los templates la aplicación.
      *[wsgi.py] #archivo creado por django
    *[dptenisdb] #base de datos SQlite3
    *[LICENSE.md](LICENSE.md) #archivo de licencia
    *[manage.py](manage.py) #archivo utilizado por Django para administrar la aplicación.
    *[README.md](README.md) #este archivo.
    *[dpTenis_Proyect.pdf](dpTenis_Proyect.pdf) #Documentación del proyecto
```