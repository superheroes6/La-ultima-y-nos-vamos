from unittest.mock import Mock
from src.controllers.cli_controller import CLIController

def test_mis_tokens():
    mock_service = Mock()
    mock_service.nft_repo.cargar_tokens.return_value = [
        {"token_id": "1", "owner": "user1", "poll_id": "poll1", "option": "Sí", "issued_at": "2023-10-01"}
    ]
    controller = CLIController(mock_service, "user1")
    controller.mis_tokens()
    mock_service.nft_repo.cargar_tokens.assert_called_once()
