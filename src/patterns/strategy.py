class DesempateStrategy:
    def __init__(self, metodo):
        self.metodo = metodo

    def resolve(self, votos):
        if self.metodo == "alfabetico":
            return min(votos.keys())
        elif self.metodo == "aleatorio":
            import random
            return random.choice(list(votos.keys()))
        else:
            raise ValueError("Método de desempate no soportado.")
