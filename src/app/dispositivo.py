class Dispositivo:
    def __init__(self, id, nombre, marca, tipo, estado="apagado"):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__marca = marca
        self.__estado = estado  # "encendido" o "apagado"

    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    # nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # tipo
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    # marca
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    # estado
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in ["encendido", "apagado"]:
            raise ValueError("El estado debe ser 'encendido' o 'apagado'.")
        self.__estado = nuevo_estado

    def __str__(self):
        return f"Dispositivo(id={self.id}, nombre={self.nombre}, tipo={self.tipo}, estado={self.estado})"

    def encender_dispositivo(self):
        if self.estado == "encendido":
            print(f"El dispositivo {self.nombre} ya está encendido.")
        else:
            self.estado = "encendido"
            print(f"El dispositivo {self.nombre} ha sido encendido.")

    def apagar_dispositivo(self):
        if self.estado == "apagado":
            print(f"El dispositivo {self.nombre} ya está apagado.")
        else:
            self.estado = "apagado"
            print(f"El dispositivo {self.nombre} ha sido apagado.")
