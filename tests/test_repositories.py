import pytest
from src.repositories.encuesta_repo import EncuestaRepository
from src.models.encuesta import Encuesta

def test_guardar_y_cargar_encuesta():
    repo = EncuestaRepository("test_encuestas.json")
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    repo.guardar_encuesta(encuesta)
    encuesta_cargada = repo.cargar_encuesta()
    assert encuesta_cargada.pregunta == encuesta.pregunta
