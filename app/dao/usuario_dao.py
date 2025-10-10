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
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def update_rol_user(self, id_usuario, nuevo_rol):
        with self.connection.cursor() as cursor:
            try:
                query = "UPDATE Usuario SET rol = %s WHERE id_usuario = %s"
                values = (
                    nuevo_rol,
                    id_usuario,
                )
                cursor.execute(query, values)
                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def get_all(self):
        with self.connection.cursor() as cursor:
            try:
                query = "SELECT id_usuario, nombre, email, telefono,  rol FROM Usuario"
                cursor.execute(query)
                rows = cursor.fetchall()
                usuarios = [
                    Usuario(id=r[0], nombre=r[1], email=r[2], telefono=r[3], rol=r[4])
                    for r in rows
                ]
                return usuarios
            except mysql.connector.Error as err:
                raise Exception(f"Error al listar usuarios: {err}")

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
