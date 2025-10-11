from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    @abstractmethod
    def create(self, usuario):
        """Crea un nuevo usuario"""
        pass

    @abstractmethod
    def update_rol_user(self, id_usuario, nuevo_rol):
        """Actualiza el rol de un usuario"""
        pass

    @abstractmethod
    def get_all(self):
        """Devuelve todos los usuarios"""
        pass

    @abstractmethod
    def get_user(self, nombre):
        """Busca un usuario por nombre"""
        pass
