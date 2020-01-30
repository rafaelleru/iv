[![Build Status](https://travis-ci.org/rafaelleru/iv.svg?branch=master)](https://travis-ci.org/rafaelleru/iv)
[![CircleCI](https://circleci.com/gh/rafaelleru/iv.svg?style=svg)](https://circleci.com/gh/rafaelleru/iv)

# AI remote strem

# Problema

El creciente número de aplicaciones de inteligencia artificial en el mercado nos lleva a pensar en el coste de las infraestructuras que plantean estos servicios en entornos de producción. Ademas nos encontramos con que resulta complicado extrapolar los distintos modelos obtenidos a entornos reales de producción.

# Resolución del problema.

AI remote stream pretende mitigar algunas de las limitaciones planteadas anteriormente poniendo al alcance de los usuarios una infraestructura en la que poder usar dichos modelos inteligentes en entornos de producción. El sistema permitirá al usuario ejecutar tareas de clasificación de datos en la nube sin tener que disponer de una infrastructura propia.

El sistema permitira generar tareas mediante un servicio y obtener los resultados una vez estos esten listos todo mediante un servicio REST.

# Solución planteada

El sistema encolara las tareas que serán procesadas en modelos de aprendizaje automático previamente entrenados. Una vez la tarea de clasificación este completada se almacenaran los resultados en una base de datos.

El usuario podrá obtener mediante un identificador de tarea en todo momento el estado en el que se encuentra la tarea, y si esta esta completa podra obtener los resultados obtenidos por los modelos online.

## Tecnologías usadas

- [Python 3.7](https://www.python.org) como lenguaje principal en el que construir nuestro sistema.
- [Pyramid](https://trypyramid.com/) como framework para construir nuestro API REST.
- [Apache Kafka](https://kafka.apache.org/) como broker para encolar nuestras tareas.
- [Celery](http://www.celeryproject.org/) como gestor de tareas del sistema.
- [Elasticsearch](https://www.elastic.co) como sistema de base de datos.
- [Pytest](https://pytest.org) como framework para desarrollar los test unitarios.
- [Docker](https://www.docker.com) para la virtualización de nuestro servicio.
- [EKS](https://aws.amazon.com/eks/) para el despliegue, ya que para el despliegue final usaremos [kubernetes](https://kubernetes.io) para orquestar los contenedores.
- [Emacs](https://www.gnu.org/software/emacs/) (con [evil](https://github.com/emacs-evil/evil) mode) y [neovim](https://neovim.io) para el desarrollo ;)

## Integracion continua

Para la integración continua vamos a usar travis, no es necesario usar herramientas tipo make por el momento ya que solo queremos ejecutar los tests de nuestro proyecto.

Para configurar travis solo ha sido necesario dar de alta el proyecto en la web y añadir el repositorio, tras esto hemos añadido el archivo `.travis.yml` para ejecutar todo el proceso de integración continua en cada commit

## Documentacion
 - [tests](./doc/tests.md)
 - [paas](./doc/paas.md)


buildtool: makefile

Despliegue: https://streamai.herokuapp.com

Contenedor: https://streamai-docker.herokuapp.com

docker-hub: https://hub.docker.com/r/rafaelleru/stream-ai

provision: terraform/main.tf