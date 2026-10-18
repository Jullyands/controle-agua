# Controle de Níveis de Água

from colorama import Fore, Style

mensagens = [
Fore.RED + "Muito baixo (crítico)",
Fore.YELLOW + "Baixo",
Fore.GREEN + "Médio",
Fore.CYAN + "Alto",
Fore.BLUE + "Muito alto (alerta)"
]

def obter_mensagem(nivel):
    return mensagens [nivel - 1 ]

valor_definido = 1 # Valor que pode ser alterado

resposta = obter_mensagem(valor_definido)

print(resposta)

print(Style.RESET_ALL)