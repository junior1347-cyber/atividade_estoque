estoque_cont = {
	"cabo de rede": {"preco": 50.00, "quantidade": 5 },
	"bateria moura": {"preco": 40.00, "quantidade": 10 },
	"pilha AAA": {"preco": 20.00, "quantidade": 100 },
}
while True:

	try:
		print("\n--- MENU PRINCIPAL ---")
		print("1-Visualizar estoque atual")
		print("2-Registrar entrada de produto")
		print("3-Registrar saída de produto")
		print("4-Sair do sistema\n")

		opcao = int(input(" Escolha uma opção:  "))

		#OPÇÃO1
		if opcao == 1:
			for c, v in estoque_cont.items():
				print(f"{c}: R$ {v["preco"]:.2f}")

		#OPÇÃO2
		if opcao == 2:
			produto = input("Nome do produto: ")
			preco_produto = float(input("Preço: "))
			qtd_produto = int(input("Quantidade a adicionar: "))

			estoque_cont[produto] = {"preco": preco_produto, "quantidade": qtd_produto}

		#OPÇÃO3
		if opcao == 3:
			produto_ret = input("Nome do produto: ")
			qtd_ret = int(input("Quantidade a retirar: "))
			estoque_cont[produto_ret] = {"quantidade": estoque_cont.pop(produto)}
		#OPÇÃO4
		if opcao == 4:
			break

	except ValueError:
		print("Digite apenas numeros válidos!")
