import random

palavra = ['palavras','sorteio','ganhador','manino','menina','homem','mulher']
palavra_secreta = random.choice(palavra)
lacunas = ['_'] * len(palavra_secreta)
tentativa = set()
print(lacunas)
print(palavra_secreta)
