import mysql.connector
from app.conn.db_conn import DBConnection
from app.dominio.usuario import Usuario


class UsuarioDAO:
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create(self, usuario):
        with self.connection.cursor() as cursor:
            try:
                query = "INSERT INTO Usuario (nombre, email, telefono, contraseña, rol) VALUES (%s, %s, %s, %s, %s)"
                values = (
                    usuario.nombre,
                    usuario.email,
                    usuario.telefono,
                    usuario.contraseña,
                    usuario.rol,
                )
                cursor.execute(query, values)
                self.connection.commit()
                print("Usuario creado exitosamente.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def get_user(self, nombre):
        with self.connection.cursor() as cursor:
            try:

                query = "SELECT id_usuario, nombre, email, telefono, contraseña, rol FROM Usuario WHERE nombre = %s"
                cursor.execute(query, (nombre,))
                row = cursor.fetchone()
                if row:
                    return Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
