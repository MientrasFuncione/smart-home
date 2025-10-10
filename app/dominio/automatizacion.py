class Automatizacion:
    def __init__(self, id, nombre, descripcion, estado="inactiva"):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def activar(self, dispositivos):

        if self.estado != "activa":
            print("La automatización no está activada.")
            return

        if self.nombre == "Encender todos los dispositivos":
            for dispositivo in dispositivos:
                # metodo creado en la clase dispositivo
                dispositivo.encender_dispostivo()
            print(f"Todos los dispositivos han sido encendidos")

        if self.nombre == "Apagar todos los dispositivos":
            for dispositivo in dispositivos:
                # metodo creado en la clase dispositivo
                dispositivo.apagar_dispostivo()
            print(f"Todos los dispositivos han sido apagados")
