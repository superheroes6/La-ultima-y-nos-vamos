from src.models.encuesta import Encuesta

class EncuestaFactory:
    @staticmethod
    def crear_encuesta(tipo, id, pregunta, opciones, duracion):
        if tipo == "simple":
            return Encuesta(id, pregunta, opciones, duracion)
        elif tipo == "multiple":
            encuesta = Encuesta(id, pregunta, opciones, duracion)
            encuesta.tipo = "multiple"
            return encuesta
        else:
            raise ValueError("Tipo de encuesta no soportado.")
