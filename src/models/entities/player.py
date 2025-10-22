class Player:
    def __init__(self, nome, level, classe, hp_max, dano):
        self.nome = nome
        self.level = level
        self.classe = classe
        self.hp = hp_max
        self.hp_max = hp_max
        self.dano = dano
        self.localizacao = 0


    def atacar(self, inimigo):
        dano_ataque = self.dano 
        inimigo.hp -= self.dano
        print(f"{inimigo.nome} e sofreu {self.dano} de dano!")

