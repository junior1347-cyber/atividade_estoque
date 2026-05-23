import os
from dataclasses import dataclass


def limpar_tela():
	os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class E_P:
    nome: str
    preco: float
    quantidade: int

estoque_prod = [
	 E_P("Tablet", 5000.00, 100),
	 E_P("Notebook", 7000.00, 100),
	 E_P("Smartphone", 5000.00, 100),
]

while True:
	try:
		limpar_tela()

		print("\n --- MENU PRINCIPAL ---")
		print("1-Visulaizar estoque atual.")
		print("2-Registrar nova entrada.")
		print("3-Registrar nova saída.")
		print("4-cancelar\n")
		opcao = int(input("\nDigite uma opção válida: "))

		#OPÇÃO1
		if opcao == 1:
			for produto in estoque_prod:
				print(f"Produto: {produto.nome} | Valor: R$ {produto.preco:.2f} | Estoque: {produto.quantidade} Unidades")
		#OPÇÃO2
		if opcao == 2:
			nome = input("Nome do produto: ")
			preco = input("Valor: ")
			quantidade = input("Quantidade: ")

			novo_produto = E_P(nome, float(preco), int(quantidade))
			estoque_prod.append(novo_produto)
			print(f"produto {novo_produto.nome} adicionado com sucesso!")

		#OPÇÃO4
		if opcao == 4:
			break
	except ValueError:
		print()
