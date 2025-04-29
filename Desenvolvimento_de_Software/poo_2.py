#2.2. Encapsulamento
#Protege os dados internos, permitindo acesso controlado por métodos.

#Exemplo:

#python
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado (__)

    # Método público para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    # Método público para ver saldo
    def get_saldo(self):
        return self.__saldo

# Uso
minha_conta = ContaBancaria()
minha_conta.depositar(100)
print(minha_conta.get_saldo())  # Saída: 100
# minha_conta.__saldo  # Erro! Atributo privado.
#2.3. Herança
#Uma classe filha herda atributos e métodos da classe pai.