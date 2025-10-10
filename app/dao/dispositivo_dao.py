import mysql.connector
from app.conn.db_conn import DBConnection
from app.dominio.dispositivo import Dispositivo


class DispositivoDAO:
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create_device(self, dispositivo, id_usuario):
        with self.connection.cursor() as cursor:
            try:
                query = "INSERT INTO Dispositivo (nombre, marca, tipo, estado) VALUES (%s, %s, %s, %s)"
                values = (
                    dispositivo.nombre,
                    dispositivo.marca,
                    dispositivo.tipo,
                    dispositivo.estado,
                )
                cursor.execute(query, values)

                id_dispositivo = cursor.lastrowid

                query = "INSERT INTO DispositivoUsuario (id_usuario,id_dispositivo) VALUES (%s, %s)"
                values = (id_usuario, id_dispositivo)
                cursor.execute(query, values)

                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def get_all(self):
        with self.connection.cursor() as cursor:
            try:
                query = (
                    "SELECT id_dispositivo, nombre,marca,tipo,estado FROM Dispositivo"
                )
                cursor.execute(query)
                rows = cursor.fetchall()
                dispositivos = [Dispositivo(r[0], r[1], r[2], r[3], r[4]) for r in rows]
                return dispositivos

            except mysql.connector.Error as err:
                raise Exception(f"Error al consultar los dispositivos: {err}")

    def get_device_by_user(
        self,
        id_usuario,
    ):
        with self.connection.cursor() as cursor:
            try:
                query = "SELECT d.id_dispositivo, d.nombre, d.marca, d.tipo, d.estado FROM Dispositivo d INNER JOIN DispositivoUsuario ud ON d.id_dispositivo = ud.id_dispositivo WHERE ud.id_usuario = %s"

                cursor.execute(query, (id_usuario,))
                rows = cursor.fetchall()
                return [Dispositivo(r[0], r[1], r[2], r[3], r[4]) for r in rows]
            except mysql.connector.Error as err:
                raise Exception(f"Error al consultar los dispositivos: {err}")
