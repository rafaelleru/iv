# Provisionando maquinas virtuales con terraform en google cloud engine

Para automatizar la gestion de las maquinas virtuales en la plataforma de google he elegido terraform, primero por que la mayor parte de los proyectos que he visto han usado vagrant y segundo por que alguna vez he leido acerca de la solucion de terraform.

El primer paso es darnos de alta en la plataforma, una vez hecho esto descargamos el sdk de terraform y lo ponemos en nuestra variable `$PATH`

Creamos el archivo `main.tf`,yo lo he metido en un directorio llamado terraform por organizacion, asi que primero hay ue acceder al directorio. En este archivo se indica el id de nuestro proyecto en gce, el tipo de instancia que queremos, sistema operativo, etc.

mencion especial al archivo referenciado en la linea 3, el cual debemos obtener en la consola de gce para poder acceder al proyecto con la API de gce, ademas en el proyecto debemos habilitar el acceso mediante API a la consola, terraform fallara y nos dara ayuda si no lo hemos hecho.

por ultimo ejecutamos los siguientes commandos:

```
terraform init
terraform plan
terraform apply
```

El primero inicia y crea el directorio `.terraform`, el segundo comprueba que el archivo `main.tf` es correcto y el ultimo provisiona la maquina virtual en la nube de google.


