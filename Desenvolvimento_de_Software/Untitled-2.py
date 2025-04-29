#Aula de Programação Orientada a Objetos (POO) em Python
#Objetivo da aula:
#Introduzir os conceitos básicos da Programação Orientada a Objetos (POO) #usando Python, com exemplos simples e práticos.

#1. O que é POO?
#POO é um paradigma de programação que organiza o código em objetos, que #contêm:

#Atributos (dados, características)

#Métodos (ações, comportamentos)

#Vantagens:
#✅ Reutilização de código (evita repetição)
#✅ Organização melhorada (código mais legível)
#✅ Facilidade de manutenção (alterações pontuais)

#2. Pilares da POO em Python
#2.1. Classes e Objetos
#Classe: Molde que define atributos e métodos.

#Objeto: Instância (realização concreta) de uma classe.

#Exemplo:

#python
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

#Exemplo:

#python
# Classe Pai
class Animal:
    def comer(self):
        print("O animal está comendo.")

# Classe Filha
class Cachorro(Animal):  # Herda de Animal
    def latir(self):
        print("Au au!")

# Uso
rex = Cachorro()
rex.comer()  # Método herdado (Saída: O animal está comendo.)
rex.latir()  # Método próprio (Saída: Au au!)
#2.4. Polimorfismo
#Métodos com o mesmo nome podem ter comportamentos diferentes.

#Exemplo:

#python
class Animal:
    def emitir_som(self):
        print("Som genérico")

class Gato(Animal):
    def emitir_som(self):  # Sobrescreve o método
        print("Miau!")

class Vaca(Animal):
    def emitir_som(self):  # Sobrescreve o método
        print("Moo!")

# Uso
animais = [Gato(), Vaca()]
for animal in animais:
    animal.emitir_som()
# Saída:
# Miau!
# Moo!
#3. Resumo dos Pilares
#Pilar	Conceito	Exemplo Python
#Classe/Objeto	Molde e instância	carro = Carro("Azul", "Civic", 2020)
#Encapsulamento	Proteção de dados	self.__saldo + métodos get_saldo()
#Herança	Reutilização de código	class Cachorro(Animal):
#Polimorfismo	Mesmo método, ações diferentes	def emitir_som() em Gato e Vaca
#4. Atividade Prática (para a turma)
#Crie uma classe Pessoa com:

#Atributos: nome, idade

#Método: fazer_aniversario() (aumenta a idade em 1)

#Depois, crie Aluno (herda de Pessoa) com:

#Atributo extra: matricula

#Método extra: estudar() (imprime "Estudando...")

#Solução sugerida:

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

#Dúvidas? Bora codar! 🚀🐍

#obrigado
#De nada! Fico feliz em ajudar. 😊

#Se precisar de mais exemplos, exercícios ou explicações sobre POO em Python (ou qualquer outro tópico de programação), é só chamar!

#Boa aula e sucesso com seus alunos! 🚀🐍

#Dica extra: Que tal sugerir um projeto simples para a turma?

#Sistema de Biblioteca: Classes Livro, Autor, Usuário com empréstimos e devoluções.

#python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

# Desafiem os alunos a completar o código!