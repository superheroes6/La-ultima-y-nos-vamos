import pytest
from unittest.mock import Mock
from src.services.poll_service import PollService
from src.services.chatbot_service import ChatbotService
from src.services.nft_service import NFTService
from src.models.encuesta import Encuesta
from src.models.token_nft import TokenNFT

# PollService tests
def test_crear_encuesta():
    mock_repo = Mock()
    service = PollService(mock_repo, None, None, None)
    service.crear_encuesta("¿Te gusta Python?", ["Sí", "No"], 60)
    mock_repo.guardar_encuesta.assert_called_once()

def test_votar_encuesta():
    mock_repo = Mock()
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    mock_repo.cargar_encuesta.return_value = encuesta
    service = PollService(mock_repo, None, None, None)
    service.votar("1", "user1", "Sí")
    assert encuesta.votos["Sí"] == 1

def test_voto_duplicado():
    mock_repo = Mock()
    encuesta = Encuesta("1", "¿Te gusta Python?", ["Sí", "No"], 60)
    mock_repo.cargar_encuesta.return_value = encuesta
    mock_voto_repo = Mock()
    mock_voto_repo.obtener_votantes.return_value = ["user1"]
    service = PollService(mock_repo, mock_voto_repo, None, None)
    with pytest.raises(ValueError):
        service.votar("1", "user1", "Sí")

# ChatbotService tests
def test_chatbot_respuesta_clave():
    mock_poll_service = Mock()
    mock_poll_service.get_partial_results.return_value = {"Sí": {"conteo": 10, "porcentaje": 50}}
    service = ChatbotService(mock_poll_service)
    respuesta = service.responder("user1", "¿Quién va ganando?")
    assert "Resultados parciales" in respuesta

# NFTService tests
def test_mint_token():
    mock_repo = Mock()
    service = NFTService(mock_repo)
    service.mint_token("user1", "poll1", "Sí")
    mock_repo.guardar_token.assert_called_once()

def test_transferir_token_valido():
    mock_repo = Mock()
    token = TokenNFT("1", "user1", "poll1", "Sí")
    mock_repo.cargar_tokens.return_value = [token]
    service = NFTService(mock_repo)
    service.transfer_token("1", "user2", "user1")
    mock_repo.actualizar_token.assert_called_once_with("1", "user2")

def test_transferir_token_invalido():
    mock_repo = Mock()
    token = TokenNFT("1", "user1", "poll1", "Sí")
    mock_repo.cargar_tokens.return_value = [token]
    service = NFTService(mock_repo)
    with pytest.raises(ValueError):
        service.transfer_token("1", "user2", "user3")
