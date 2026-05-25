# Importa o decorador dataclass para criar classes de dados de forma simplificada
from dataclasses import dataclass

# Define a estrutura de dados para o estoque de produtos
@dataclass
class E_P:
    nome: str         # Nome do produto (Texto)
    preco: float       # Preço do produto (Número decimal)
    quantidade: int = 0  # Quantidade em estoque (Inteiro, padrão é 0 caso não informado)

# Inicializa a lista vazia que servirá como banco de dados temporário do estoque
estoque_prod = []

# Inicia o laço de repetição infinito para manter o menu ativo
while True:
	# Bloco de tratamento de erros para capturar entradas inválidas do usuário
	try:
		# Exibe as opções do menu na tela
		print("\n --- MENU PRINCIPAL ---")
		print("1-Visualizar estoque atual.")
		print("2-Registrar nova entrada.")
		print("3-Registrar nova saída.")
		print("4-Cancelar\n")
		
		# Recebe a opção do usuário e converte para número inteiro
		opcao = int(input("Digite uma opção válida: "))

		# OPÇÃO 1: Visualizar o estoque atual
		if opcao == 1:
			# Verifica se o estoque está totalmente vazio
			if not estoque_prod:
				print("\nO estoque está vazio no momento.")
			else:
				# Percorre a lista e exibe os detalhes de cada produto formatados
				for produto in estoque_prod:
					print(f"Produto: {produto.nome} | Valor: R$ {produto.preco:.2f} | Estoque: {produto.quantidade} Unidades")
		
		# OPÇÃO 2: Registrar a entrada/cadastro de um novo produto
		elif opcao == 2:
			nome = input("Nome do produto: ")
			preco = float(input("Valor: "))
			quantidade = int(input("Quantidade: "))

			# Cria um novo objeto da classe E_P com os dados digitados
			novo_produto = E_P(nome, preco, quantidade)
			# Adiciona o novo produto no final da lista de estoque
			estoque_prod.append(novo_produto)
			print(f"Produto {novo_produto.nome} adicionado com sucesso!")
		
		# OPÇÃO 3: Registrar a saída/remoção de itens do estoque
		elif opcao == 3:
			nome = input("Nome do produto: ")
			quantidade = int(input("Quantidade: "))
			produto_encontrado = False  # Flag para controle de existência do produto
			
			# Busca o produto na lista pelo nome
			for produto in estoque_prod:
				if produto.nome == nome:
					produto_encontrado = True  # Sinaliza que o produto existe
					# Verifica se a quantidade solicitada está disponível
					if produto.quantidade >= quantidade:
						produto.quantidade -= quantidade  # Deduz do estoque atual
						print(f"\n{quantidade} unidades removidas do produto: {nome}. Novo estoque: {produto.quantidade}")
					else:
						print(f"Quantidade disponível ({produto.quantidade}) é insuficiente para remover {quantidade} unidades de {nome}!")
					break  # Interrompe o loop após processar o produto encontrado
			
			# Mensagem caso o produto digitado não conste na lista
			if not produto_encontrado:
				print(f"Produto '{nome}' não foi encontrado no estoque.")

		# OPÇÃO 4: Encerrar a execução do sistema
		elif opcao == 4:
			print("Encerrando o programa. Até logo!!")
			break  # Quebra o laço 'while True' e finaliza o script
		
		# Captura qualquer número digitado que não seja de 1 a 4
		else:
			print("\nOpção inválida! Digite apenas números de 1 a 4.")
			
	# Captura o erro caso o usuário digite letras ou símbolos onde o sistema espera números (int/float)
	except ValueError:
		print("\nErro: Digite apenas números válidos!")

