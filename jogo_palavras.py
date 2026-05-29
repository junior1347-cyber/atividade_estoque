import random

palavra = ['bicicleta','gato','ganhador','amigo','menina','homem','carro']
palavra_secreta = random.choice(palavra)
lacunas = ['_'] * len(palavra_secreta)
tentativa = set()
print(lacunas)
print(palavra_secreta)

