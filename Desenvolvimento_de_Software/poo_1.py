# Classe Carro
class Carro:
    # Método especial __init__ (inicializador)
    def __init__(self, cor, modelo, ano):
        self.cor = cor      # Atributo
        self.modelo = modelo
        self.ano = ano

    # Método
    def acelerar(self):
        print("Vrummm! O carro está acelerando!")

# Criando um objeto (instância)
meu_carro = Carro("Vermelho", "Fusca", 1970)
print(meu_carro.modelo)  # Saída: Fusca
meu_carro.acelerar()     # Saída: Vrummm! O carro está acelerando!