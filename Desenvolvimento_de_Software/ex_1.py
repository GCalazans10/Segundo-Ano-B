class Celular:  
    def __init__(self, modelo):  
        self.modelo = modelo  
        self.carga = 100  

    def tirar_foto(self):  
        if self.carga > 0:  
            print("Foto tirada!")  
            self.carga -= 10  
        else:  
            print("Sem bateria!")  

# Usando a classe  
meu_celular = Celular("Galaxy")  
meu_celular.tirar_foto()  # Saída: "Foto tirada!"