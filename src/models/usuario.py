class Usuario:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        self.tokens = []

    def agregar_token(self, token):
        self.tokens.append(token)
