# Django en producción a través de gunicorn y nginx

## Antecedentes
* La presente guía está basada en el tutorial del servicio **DigitalOcean** [[enlace - web]](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04) 

## Softaware utilizado

    * Sistema operativo GNU/Linux **KaliLinux** 
    * Lenguaje de programación Python (3.9)
    * Librerías de pyhton: django, corsheaders, rest_framework, gunicorn. 
    * Servidor Web - nginx
	
## Proceso 

### Parte 1

Una ves que se tiene un proyecto de django funcional, se procede a:

1. Instalar la librería gunicorn (pip install gunicorn)
2. Agregar la variable **ALLOWED_HOSTS**  con algunas direcciones en el archivo **settings.py** del proyecto de django que permitan acceder desde gunicorn y luego desde el servidor web.
```
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"] 	 
```
3. En el archivo **urls.py** del proyecto de django agregar lo siguiente (para el manejo de los archivo de la carpeta de static:
```
# importar
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# agregar el siguiente valor a la variable urlpatterns
urlpatterns += staticfiles_urlpatterns()
```
4. Recopilar el contenido estático en al carpeta static (principalmente los archivos de admin)

```
python manage.py collectstatic
```

5. Levantar o iniciar el proyecto con **gunicorn**, desde la carpeta raíz del mismo. A través del siguiente comando:

```
gunicorn --bind 0.0.0.0:8000 proyectoUno.wsgi
```
Donde, **proyectoUno** es el nombre del proyecto. En el navegador, se debe observar el proyecto funcionando. ***Consejo***, si no es posible visualizar el proyecto, debe revisar los errores; cuando se superen los mismos, pasar a la siguiente parte.

5. Terminar la ejecución del servicio de gunicorn a través de **control+c**

### Parte 2

Ahora procedemos a iniciar el proceso de enlazar el servidor nginx mediante gunicorn con el proyecto de django.

1) Agregar un servicio en el sistema operativo; mismo que será encargado de levantar el proyecto de django mediante gunicorn. Luego el servicio será usado por nginx.

2) En el directorio **/etc/systemd/system/** agregar un archivo con la siguiente extensión y estructura. Se debe usar **sudo** para acceder y crear el archivo.

2.1. Nombre del archivo **proyecto01.service** . Donde proyecto01 es un nombre cualquiera.
2.2. En el archivo agregar la siguiente información
```

[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=kali
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/kali/Desktop/trafinal-2bim-grupo-juventud-cristiana/proyecto-django/app/

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=/usr/bin/python3.9"

# Detallar el comando para iniciar el servicio
ExecStart=/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 proyectoUno.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target
```
3) Iniciar y habilitar el proceso a través de los siguiente comandos:
```
sudo systemctl start proyecto01
sudo systemctl enable proyecto01
```
Donde **proyecto01**, es el nombre que se le asignó al archivo creado con extensión **service**

Verificar que todo esté en orden con el servicio, usar el comando:
```
sudo systemctl status proyecto01
```

4) Este paso es importante, se debe verificar que el archivo .sock esté creado en el directorio del proyecto.


### Parte 3
* Configuración del servidor web **nginx**. 

1) Procedemos ha crear un archivo **sites-available** de nginx; la ruta de acceso es: /etc/nginx/sites-available/. Se debe ingresar con permisos de administrador (sudo).
```
sudo touch /etc/nginx/sites-available/proyecto01

```
2) En el archivo se debe usar la siguiente estructura
```
server {
    listen 81;
    server_name localhost;
    
    location / {
       rewrite /(.*) /$1 break;
        include proxy_params;
        proxy_pass http://unix:/home/kali/Desktop/trafinal-2bim-grupo-juventud-cristiana/proyecto-django/app/application.sock;
    }

    
    location /static/ {
        rewrite /static/(.*) /$1 break;
        root /home/kali/Desktop/trafinal-2bim-grupo-juventud-cristiana/proyecto-django/app/static/;
    }

}
```
3) Iniciar un enlace simbólico del archivo creado en el directorio sites-available.

```
sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled
```

4) En el archivo settings.py del proyecto realizar las siguientes modificaciones:
```
# modificar esta variable solo en producción, donde proyecto1, es el subdirectorio usado en el archivo de nginx
STATIC_URL = '/proyecto1/static/'

```

4) Iniciar o reiniciar el servicio de nginx.

5) Si todo marcha bien, en un navegador con las siguiente direcciones se debe deplegar el proyecto a través de nginx:

* http://localhost:81/proyecto1
* http://0.0.0.0:81/proyecto1
* http://127.0.0.0:81/proyecto1


6) Verificar que el proyecto funcione.

