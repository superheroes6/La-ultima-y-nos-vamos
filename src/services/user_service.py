import bcrypt
import uuid

class UserService:
    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo
        self.sesiones = {}  # Diccionario para manejar sesiones activas

    def register(self, username, password):
        # Verificar si el usuario ya existe
        usuarios = self.usuario_repo.cargar_usuario()
        if username in usuarios:
            raise ValueError("El nombre de usuario ya existe.")

        # Generar hash de la contraseña
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Guardar el usuario
        usuarios[username] = {"password_hash": password_hash.decode('utf-8')}
        self.usuario_repo.guardar_usuario(usuarios)

    def login(self, username, password):
        # Cargar usuarios
        usuarios = self.usuario_repo.cargar_usuario()
        if username not in usuarios:
            raise ValueError("Usuario no encontrado.")

        # Verificar contraseña
        password_hash = usuarios[username]["password_hash"].encode('utf-8')
        if not bcrypt.checkpw(password.encode('utf-8'), password_hash):
            raise ValueError("Contraseña incorrecta.")

        # Generar token de sesión
        session_token = str(uuid.uuid4())
        self.sesiones[session_token] = username
        return session_token
