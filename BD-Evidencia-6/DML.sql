INSERT INTO Usuario (nombre,email,telefono,contraseña,rol) VALUES
('Gadiel','gadiel@gmail.com','3518053537', '123456789', 'admin'),
('Ezequiel','ezequiel@gmail.com','3518053538', '123456789', 'usuario'),
('Silva','silva@gmail.com','3518053539', '123456789', 'usuario'),
('Monteabaro','monteabaro@gmail.com','3518053540', '123456789', 'admin'),
('Facundo','facundo@gmail.com','3518053541', '123456789', 'admin'),
('Perez','perez@gmail.com','3518053542', '123456789', 'admin'),
('Carlos','carlos@gmail.com','3518053543', '123456789', 'usuario'),
('Arnold','arnold@gmail.com','3518053544', '123456789', 'usuario'),
('Gabriel','gabriel@gmail.com','3518053545', '123456789', 'usuario'),
('Ventura','ventura@gmail.com','3518053546', '123456789', 'usuario');

INSERT INTO Dispositivo (nombre,marca,tipo,estado) VALUES 
('Aspiradora', 'Gadnic', 'Limpieza', 'apagado'),
('Luces', 'LED', 'Iluminacion', 'apagado'),
('Aire Acondicionado', 'Samsung', 'Entretenimiento', 'encendido'),
('Televisor', 'Samsung', 'Entretenimiento', 'encendido'),
('Heladera', 'Whirlpool', 'Electrodoméstico', 'encendido'),
('Lavarropas', 'Drean', 'Electrodoméstico', 'apagado'),
('Computadora', 'Lenovo', 'Entretenimiento', 'encendido'),
('persianas', 'Lana', 'Iluminacion', 'apagado'),
('Parlante', 'Google Nest', 'Entretenimiento', 'apagado'),
('Televisor', 'Samsung', 'Entretenimiento', 'apagado');

INSERT INTO Automatizacion (nombre, descripcion, estado) VALUES 
('encender_dispositivos', 'Enciende todos los dispositivos', 'inactiva'),
('apagar_dispositivos', 'Apaga todos los dispositivos', 'activa'),
('modo_ahorro', 'Configura los dispositivos en bajo consumo', 'inactiva'),
('modo_fiesta', 'Enciende luces y parlante con música', 'activa'),
('modo_noche', 'Apaga luces y activa alarma de seguridad', 'inactiva'),
('abrir_persianas', 'Sube automáticamente las persianas', 'inactiva'),
('limpieza_full', 'Limpia durante mas tiempo la aspiradora', 'inactiva'),
('limpieza_simple', 'solo limpia durante 15 minutos', 'inactiva'),
('programar_encendido', 'Sube automáticamente las persianas', 'inactiva'),
('cerrar_persianas', 'Baja automáticamente las persianas', 'inactiva');


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

INSERT INTO DispositivoAutomatizacion (id_dispositivo, id_automatizacion) VALUES
(1, 4),
(5, 4), 
(1, 1), 
(4, 3), 
(4, 2), 
(5, 3); 

SELECT * FROM Usuario;

SELECT * FROM Dispositivo;

SELECT * FROM Automatizacion;

SELECT * FROM DispositivoUsuario;    

SELECT * FROM DispositivoAutomatizacion;

SELECT nombre
FROM Usuario;

SELECT nombre, rol
FROM Usuario
WHERE nombre = 'Facundo'; 

SELECT id_usuario, nombre, rol
FROM Usuario
WHERE id_usuario BETWEEN 3 AND 7; 

UPDATE Usuario
SET nombre = 'Gabriela', email = 'gabriela.a@ejemplo.com'
WHERE id_usuario = 9;

UPDATE Dispositivo
SET marca = 'Dyson', tipo = 'Alta Gama'
WHERE id_dispositivo = 1;


SELECT d.id_dispositivo, d.nombre, d.marca, d.tipo, d.estado FROM Dispositivo d INNER JOIN DispositivoUsuario ud ON d.id_dispositivo = ud.id_dispositivo WHERE ud.id_usuario = 1;

SELECT u.nombre AS usuario, d.nombre AS dispositivo, d.estado
FROM Usuario u
INNER JOIN DispositivoUsuario du ON u.id_usuario = du.id_usuario
INNER JOIN Dispositivo d ON du.id_dispositivo = d.id_dispositivo;



