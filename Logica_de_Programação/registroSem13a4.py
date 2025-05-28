def processar_pagamento():
    # Passo 1: Obter o valor total da compra
    valor_total = float(input("Digite o valor total da compra: R$ "))
    
    # Passo 2: Mostrar opções de pagamento
    print("\nMétodos de pagamento disponíveis:")
    print("1 - Cartão de crédito/débito")
    print("2 - Dinheiro")
    
    # Passo 3: Capturar escolha do cliente
    opcao = input("Escolha o método de pagamento (1 ou 2): ")
    
    # Passo 4: Processar conforme a opção
    if opcao == "1":
        # Pagamento com cartão
        print("\nProcessando pagamento via cartão...")
        numero_cartao = input("Digite o número do cartão: ")
        validade = input("Digite a validade (MM/AA): ")
        cvv = input("Digite o CVV: ")
        
        # Aqui normalmente integraria com uma API de pagamento
        print(f"Pagamento de R$ {valor_total:.2f} processado com sucesso no cartão!")
        
    elif opcao == "2":
        # Pagamento em dinheiro
        print("\nPagamento em dinheiro selecionado")
        valor_recebido = float(input("Digite o valor recebido em dinheiro: R$ "))
        
        if valor_recebido >= valor_total:
            troco = valor_recebido - valor_total
            print(f"Pagamento recebido. Troco: R$ {troco:.2f}")
        else:
            print("Valor insuficiente. Favor completar o pagamento.")
            
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Executar o fluxo
processar_pagamento()