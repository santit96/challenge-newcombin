### Instalacion

Para poder levantar la applicación con Docker, podemos utilizar el comando:
```make up```

Esto creará o ejecutará (si ya están creados), los containers de django y la base de datos.

Tener en cuenta que primero debemos **customizar las variables de entorno** para que la aplicación inicialice correctamente y poder crear la base de datos.

* #### Customización de las variables de entorno

Debemos crear un archivo llamado *.env* en la carpeta base de nuestra aplicación donde estarán definidas nuestras variables de entorno que contienen, entre otras cosas, el nombre de usuario y contraseña de la base de datos, la contraseña del usuario toor de la base de datos y el nombre de nuestro proyecto.

Podemos encontrar ejemplos de valores para nuestras variables en el archivo *.env.example*

* #### Creación de la base de datos

Debido a que con Django no se nos permite crear la db, hay que hacerlo de manera manual. Para realizar esto, una vez que se hayan creado nuestros containers, podemos ejecutar el comando:
`make create-db` (debemos asegurarnos que el container de MySQL haya terminado de iniciar, de lo contrario este comando fallará).

O ingresando al container de postgres siguiendo los siguientes pasos:

- Con el comando  `make bash_db` accedemos a una terminal dentro del container.
- Una vez dentro, ejecutamos `psql -u root -p` y cuando nos pida la contraseña ingresamos lo definido en la variable de entorno *$MYSQL\_ROOT\_PASSWORD*.
- Dentro de la terminal de MySQL ejecutamos `CREATE DATABASE <database_name>`, donde `<database_name>` es el nombre de nuestra base de datos, definido en la variable de entorno *$DATABASE_NAME* en el archivo *.env*.

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