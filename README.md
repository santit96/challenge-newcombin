### Instalacion

Para poder levantar la applicación con Docker, podemos utilizar el comando:
```make up```

Esto creará o ejecutará (si ya están creados), los containers de django y la base de datos.

Tener en cuenta que primero debemos **customizar las variables de entorno** para que la aplicación inicialice correctamente y poder crear la base de datos.

* #### Customización de las variables de entorno

Debemos crear un archivo llamado *.env* en la carpeta base de nuestra aplicación donde estarán definidas nuestras variables de entorno que contienen, entre otras cosas, el nombre de usuario y contraseña de la base de datos, la contraseña del usuario toor de la base de datos y el nombre de nuestro proyecto.

Podemos encontrar ejemplos de valores para nuestras variables en el archivo *.env.example*

* #### Migraciones

El siguiente paso es ejecutar las migraciones, para eso se ejecuta `make bash` para acceder a una terminal dentro del container.
Una vez dentro, ejecutamos `python manage.py migrate`.
Se deberían ejecutar las migraciones sin problema.

* ### Uso

Una vez seguidos estos pasos se habrá levantado la aplicación en el puerto 8000 de nuestra máquina. Para acceder http://localhost:8000

- Con un GET a http://localhost:8000/api/payables se mostrara el listado de boletas de pago no pagas
- Con un GET a http://localhost:8000/api/transactions se mostrara el listado de transacciones acumuladas por día con su monto total y la cantidad
- POST a http://localhost:8000/api/payables con los correspondientes parametros en formato json para crear una boleta de pago
- POST a http://localhost:8000/api/transactions con los correspondientes parametros en formato json para crear una transacción de pago

* #### Resumen de comandos *make* disponibles:


- `make up`: crea/arranca los containers
- `make build`: build (o rebuild) de la imagen docker
- `make create_db`: crea la base de datos en el container mysql
- `make down/stop`: para la ejecución de los containers
- `make prune`: elimina los containers
- `make ps`: muestra los containers del proyecto en ejecución
- `make bash`: permite ingresar a la consola del container de python
- `make bash_db`: permite ingresar a la consola del container de mysql
- `make logs`: muestra los logs de todos los containers del proyecto