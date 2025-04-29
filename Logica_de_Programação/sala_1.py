while True:
    print("\n--- MENU ---")
    print("1. Cadastrar")
    print("2. Consultar")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("Cadastrando usuário...")
    elif opcao == "2":
        print("Consultando dados...")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")