from colorama import Fore, Style

# 1) Lista com as mensagens
mensagens = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)",
]

# 2) Função que define a cor de acordo com o nível 
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE

# 3) Função que mostra a situação do reservatório com a cor certa
def exibir_situacao(nivel):
    cor = definir_cor(nivel)
    mensagem = mensagens[nivel - 1]
    print(cor + mensagem)

# 4) Simulação: o reservatório passando por todos os níveis
print("Monitoramento do reservatório\n")
for nivel in range(1, 6):
    exibir_situacao(nivel)

# 5) Restaura o estilo padrão do terminal
print(Style.RESET_ALL)