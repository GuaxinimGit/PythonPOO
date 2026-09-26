# Declaração de Classe
class Aluno:
    """
    Essa classe cria um Aluno, que é uma pessoa com nome e idade.

    Para criar uma nova pessoa, use
    variável = Aluno("nome", idade) 
    """
    def __init__(self, n = "Sem nome", i = 0): # Método Construtor
        # Atributos de Instância
        self.nome = n # é o parâmetro do método construtor
        self.idade = i # self.idade é o atributo

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Aluno(a) e tem {self.idade} anos."

    
# Declaração de Objetos
a1 = Aluno("Francisco", 60)
a1.aniversario()
print(a1.mensagem())

a2 = Aluno("Pedrinho", 20)
a2.aniversario()
print(a2.mensagem())

a3 = Aluno() # quando não passado nenhum parâmetro, ele executa o que foi definido no método construtor
print(a3.mensagem()) 
