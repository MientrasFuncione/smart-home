CREATE TABLE Usuario (
  id_usuario INT primary key not null AUTO_INCREMENT,
  nombre VARCHAR(150) NOT NULL,
  email VARCHAR(150) NOT NULL,
  telefono VARCHAR(150) ,
  contraseña VARCHAR(150) NOT NULL,
  rol VARCHAR(150) NOT NULL
);

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

INSERT INTO Dispositivo (nombre,marca,tipo,estado) VALUES 
('Aspiradora', 'Gadnic', 'Limpieza', 'apagada'),
('Luces', 'LED', 'Iluminacion', 'apagada'),
('Aire Acondicionado', 'Samsung', 'Entretenimiento', 'encendida'),
('Televisor', 'Samsung', 'Entretenimiento', 'encendida'),
('Heladera', 'Whirlpool', 'Electrodoméstico', 'encendida'),
('Lavarropas', 'Drean', 'Electrodoméstico', 'apagada'),
('Computadora', 'Lenovo', 'Entretenimiento', 'encendida'),
('persianas', 'Lana', 'Iluminacion', 'apagada'),
('Parlante', 'Google Nest', 'Entretenimiento', 'apagada');

INSERT INTO Automatizacion (nombre, descripcion, estado) VALUES 
('encender_dispositivos', 'Enciende todos los dispositivos', 'inactiva'),
('apagar_dispositivos', 'Apaga todos los dispositivos', 'activa'),
('modo_ahorro', 'Configura los dispositivos en bajo consumo', 'inactiva'),
('modo_fiesta', 'Enciende luces y parlante con música', 'activa'),
('modo_noche', 'Apaga luces y activa alarma de seguridad', 'inactiva'),
('abrir_persianas', 'Sube automáticamente las persianas', 'inactiva'),
('cerrar_persianas', 'Baja automáticamente las persianas', 'inactiva')
