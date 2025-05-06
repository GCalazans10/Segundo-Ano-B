# Função para calcular o IMC
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: IMC = peso / (altura^2)
    
    Parâmetros:
        peso (float): peso em quilogramas
        altura (float): altura em metros
    
    Retorna:
        float: valor do IMC calculado
    """
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    """
    Classifica o IMC de acordo com os padrões da OMS
    
    Parâmetros:
        imc (float): valor do IMC a ser classificado
    
    Retorna:
        str: classificação do IMC
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III (mórbida)"

# Função principal
def main():
    # Exibe o cabeçalho do programa
    print("====================================")
    print("      CALCULADORA DE IMC            ")
    print("====================================")
    print()
    
    try:
        # Solicita os dados do usuário
        peso = float(input("Digite seu peso em kg (ex: 68.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
        
        # Verifica se os valores são positivos
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos!")
            return
        
        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        
        # Classifica o IMC
        classificacao = classificar_imc(imc)
        
        # Exibe os resultados
        print("\n============ RESULTADO ============")
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("===================================")
        
        # Tabela de referência
        print("\nTABELA DE REFERÊNCIA IMC (OMS):")
        print("Abaixo de 18.5: Abaixo do peso")
        print("18.5 - 24.9: Peso normal")
        print("25.0 - 29.9: Sobrepeso")
        print("30.0 - 34.9: Obesidade Grau I")
        print("35.0 - 39.9: Obesidade Grau II")
        print("Acima de 40: Obesidade Grau III (mórbida)")
        
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos!")

# Verifica se o programa está sendo executado diretamente
if __name__ == "__main__":
    main()
