def dia_da_semana(numero):
    if numero == 1:
        return "Domingo - Dia de descanso!"
    elif numero == 2:
        return "Segunda-feira - Começo da semana!"
    elif numero == 3:
        return "Terça-feira - Bora trabalhar!"
    elif numero == 4:
        return "Quarta-feira - Já é meio da semana!"
    elif numero == 5:
        return "Quinta-feira - Quase sexta!"
    elif numero == 6:
        return "Sexta-feira - Último dia útil!"
    elif numero == 7:
        return "Sábado - Dia de relaxar!"
    else:
        return "Número inválido! Escolha de 1 a 7."

# Solicita entrada do usuário
try:
    escolha = int(input("Digite um número de 1 a 7 para escolher o dia da semana: "))
    mensagem = dia_da_semana(escolha)
    print(mensagem)
except ValueError:
    print("Por favor, digite um número válido!")