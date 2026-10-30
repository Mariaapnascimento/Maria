class Bebida:
    def __init__(self, nome, preco, volume_ml):
        self.nome = nome
        self.preco = preco
        self.volume_ml = volume_ml
    def servir(self):
        print(f"Servindo {self.nome} ({self.volume_ml}ml) - R${self.preco:.2f}")
class Refrigerante(Bebida):
    def __init__(self, nome, preco, volume_ml, com_gas):
        super().__init__(nome, preco, volume_ml)
        self.com_gas = com_gas
    def servir(self):
        print(f"{self.nome} ({self.volume_ml}ml)- R${self.preco:.2f} (com gás)")
class Suco(Bebida):
    def __init__(self, nome, preco, volume_ml, natural):
        super().__init__(nome, preco, volume_ml)
        self.natural = natural
    def servir(self):
        print(f"{self.nome} ({self.volume_ml}ml) - R${self.preco:.2f} (natural)")


r = Refrigerante("Fanta", 6.00, 300, True)
s = Suco("Laranja", 5.00, 500, True)

r.servir()
s.servir()
