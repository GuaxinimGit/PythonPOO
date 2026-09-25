# Declaração de Classe
class Aluno:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Aluno(a) e tem {self.idade} anos."

    
# Declaração de Objetos
a1 = Aluno()
a1.nome = "Francisco"
a1.idade = 60
a1.aniversario()
print(a1.mensagem())
