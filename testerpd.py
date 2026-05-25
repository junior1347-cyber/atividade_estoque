from dataclasses import dataclass

@dataclass
class E_P:
    nome: str
    preco: float
    quantidade: int = 0

#estoque_prod = []

while True:
	try:
		print("\n --- MENU PRINCIPAL ---")
		print("1-Visulaizar estoque atual.")
		print("2-Registrar nova entrada.")		
		print("3-Registrar nova saída.")
		print("4-cancelar\n")
		opcao = int(input("\nDigite uma opção válida: \n"))
		if opcao < 1:
			print("Digite apenas números de 1 a 4!")
		if opcao > 4:
			print("Digite apenas números de 1 a 4!")
		#OPÇÃO1
		if opcao == 1:
			for produto in estoque_prod:
				print(f"Produto: {produto.nome} | Valor: R$ {produto.preco:.2f} | Estoque: {produto.quantidade} Unidades")
		#OPÇÃO2
		elif opcao == 2:
			nome = input("Nome do produto: ")
			preco = float(input("Valor: "))
			quantidade = int(input("Quantidade: "))

			novo_produto = E_P(nome, preco, quantidade)
			estoque_prod.append(novo_produto)
			print(f"produto {novo_produto.nome} adicionado com sucesso!")
		#OPÇÃO3
		elif opcao == 3:
			nome = input("Nome do produto: ")
			quantidade = int(input("Quantidade: "))
			produto_encontrado = False
			for produto in estoque_prod:
				if produto.nome == nome:
					produto_encontrado = True
					if produto.quantidade >= quantidade:
						produto.quantidade -= quantidade
						print(f"\n{quantidade} unidades removidas do produto: {nome}. Novo estoque: {produto.quantidade}")
					else:
						print(f"Quantidade disponível ({produto.quantidade}) é insuficiente para remover {quantidade} unidades de {nome}!")
					break
			if not produto_encontrado:
				print(f"Produto '{nome}' não foi encontrado no estoque.")

		#OPÇÃO4
		elif opcao == 4:
			break
	except ValueError:
		print("\nDigite apena números!")
