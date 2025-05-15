from datetime import datetime
import uuid

class TokenNFT:
    def __init__(self, token_id=None, owner=None, poll_id=None, option=None, issued_at=None):
        self.token_id = token_id or str(uuid.uuid4())
        self.owner = owner
        self.poll_id = poll_id
        self.option = option
        self.issued_at = issued_at or datetime.now()
