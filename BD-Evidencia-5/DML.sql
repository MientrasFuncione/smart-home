

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
('cerrar_persianas', 'Baja automáticamente las persianas', 'inactiva');

INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES (5, 8); # Facundo usa persianas
INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES (7, 6); # Carlos usa lavarropas
# Metodo mas simple
INSERT INTO DispositivoUsuario (id_usuario, id_dispositivo) VALUES
(1, 1), # Gadiel tiene Aspiradora
(5, 2), # Facundo tiene Luces
(2, 4), # Ezequiel tiene Televiso
(6, 7), # Perez tiene Computadora
(3, 2), # Silva contrla las Luces
(8, 5); # Arnol tiene Heladera

INSERT INTO DispositivoAutomatizacion (id_dispositivo, id_automatizacion) VALUES
(2, 4), # Luces enciende modo fiesta
(9, 4), # Parlante enciende modo giesta
(1, 1), # Aspiradoa se enciende
(2, 3), #luces Modo Ahorro  
(1, 2), # aspiradora se aoaga el dispositivo 
(3, 3); # Aire acondicionado modo ahorro