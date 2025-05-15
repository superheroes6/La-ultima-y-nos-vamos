from unittest.mock import Mock
from src.patterns.observer import Observer
from src.patterns.factory import EncuestaFactory
from src.patterns.strategy import DesempateStrategy

# Observer tests
def test_observer_notificacion():
    mock_observer = Mock()
    mock_observer.update = Mock()
    observer = Observer()
    observer.registrar(mock_observer)
    observer.notificar("encuesta_cerrada")
    mock_observer.update.assert_called_once_with("encuesta_cerrada")

# Factory tests
def test_factory_crear_encuesta():
    factory = EncuestaFactory()
    encuesta = factory.crear_encuesta("simple", "¿Te gusta Python?", ["Sí", "No"], 60)
    assert encuesta.pregunta == "¿Te gusta Python?"

# Strategy tests
def test_strategy_desempate_alfabetico():
    strategy = DesempateStrategy("alfabetico")
    resultado = strategy.resolve({"Sí": 10, "No": 10})
    assert resultado == "No"
