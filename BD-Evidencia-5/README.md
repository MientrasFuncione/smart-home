# Modulo Programador - DDL - DML - CONSULTAS -

### Introducción

En esta tercera instancia, comenzamos a manipular bases de datos, mediante el lenguaje de consultas denominado SQL. Vamos a crear bases de datos, dentro de ellas tablas y lograremos insertar datos a las mismas, mostrando su funcionamiento con un sentencia SQL basica.
y no tan basicas, como las UPDATE,( se actualiza el registro) WHERE,(mostrará las filas donde el valor en la columna se igual al qeu solicitamos) BETWEEN(para filtrar rangos numericos) etc.

SQL al ser un lenguaje universal, podemos usar cualquier DBMS Relacional, y las consultas seran las mismas, pero puede cambiar minimamente en algunas caracteristicas. Para esta instancia abordatemos MySQL, donde implementaremos consultas DDL Y DML. Para ello utilizaremos **One Compiler**.

**One Compiler** es una plataforma online que permite escribir, compuilar y ejecutar código desde el navegador, sin la necesidad de instalar nada en la pc. En este caso utilizaremos el compilador SQL, donde nos permite practicar queries en bases de datos.

---

### Ejecución DDL
- ** Creamos la base de datos primero**
CREATE DATABASE IF NOT EXISTS casa_inteligente_bd; (si no exite ninguan base de datos con este nombre, que se cree.)

- ** USE casa_inteligente_bd; se pone en uso la base de dato para que dentro de ella se creen las tablas.

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

---

### Correcciones

https://drive.google.com/drive/folders/1inN0brNwDzBGjtmUibzzA6DA3izD3lWq?usp=sharing

### Aclaración

Quisiera aclarar que, durante el desarrollo del proyecto, varios integrantes dejaron de participar, lo que afectó la distribución de tareas y los avances que pudimos lograr.

Aun así, me aseguré de avanzar con lo que estuvo a nuestro alcance para cumplir con los objetivos principales.

Nuestro grupo conto de numerosas bajas en el desarrollo y la incorporacion de un nuevo integrante, quedando solamente dos al momento de desarrollar, se hicieron modificaciones con respecto al trabajo anterior (habladas y aprobadas por el equipo)