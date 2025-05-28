# Conceitos Básicos de Diagrama de Classes em Python

# 1. Classe Básica com Atributos e Métodos
class Pessoa:
    # Atributos da classe
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo público
        self._idade = idade  # Atributo protegido (convenção)
        self.__cpf = None  # Atributo privado (name mangling)
    
    # Métodos públicos
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self._idade} anos.")
    
    def definir_cpf(self, cpf):
        if len(cpf) == 11:
            self.__cpf = cpf
        else:
            print("CPF inválido!")
    
    # Método privado
    def __validar_dados(self):
        return self.nome and self._idade > 0 and self.__cpf


# 2. Herança
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.disciplinas = []  # Associação com Disciplina
    
    def matricular(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f"{self.nome} matriculado em {disciplina.nome}")


# 3. Associação (uso de outra classe)
class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = None  # Agregação com Professor
    
    def designar_professor(self, professor):
        self.professor = professor
        print(f"Professor {professor.nome} designado para {self.nome}")


# 4. Agregação (relação todo-parte onde a parte pode existir sem o todo)
class Professor(Pessoa):
    def __init__(self, nome, idade, departamento):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.disciplinas_ministradas = []  # Agregação com Disciplina
    
    def ministrar(self, disciplina):
        self.disciplinas_ministradas.append(disciplina)
        disciplina.designar_professor(self)


# 5. Composição (relação todo-parte onde a parte não existe sem o todo)
class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self._departamentos = []  # Composição com Departamento
    
    def criar_departamento(self, nome):
        novo_departamento = Departamento(nome, self)
        self._departamentos.append(novo_departamento)
        return novo_departamento
    
    def listar_departamentos(self):
        return [d.nome for d in self._departamentos]


class Departamento:
    def __init__(self, nome, universidade):
        self.nome = nome
        self.universidade = universidade  # Link de volta para o todo


# Exemplo de uso
if __name__ == "__main__":
    # Criando instâncias
    uni = Universidade("Universidade Federal de Python")
    
    # Composição: Departamento não existe sem Universidade
    dep_comp = uni.criar_departamento("Ciência da Computação")
    
    # Agregação: Professor pode existir sem Disciplina e vice-versa
    prof = Professor("Prof. Gilberto", 45, dep_comp)
    
    disc1 = Disciplina("Programação OO", 60)
    disc2 = Disciplina("Estruturas de Dados", 60)
    
    prof.ministrar(disc1)
    prof.ministrar(disc2)
    
    # Associação: Aluno está associado a Disciplinas
    aluno = Aluno("João", 18, "20230001")
    aluno.matricular(disc1)
    
    # Chamando métodos
    aluno.apresentar()
    print(f"Departamentos na {uni.nome}: {uni.listar_departamentos()}")
    print(f"Disciplinas ministradas por {prof.nome}: {[d.nome for d in prof.disciplinas_ministradas]}")
