CREATE TABLE Usuario (
  id_usuario INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(80) NOT NULL,
  email VARCHAR(100) NOT NULL,
  telefono VARCHAR(15) ,
  contraseña CHAR(60) NOT NULL,
  rol ENUM("admin", "usuario") NOT NULL
);

CREATE TABLE Dispositivo (
  id_dispositivo INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  marca VARCHAR(50) NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  estado ENUM("encendido", "apagado") NOT NULL
);

CREATE TABLE Automatizacion (
  id_automatizacion INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(150) NOT NULL,
  estado ENUM("activa", "inactiva") NOT NULL
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



