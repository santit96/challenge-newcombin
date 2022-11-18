### Instalacion 

Requiere de docker y docker-compose

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

* #### Tests

Para correr los tests se debe ejecutar `make bash` para acceder a una terminal dentro del container.
Una vez dentro, ejecutamos `python manage.py test`.
Se deberían ejecutar los tests y deberían aparecer en consola los resultados

### Uso

Una vez seguidos estos pasos se habrá levantado la aplicación en el puerto 8000 de nuestra máquina. Para acceder http://localhost:8000

- Con un GET a http://localhost:8000/api/payables se mostrara el listado de boletas de pago no pagas. Se puede filtrar por tipo de servicio si se agrega el parametro GET "service_type" a la URL con el valor a filtrar. Ej:
http://localhost:8000/api/payables?service_type=agua
- Con un GET a http://localhost:8000/api/transactions se mostrara el listado de transacciones acumuladas por día con su monto total y la cantidad. Se puede filtrar por rango de fecha de pago si se agregan los parametro GET "payment_day__gte" para indicar el limite inferior y payment_day__lte para indicar el limite inferior, ej para mostrar los pagos de los dias 16, 17 y 18 de noviembre:
http://localhost:8000/api/transactions?payment_day__gte=2022-11-18&payment_day__lte=2022-11-16
Si queremos que el rango sea abierto y no cerrado, debemos cambiar el prefijo lte o gte del final del parámetro por lt o gt según correponda.
- POST a http://localhost:8000/api/payables con los correspondientes parametros en formato json para crear una boleta de pago, un ejemplo de los datos a enviar en el body podría ser el siguiente:
```
{
    "barcode": 123456789,
    "service_type": "Agua",
    "service_description": "ABSA",
    "expiration": "2017-20-2",
    "amount": 100,
    "status": "pending"
}
```
- POST a http://localhost:8000/api/transactions con los correspondientes parametros en formato json para crear una transacción de pago. Un ejemplo de los datos a enviar en el body podría ser el siguiente:
```
{
    "payment_method": "credit_car",
    "card_number": 123456789,
    "amount": 100,
    "payment_date": 2022-11-20,
    "barcode": 123456789
}
```

#### Resumen de comandos *make* disponibles:


- `make up`: crea/arranca los containers
- `make build`: build (o rebuild) de la imagen docker
- `make create_db`: crea la base de datos en el container mysql
- `make down/stop`: para la ejecución de los containers
- `make prune`: elimina los containers
- `make ps`: muestra los containers del proyecto en ejecución
- `make bash`: permite ingresar a la consola del container de python
- `make bash_db`: permite ingresar a la consola del container de mysql
- `make logs`: muestra los logs de todos los containers del proyecto