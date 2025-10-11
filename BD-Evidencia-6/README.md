# Modulo Programador - DDL Y DML

### Introducción

En esta cuarta instancia, comenzamos a trabajar con bases de datos utilizando el lenguaje de consultas SQL. Aprenderemos a crear bases de datos, definir tablas, insertar datos y ejecutar consultas básicas para mostrar su funcionamiento.

SQL es un lenguaje universal, por lo que las consultas son prácticamente iguales en cualquier sistema de gestión de bases de datos relacional (DBMS), aunque algunas características puedan variar ligeramente. Para esta instancia, trabajaremos con MySQL, enfocándonos en consultas DDL (Data Definition Language) y DML (Data Manipulation Language).

Para realizar las prácticas, utilizaremos **One Compiler**, una plataforma online que permite escribir, compilar y ejecutar código directamente desde el navegador, sin necesidad de instalar software adicional. En nuestro caso, usaremos su compilador SQL para practicar consultas sobre bases de datos.

Durante esta instancia se abordarán desde sentencias simples hasta consultas con condiciones, consultas multitabla y subconsultas, permitiendo interactuar con distintos niveles de complejidad en la manipulación de datos.

Para mayor comodidad, incluimos el enlace a la plataforma donde se trabajaron todas las sentencias correspondientes.

Para mayor comodidad incorporamos el link respectivo, en donde se trabajo las sentencias correspondientes.

https://onecompiler.com/mysql/43whwdhas

---

### Ejecución DDL

- **Crear Tablas**

Para crear las tablas en SQL, utilizaremos la sentencia CREATE TABLE, especificando el nombre de la tabla, especificando al motor de bases de datos (MySQL) como se llama la tabla, sus columnas, el tipo de datos y sus respectivas restricciones.

```sql
CREATE TABLE Usuario (
  id_usuario INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(150) NOT NULL,
  email VARCHAR(150) NOT NULL,
  telefono VARCHAR(150) ,
  contraseña VARCHAR(150) NOT NULL,
  rol VARCHAR(150) NOT NULL
);
```

En este caso creamos la tabla Usuario. Donde haremos lo mismo con las demas tablas de nuestro modelo. Lo mismo haremos con Automatizacion y Dispositivo.

```sql

CREATE TABLE Dispositivo (
  id_dispositivo INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(150) NOT NULL,
  marca VARCHAR(150) NOT NULL,
  tipo VARCHAR(150) NOT NULL,
  estado VARCHAR(150) NOT NULL
);

CREATE TABLE Automatizacion (
  id_automatizacion INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(150) NOT NULL,
  descripcion VARCHAR(150) NOT NULL,
  estado VARCHAR(150) NOT NULL
);

CREATE TABLE DispositivoUsuario(
  id_usuario INT not null,
  id_dispositivo INT not null,
  foreign key (id_usuario) references Usuario(id_usuario),
  foreign key (id_dispositivo) references Dispositivo(id_dispositivo)
);

CREATE TABLE DispositivoAutomatizacion(
  id_dispositivo INT not null,
  id_automatizacion INT not null,
  foreign key (id_dispositivo) references Dispositivo(id_dispositivo),
  foreign key (id_automatizacion) references Automatizacion(id_automatizacion)
);
```

Podemos visualizar tambien que podemos crear las tablas intermedias o conocidas como **JOIN TABLE** donde las dos tablas intermedias representan una relacion N:M entre dos tablas.

---

### Ejecución DML

- **Insertar Datos**

Ahora continuamos con la manipulación de datos, lo cual DML nos permite manipular los datos dentro de las tablas, sin tocar la estructura.

Para inserta datos utilizaremos la sentencia **INSERT INTO**, donde deberemos especificar la tabla a la cual queremos ingresar los datos, con sus respectivos valores.

```sql
INSERT INTO Usuario (nombre,email,telefono,contraseña,rol) VALUES
('Gadiel','gadiel@gmail.com','3518053537', '123456789', 'admin'),
('Ezequiel','ezequiel@gmail.com','3518053538', '123456789', 'usuario'),
('Silva','silva@gmail.com','3518053539', '123456789', 'usuario'),
('Monteabaro','monteabaro@gmail.com','3518053540', '123456789', 'usuario'),
('Facundo','facundo@gmail.com','3518053541', '123456789', 'usuario'),
('Perez','perez@gmail.com','3518053542', '123456789', 'usuario'),
('Carlos','carlos@gmail.com','3518053543', '123456789', 'usuario'),
('Arnold','arnold@gmail.com','3518053544', '123456789', 'usuario'),
('Gabriel','gabriel@gmail.com','3518053545', '123456789', 'usuario'),
('Ventura','ventura@gmail.com','3518053546', '123456789', 'usuario');
```

Podemos visualizar que se especifica el nombre de la tabla, en este caso **“Usuario”**,  se especifica las columnas a las que se ingresaran los datos y posteriormente usaremos la palabra clave **VALUES,**  dond ahi meteremos todos los valores de cada columna, en el ejemplo mostrado, podemos ver que se ingresaron un total de diez (10) filas a la tabla **“Usuario”**

---

- **Consultar Datos**

En esta instancia solo se proporciono una consulta simple, donde simplemente mostraremos los datos ingresados en cada tabla.

Para ellos usamos la sentencia **SELECT,**  la cual nos permite mostrar los datos de una tabla, ya sea todos los datos o simplemente siguiendo condiciones, especificar que datos mostrar de una tabla.

```sql
select * FROM Usuario;

select * FROM Dispositivo;

select * FROM Automatizacion
```

En este caso utilizaremos el simbolo **“*”,** el cual toma todos los datos de una tabla especifica y los muestra sin ningun tipo de condición.

Para mejor practica es recomendable aclarar cuales son los atributos que queremos leer en la sentencia.

```sql
select nombre, email, telefono, rol FROM Usuario;
```

- Consultas multitabla

```sql
INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES
(1, 1), 
(5, 2), 
(1, 4),
(1, 7),
(4, 2),
(6, 2),
(4, 2), 
(4, 2), 
(6, 2), 
(4, 1);
```

En este caso tenemos una tabla intermedia, la cual almacena el id que hace referencia al usuario como al dispositivo.

```sql
SELECT d.id_dispositivo, d.nombre, d.marca, d.tipo, d.estado 
FROM Dispositivo d INNER JOIN DispositivoUsuario ud 
ON d.id_dispositivo = ud.id_dispositivo 
WHERE ud.id_usuario = 1;
```

En esta sentencia indicamos qué columnas queremos obtener: en este caso, seleccionamos el id, nombre, marca, tipo y estado del dispositivo.

Luego especificamos la tabla de donde vamos a solicitar esos datos.

Un punto muy importante es el uso de INNER JOIN, que nos permite combinar datos de dos tablas, en este caso Usuarios y Dispositivos, basándonos en una condición específica.

Finalmente, utilizamos WHERE como un filtro, limitando los resultados a aquellos registros que cumplen con la condición dada. En este ejemplo, solo se devuelven los dispositivos asociados al usuario cuyo id es 1.

```sql
SELECT u.nombre AS usuario, d.nombre AS dispositivo, d.estado
FROM Usuario u
INNER JOIN DispositivoUsuario du ON u.id_usuario = du.id_usuario
INNER JOIN Dispositivo d ON du.id_dispositivo = d.id_dispositivo;
```

En esta instancia vamos un poco más al grano. La consulta permite visualizar de manera directa el nombre del usuario y el nombre del dispositivo, junto con el estado del mismo. Es menos precisa que otras consultas más específicas, pero resulta útil para obtener y ver los datos de forma más sencilla y rápida.

---

- Sentencias con condiciones o filtro

```sql
SELECT nombre, rol
FROM Usuario
WHERE nombre = 'Facundo';
```

Sentencia sencilla que devuelve el nombre y el rol de un determinado usuario, en este caso “Facundo”

```sql
SELECT id_usuario, nombre, rol
FROM Usuario
WHERE id_usuario BETWEEN 3 AND 7;
```

Esta sentencia nos permite devolver el id, nombre y rol de un conjunto determinado de usuarios, filtrando por su id. No se utilizó en el proyecto main, pero es útil para **aprender a usar operadores de rango** como between.