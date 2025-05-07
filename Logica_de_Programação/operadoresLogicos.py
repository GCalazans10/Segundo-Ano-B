# Operadores Lógicos básicos
print("=== OPERADORES LÓGICOS EM PYTHON ===")
print("AND (E): Retorna True se ambas as condições forem verdadeiras")
print("OR (OU): Retorna True se pelo menos uma condição for verdadeira")
print("NOT (NÃO): Inverte o valor lógico (True vira False e vice-versa)")

# Exemplo 1: Verificação de acesso
print("\n--- Exemplo 1: Verificação de Acesso ---")
usuario_correto = True
senha_correta = False

if usuario_correto and senha_correta:
    print("Acesso concedido! (AND)")
else:
    print("Acesso negado! (AND)")

if usuario_correto or senha_correta:
    print("Pelo menos uma credencial está correta (OR)")
else:
    print("Nenhuma credencial está correta (OR)")

# Exemplo 2: Verificação de faixa etária
print("\n--- Exemplo 2: Faixa Etária ---")
idade = int(input("Digite sua idade: "))

if idade >= 12 and idade <= 17:
    print("Você é um adolescente!")
elif idade >= 18 and idade <= 65:
    print("Você é um adulto!")
elif idade > 65 and idade <= 120:
    print("Você é um idoso!")
else:
    print("Idade fora das faixas consideradas!")

# Exemplo 3: Uso do NOT
print("\n--- Exemplo 3: Operador NOT ---")
tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower() == 's'

if not tem_carteira:
    print("Você NÃO pode dirigir!")
else:
    print("Você pode dirigir!")

# Exemplo 4: Combinação de operadores
print("\n--- Exemplo 4: Combinação de Operadores ---")
nota = float(input("Digite sua nota (0-10): "))
frequencia = float(input("Digite sua frequência (0-100): "))

if nota >= 7 and frequencia >= 75 or nota >= 9 and frequencia >= 50:
    print("Aprovado!")
else:
    print("Reprovado.")

# Tabela Verdade dos Operadores
print("\n=== TABELA VERDADE ===")
print("A\tB\tA AND B\tA OR B\tNOT A")
print(f"True\tTrue\t{True and True}\t{True or True}\t{not True}")
print(f"True\tFalse\t{True and False}\t{True or False}\t{not True}")
print(f"False\tTrue\t{False and True}\t{False or True}\t{not False}")
print(f"False\tFalse\t{False and False}\t{False or False}\t{not False}")
