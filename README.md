# API

### Requirements

- docker
- docker-compose

### Start the project

`docker-compose up`

### Create migrations

`docker-compose run web python manage.py makemigrations`

### Run migrations

`docker-compose run web python manage.py migrate`

## Mi tarea:
No alcancé a realizar la comunnicación del otro proyecto con este :(

Web: Ir a Api Root > service_area > Extra actions

Necesitamos que desarrolles un script o una API separada del proyecto safari, en el lenguaje o framework que prefieras, que cumpla con las siguientes funciones:

Postman: /service_area/get_route_beta/ with parameters GET a and b 
- Obtener la ruta de un punto A a un punto B cualquiera, listando las áreas de servicio por las cual se debería pasar.

Postman: /service_area/get_route_with_fuel_beta/ with parameters GET a and b and number_plate
- Calcular en qué puntos y cuánto combustible debe uno cargar para que una ruta completa (desde un punto A a un punto B cualquiera) sea lo más barata posible. Considerar lo siguiente
    - La función recibe: punto de inicio (int que corresponde al km), punto de término (int que corresponde al km) y patente del vehículo.
    - Debe retornar una lista con los puntos donde parar y cuántos litros cargar.
    - Un viaje puede comenzar y terminar en cualquier punto de descanso, sin devolverse por el mismo camino.
    - Todos los vehículos comienzan con el estanque lleno, no es necesario devolverlos llenos.
    - No todos los vehículos tienen el mismo rendimiento ni tamaño de estanque.
    - No todos los vehículos van a tener rendimiento y estanque suficiente como para realizar un recorrido completo sin cargar combustible.
    - No es necesario realizar carga completa del estanque cuando uno pasa por un punto de descanso, se puede cargar lo suficiente como para sólo llegar hasta el siguiente.
    - Todas las áreas de servicio tienen precios de combustible distintos.

# Para conocerte mejor

1. Cuáles crees que son los aspectos más importantes al momento de hacer Code Review
	Mente abierta para comprender el porqué de algunas decisiones anteriores en el código, Consciencia para aportar mejoras y para tomar lo mejor de la experiencia de otros, Alineamiento total del equipo para que todos estemos al menos claros de a dónde queremos llegar, esto icluye: estructura a seguir, nomenclatura y forma de trabajo del equipo y no individual 
2. Has trabajado con control de versiones? Cuál ha sido el flujo que has utilizado? Por favor explicar.
	GIT. Desde hace años uso git, me gusta usarlo con la terminal directamente. Actualmente lo uso con GCP, generalmente uso 3 ramas: development, staging and master; development para desarrollo, luego merge con staging para ser revisado por usuarios internos y/o QAs y finalmente merge con master cuando el módulo y/o la funcionalidad está lista
3. Cuál ha sido tu experiencia utilizando herramientas fuera de desarrollo del código mismo? (AWS, GCP, VPS, Docker, etc.)
	Actualmente mis desarrollos están alojados en GCP. Uso App Engine Standard generalmente para la app, IAM para algunos permisos y uso de librerías de GCP, Cloud Functions para algunas funcionalidades, Cloud Storage para los estaticos, SQL para la BD, Cloud Build para el deploy y Source Repositories para el control de versiones. Generalmente en mi día a día es lo que uso.
4. Tienes algún servicio en la nube favorito? Cuál y por qué?
	Me gusta la nube en general pero diría App Engine porque es increíble que proporcione uan estructura lista gestionada por Google :)
5. Has tenido experiencia con microservicios? En caso de que la tengas, podrías explicar por qué en ese caso fue mejor un microservicio que otro tipo de arquitectura?
	Sí. El último caso que recuerdo fue mejor debido a que el software a desarrollar se comunica cosntantemente con APIs de Google para saber tareas específicas: cuantos dominios tengo?, cuál es mi factura este mes?, cuándo vence mi contrato?, cuántas licencias tengo?; por ello se tomó la decisión de crear microservicios independientes que puedan usar diferentes software a futuro.
