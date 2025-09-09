import random
from models.entities.enemies import Enemies


def gerar_inimigo():
    especies = ["Goblin", "Esqueleto Possuido", "Urso Raivoso", "Dragão"]
    especie = random.choice(especies)
    enemie = Enemies(especie, 100, random.randint(1, 10), 20)
    print(f"Apareceu um {enemie.especie} de nível {enemie.level} com {enemie.hp_max} de HP e {enemie.dano} de dano!")