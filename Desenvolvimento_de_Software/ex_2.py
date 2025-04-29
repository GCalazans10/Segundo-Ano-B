#Defina a “receita” dos seus objetos. Por exemplo, para um sistema de petshop:

class Animal:  
    def __init__(self, nome, especie):  
        self.nome = nome  
        self.especie = especie  

    def emitir_som(self):  
        print(f"{self.nome} faz algum som!")
#Instancie objetos e teste
#Crie objetos reais a partir das classes e interaja com eles:

gato = Animal("Meal", "Gato")  
gato.emitir_som()  # Saída: "Mimi faz algum som!" 