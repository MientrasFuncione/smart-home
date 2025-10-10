SELECT * FROM Usuario;

SELECT * FROM Dispositivo;

SELECT * FROM Automatizacion

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