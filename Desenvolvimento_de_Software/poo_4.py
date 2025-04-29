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