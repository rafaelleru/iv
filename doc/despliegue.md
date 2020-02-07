# Despliegue de nuestra apicacion en la maquina provisionada.

El despliegue de la version final en gce ha sido sencillo gracias al uso de terraform y ansible.

Una vez que hemos creado la instancia de la maquina virtual en la consola de google, hemos creado una regla para que el firewall permita el trafico hacia nuestra aplicacion, con el siguiente comando:

```
gcloud compute firewall-rules create default-allow-http-8000 \
    --allow tcp:8000 \
    --source-ranges 0.0.0.0/0 \
    --target-tags http-server \
    --description "Allow port 8080 access to http-server"
```

Esto permitira el paso del trafico hacia la API que queremos ejecutar.

Para automatizar el despliegue he creado un nuevo playbook de ansible que podemos encontrar en el directorio `despliegue` el cual contiene los pasos para ejecutar la siguiente secuencia:

- Borra el codigo que hay en la maquina
- Descarga nuevamente el codigo con su version mas reciente
- instala las dependencias de la API, por si estas hubieran cambiado.
- Para todos los procesos de la API que estan corriendo en la instancia.
- Ejecuta la orden start de nuestro makefile para arrancar nuevamente el servicio.
