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
('Aspiradora', 'Gadnic', 'Limpieza', 'apagado'),
('Luces', 'LED', 'Iluminacion', 'apagado'),
('Aire Acondicionado', 'Samsung', 'Entretenimiento', 'encendido'),
('Televisor', 'Samsung', 'Entretenimiento', 'encendido'),
('Heladera', 'Whirlpool', 'Electrodoméstico', 'encendido'),
('Lavarropas', 'Drean', 'Electrodoméstico', 'apagado'),
('Computadora', 'Lenovo', 'Entretenimiento', 'encendido'),
('persianas', 'Lana', 'Iluminacion', 'apagado'),
('Parlante', 'Google Nest', 'Entretenimiento', 'apagado');

INSERT INTO Automatizacion (nombre, descripcion, estado) VALUES 
('encender_dispositivos', 'Enciende todos los dispositivos', 'inactiva'),
('apagar_dispositivos', 'Apaga todos los dispositivos', 'activa'),
('modo_ahorro', 'Configura los dispositivos en bajo consumo', 'inactiva'),
('modo_fiesta', 'Enciende luces y parlante con música', 'activa'),
('modo_noche', 'Apaga luces y activa alarma de seguridad', 'inactiva'),
('abrir_persianas', 'Sube automáticamente las persianas', 'inactiva'),
('cerrar_persianas', 'Baja automáticamente las persianas', 'inactiva');

INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES (5, 8); 
INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES (7, 6); 

INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES
(1, 1), 
(5, 2), 
(2, 4),
(6, 7),
(3, 2), 
(8, 5);

INSERT INTO DispositivoAutomatizacion (id_dispositivo, id_automatizacion) VALUES
(2, 4),
(9, 4), 
(1, 1), 
(2, 3), 
(1, 2), 
(3, 3); 

SELECT * FROM Usuario;

SELECT * FROM Dispositivo;

SELECT * FROM Automatizacion;

SELECT * FROM Usuario;

SELECT * FROM Dispositivo;

SELECT * FROM Automatizacion;

SELECT * FROM DispositivoUsuario;    

SELECT * FROM DispositivoAutomatizacion;

SELECT nombre
FROM Usuario;

SELECT nombre, rol
FROM Usuario
WHERE nombre = 'Facundo'; # Selecciona El rol de "facudno"

SELECT id_usuario, nombre, rol
FROM Usuario
WHERE id_usuario BETWEEN 3 AND 7; # Seleccionar usuarios cuyos ID están entre 3 y 7 (Silva, Monteabaro, Facundo, Perez, Carlos)

UPDATE Usuario
SET nombre = 'Gabriela', email = 'gabriela.a@ejemplo.com'
WHERE id_usuario = 9; # Actualiza el registro del Usuario 9 (Gabriel)

UPDATE Dispositivo
SET marca = 'Dyson', tipo = 'Alta Gama'
WHERE id_dispositivo = 1; # Cambiar la marca y el tipo de la Aspiradora (ID 1)

