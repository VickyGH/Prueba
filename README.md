# Prueba - VGH

Coleccion: https://www.getpostman.com/collections/2962efb6e83844f72f0d


## Pasos

1.- Crear un entorno virtual
- python3 -m venv Vent_Prueba
- source myvenv/bin/activate

2.- Descarga los requerimientos
- pip install -r requirements.txt

3.- Crea los modelos
- python manage.py makemigrations
- python manage.py migrate

4.- Inicia el sevicio
- python manage.py runserver 0.0.0.0:8080

5.- Crea un superusuario
- python manage.py createsuperuser

6.- Accede a el enlace

**Para la coleccion necesita un token:
- Inicia sesion con el apartado "login", en la coleccion
- Retornara un token, el cual debera anexar en las peticiones de
POST, DELETE, PUT


