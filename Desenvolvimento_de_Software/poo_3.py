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