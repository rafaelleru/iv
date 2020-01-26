# Test automaticos para integracion continua

Los tets automaticos se dividen en dos. Test funcionales que testean la clase encargada de gestionar la logica de la aplicacion y los tests de integracion que se encargan de testear el servicio.

## Travis ci

En travis la ejecucion de los tests es sencilla, primero construimos el contenedor de docker en el cual se ejecutara la aplicacion. Despues lo levantamos usando el comando make run que hemos definido para levantar nuestro entorno. Por ultimo ejecutamos el comando make test el cual ejecuta la suite de tests al completo conectandose con el contenedor que ejecuta la API cuando es necesario.

## circleci

En circleci la ejecuciojnde tests es un poco diferente de la ejecucion en travis. Circleci nos provee de un contenedor principal que es en el que se ejecutara todo nuestro pipeline.

A partir de aqui la ejecucion es simple, usamos un paso nuevo en el makefile el cual es el encargado de arrancar el servidor API en segundo plano y luego llamamos al comando para ejecutar los tests. En circleci no es posible hacerlo usando docker-compose como hacemos en circleci ya que por defecto el contenedor en el que se ejecuta el pipeline no nos permite exponer puertos mediante docker. 

