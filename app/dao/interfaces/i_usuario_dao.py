from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    @abstractmethod
    def create(self, usuario):
        pass

    @abstractmethod
    def update_rol_user(self, id_usuario, nuevo_rol):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user(self, nombre):
        pass
