#python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # Chama o __init__ da classe pai
        self.matricula = matricula

    def estudar(self):
        print(f"{self.nome} está estudando...")

# Uso
aluno1 = Aluno("João", 20, "20240001")
aluno1.fazer_aniversario()
print(aluno1.idade)  # Saída: 21
aluno1.estudar()     # Saída: João está estudando...
#5. Conclusão
#POO em Python é poderosa e intuitiva.

#Use classes, objetos, encapsulamento, herança e polimorfismo para criar código organizado.

#Pratiquem com exemplos do dia a dia (carros, animais, contas bancárias, etc.).