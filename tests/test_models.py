import pytest
from datetime import datetime, timedelta
from src.models.encuesta import Encuesta

def test_crear_encuesta():
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    assert encuesta.id == "1"
    assert encuesta.pregunta == "¿Te gusta Python?"
    assert encuesta.opciones == ["Sí", "No"]
    assert encuesta.estado == "activa"

def test_registrar_voto():
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    encuesta.registrar_voto("Sí")
    assert encuesta.votos["Sí"] == 1

def test_registrar_voto_invalido():
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    with pytest.raises(ValueError):
        encuesta.registrar_voto("Tal vez")

def test_cerrar_encuesta():
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    encuesta.cerrar()
    assert encuesta.estado == "cerrada"
