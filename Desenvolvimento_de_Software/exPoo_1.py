class Lampada:
    def __init__(self):
        self.estado = False  # Começa desligada
# Uso da classe
lampada = Lampada()
print(lampada.alterar_estado())  # Liga a lâmpada
print(lampada.alterar_estado())  # Desliga a lâmpada
