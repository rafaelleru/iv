# Despliegue de streamai en un PaaS

Como plataforma PaaS se ha usado heroku ya que es muy facil desplegar un servicio API independientemente del lenguaje en el que este implementado en este servicio.

Para replicar este despliegue el proceso es sencillo, primero instalamos el cli que provee heroku, yo lo he hecho usando snap ya que no proveen de un rpm para fedora:

```
sudo snap install --classic heroku
```

Una vez instalado heroku y siempre que tengamos cuenta en el servicio, procedemos a hacer login para ello ejecutamos

```
heroku login
```

A continuacion si no tenemos el codigo clonado en local lo clonamos desde github:

```
git clone https://github.com/rafaelleru/iv.git
```

Una vez hecho esto creamos una app en heroku desde el cli usando

```
heroku create <nombre-de-la-aplicacion>
```

Por ultimo publicamos la App en heroku, el cual detectara automaticamente que esta esta escrita en python:

```
git push heroku master
```

## Consideraciones adicionales sobre el despliegue en heroku

Los pasos anteriores estan enfocados a reproducir el despliegue de mi aplicacion en heroku a partir del codigo en el repositorio de github, aunque para que esta funciona en primer lugar he tenido que hacer algunas modificaciones en el mismo,las cuales procedo a detallar.

- Crear un archivo `Procfile` que contiene lo siguiente:
```
web: make run-heroku
```

web indica a heroku que nuestro servicio es un servicio https, make es el comando que usamos para servir el API y run heroku es una nueva entrada en el makefile que contiene lo siguiente:

```
python3 src/api.py
```
