import Semana_14.clases.postre as p

# Horneado hereda de postre
class Horneado(p.Postre):

    def __init__(self, temperatura):
        self = super()
        self.temperatura = temperatura
