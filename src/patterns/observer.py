class Observer:
    def __init__(self):
        self.subscribers = []

    def registrar(self, subscriber):
        self.subscribers.append(subscriber)

    def notificar(self, evento):
        for subscriber in self.subscribers:
            subscriber.update(evento)

class EncuestaObserver:
    def update(self, evento):
        print(f"Evento recibido: {evento}")
