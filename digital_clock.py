import datetime
import pytz
import time
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_relogio():
    """Exibe um relógio digital com múltiplos fusos horários"""
    
    # Dicionário com fusos horários principais
    fusos = {
        "🌍 GMT/UTC (Londres)": "UTC",
        "🌎 EST (Nova York)": "America/New_York",
        "🌎 CST (Chicago)": "America/Chicago",
        "🌎 PST (Los Angeles)": "America/Los_Angeles",
        "🌏 JST (Tóquio)": "Asia/Tokyo",
        "🌏 IST (Índia)": "Asia/Kolkata",
        "🌏 AEST (Sydney)": "Australia/Sydney",
        "🇧🇷 BRT (São Paulo)": "America/Sao_Paulo",
    }
    
    try:
        while True:
            limpar_tela()
            
            print("=" * 60)
            print(" " * 15 + "⏰ RELÓGIO MUNDIAL DIGITAL ⏰")
            print("=" * 60)
            print()
            
            # Obtém a hora atual para cada fuso horário
            for nome_fuso, codigo_fuso in fusos.items():
                tz = pytz.timezone(codigo_fuso)
                hora_atual = datetime.datetime.now(tz)
                
                # Formata a hora: HH:MM:SS
                hora_formatada = hora_atual.strftime("%H:%M:%S")
                data_formatada = hora_atual.strftime("%d/%m/%Y")
                
                print(f"{nome_fuso}")
                print(f"  ⌚ Hora: {hora_formatada}")
                print(f"  📅 Data: {data_formatada}")
                print()
            
            print("=" * 60)
            print("Pressione Ctrl+C para sair | Atualizando a cada 1 segundo...")
            print("=" * 60)
            
            # Aguarda 1 segundo antes de atualizar
            time.sleep(1)
            
    except KeyboardInterrupt:
        limpar_tela()
        print("\n👋 Relógio encerrado!")
        print("Obrigado por usar o Relógio Mundial Digital!")

def menu_personalizado():
    """Menu para o usuário escolher quais fusos horários ver"""
    
    fusos_disponiveis = {
        "1": ("UTC (Londres)", "UTC"),
        "2": ("EST (Nova York)", "America/New_York"),
        "3": ("CST (Chicago)", "America/Chicago"),
        "4": ("PST (Los Angeles)", "America/Los_Angeles"),
        "5": ("JST (Tóquio)", "Asia/Tokyo"),
        "6": ("IST (Índia)", "Asia/Kolkata"),
        "7": ("AEST (Sydney)", "Australia/Sydney"),
        "8": ("BRT (São Paulo)", "America/Sao_Paulo"),
    }
    
    print("\n" + "=" * 60)
    print("FUSOS HORÁRIOS DISPONÍVEIS:")
    print("=" * 60)
    for chave, (nome, _) in fusos_disponiveis.items():
        print(f"{chave} - {nome}")
    print("0 - Ver todos os fusos horários")
    print("=" * 60)
    
    escolha = input("\nDigite o número do fuso horário desejado (ou 0 para todos): ").strip()
    
    return escolha, fusos_disponiveis

def exibir_relogio_personalizado(fusos_escolhidos):
    """Exibe relógio apenas com os fusos horários escolhidos"""
    
    try:
        while True:
            limpar_tela()
            
            print("=" * 60)
            print(" " * 15 + "⏰ RELÓGIO DIGITAL PERSONALIZADO ⏰")
            print("=" * 60)
            print()
            
            # Obtém a hora atual para cada fuso horário escolhido
            for nome_fuso, codigo_fuso in fusos_escolhidos.items():
                tz = pytz.timezone(codigo_fuso)
                hora_atual = datetime.datetime.now(tz)
                
                hora_formatada = hora_atual.strftime("%H:%M:%S")
                data_formatada = hora_atual.strftime("%d/%m/%Y")
                
                print(f"🌐 {nome_fuso}")
                print(f"   ⌚ Hora: {hora_formatada}")
                print(f"   📅 Data: {data_formatada}")
                print()
            
            print("=" * 60)
            print("Pressione Ctrl+C para sair | Atualizando a cada 1 segundo...")
            print("=" * 60)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        limpar_tela()
        print("\n👋 Relógio encerrado!")

def main():
    """Função principal com menu de opções"""
    
    while True:
        limpar_tela()
        
        print("=" * 60)
        print(" " * 10 + "🕐 BEM-VINDO AO RELÓGIO MUNDIAL DIGITAL 🕐")
        print("=" * 60)
        print()
        print("1 - Exibir todos os fusos horários")
        print("2 - Escolher fusos horários personalizados")
        print("3 - Ver hora apenas do Brasil (São Paulo)")
        print("4 - Sair")
        print()
        print("=" * 60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_relogio()
        
        elif opcao == "2":
            limpar_tela()
            escolha, fusos_disponiveis = menu_personalizado()
            
            if escolha == "0":
                exibir_relogio()
            elif escolha in fusos_disponiveis:
                nome, codigo = fusos_disponiveis[escolha]
                fusos_personalizados = {nome: codigo}
                exibir_relogio_personalizado(fusos_personalizados)
            else:
                print("❌ Opção inválida!")
                time.sleep(2)
        
        elif opcao == "3":
            fusos_brasil = {"🇧🇷 BRT (São Paulo)": "America/Sao_Paulo"}
            exibir_relogio_personalizado(fusos_brasil)
        
        elif opcao == "4":
            limpar_tela()
            print("\n👋 Obrigado por usar o Relógio Mundial Digital!")
            print("Até logo! 🕐\n")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()
