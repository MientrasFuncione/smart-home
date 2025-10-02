from app.automatizacion import AutomatizacionBase

def nueva_automatizacion(self, id, nombre, descripcion):
    return AutomatizacionBase(id, nombre.capitalize(), descripcion.capitalize())


class AutomatizacionService:
    def __init__(self):
        self.automatizaciones = []
        self.id_contar = 1

    def nueva_automatizacion(self, id, nombre, descripcion):
        nueva_automatizacion = AutomatizacionBase(
            id, nombre.capitalize(), descripcion.capitalize()
        )
        return nueva_automatizacion

    def agregar_automatizacion(self, nombre, descripcion):
        if not nombre or not descripcion:
            raise ValueError("El nombre y la descripción son obligatorios")

        for automatizacion in self.automatizaciones:
            if automatizacion.nombre.lower() == nombre.lower():
                return False, "La automatización ya existe."

        nueva_automatizacion = self.nueva_automatizacion(
            str(self.id_contar), nombre, descripcion
        )
        self.automatizaciones.append(nueva_automatizacion)
        self.id_contar += 1

        return True, "La automatización fue agregada exitosamente."

    def eliminar_automatizacion(self, nombre):
        for automatizacion in self.automatizaciones:
            if automatizacion.nombre.lower() == nombre.lower():
                self.automatizaciones.remove(automatizacion)
                print("La automatización fue eliminada exitosamente.")
                return
        print("La automatización no fue encontrada.")


if __name__ == "__main__":
    servicio = AutomatizacionService()
    servicio.agregar_automatizacion(
        "Encender dispositivos", "Encender todos los dispositivos conectados"
    )

    servicio.agregar_automatizacion(
        "Apagar dispositivos", "Apagar todos los dispositivos conectados"
    )

    print("Automatizaciones:")
    for automatizacion in servicio.automatizaciones:
        print(f"- {automatizacion.nombre}: {automatizacion.descripcion}")


