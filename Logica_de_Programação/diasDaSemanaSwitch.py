def switch_dia_semana(numero):
    dias = {
        1: "Domingo - Dia de descanso!",
        2: "Segunda-feira - Começo da semana!",
        3: "Terça-feira - Bora trabalhar!",
        4: "Quarta-feira - Já é meio da semana!",
        5: "Quinta-feira - Quase sexta!",
        6: "Sexta-feira - Último dia útil!",
        7: "Sábado - Dia de relaxar!"
    }
    return dias.get(numero, "Número inválido! Escolha de 1 a 7.")

# Solicita entrada do usuário
try:
    escolha = int(input("Digite um número de 1 a 7 para escolher o dia da semana: "))
    mensagem = switch_dia_semana(escolha)
    print(mensagem)
except ValueError:
    print("Por favor, digite um número válido!")