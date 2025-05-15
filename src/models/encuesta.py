from datetime import datetime

class Encuesta:
    def __init__(self, id, pregunta, opciones, duracion):
        self.id = id
        self.pregunta = pregunta
        self.opciones = opciones
        self.votos = {opcion: 0 for opcion in opciones}
        self.estado = "activa"
        self.creada_en = datetime.now()
        self.duracion = duracion

    def registrar_voto(self, opcion):
        if self.estado != "activa":
            raise ValueError("La encuesta no está activa.")
        if opcion not in self.opciones:
            raise ValueError("Opción inválida.")
        self.votos[opcion] += 1

    def cerrar(self):
        self.estado = "cerrada"
