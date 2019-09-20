# Prácticas IV

## AI remote strem

AI remote stream es una aplicación que pone al alcance del usuario modelos de amchine learning que pueden ser usados on demand.

El sistema provee una serie de modelos de machine learning preentrenados, el usuario pr medio de una API REST puede subir distintos datos al sistema, 
el formato de estos datos dependera del modelo a usar (cada modelo usa un endpoint distinto).

### Servicios y técnologias usados.

- kafka para encolar los  distintos trabajos.
- docker para la virtualización.
- kubernetes para el despliegue en el entorno remoto.
- ElasticSearch como tecnología de base de datos.
