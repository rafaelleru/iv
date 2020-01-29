# Despliegue y ejecucion de un docker listo para ejecutar

Con el objetivo de facilitar el despliegue se ha construido un nuevo contenedor, el cual contiene la misma base que el contenedor usado
anteriormente en desarrollo pero que en lugar de no ejecutar ningun comando, arranca el servicio we automaticamente. El dockerfile esta accesible en `docker/streamai/Dockerfile`

Se ha creado una nueva app en heroku que usa el stack de container para poder tener desplegadas a la vez la version del hito 4 y esta en la que usamos el contenedor, para ello ejecutamos:

```
heroku create streamai-docker
```

A continuacion seteamos el stack con el comando

```
heroku stack:set container --app streamai-docker
```

una vez hecho esto creamos un nuevo archivo `heroku.yml` el cual contiene la informacion necesaria para que heroku sepa como construir el contenedor. En mi caso al no estar el Dockerfile en la raiz del repositorio el contenido es el siguiente

```
build:
    docker:
        web: docker/streamai/Dockerfile
```

una vez hecho esto pusheamos al remote llamado heroku y el despliegue comienza, si todo ha ido bien el servicio estara disponible en ambas urls:
 - `https://streamai.herokuapp.com`
 - `https://streamai-docker.herokuapp.com`
