from app.conn.db_conn import DBConnection
import mysql.connector


class UsuarioDAO:
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create(self, usuario):
        try:
            cursor = self.connection.cursor()
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
        finally:
            cursor.close()
