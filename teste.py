class Aluno:
    def __init__(self, matrícula, nome, sexo, idade):
        self.matrícula = matrícula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

if __name__ == "__main__":
    aluno1 = Aluno("0009038","Elisa", "feminino", "16") 
    aluno2 = Aluno("0004079","Maria", "feminino","17")
    print(aluno1.matrícula, aluno1.nome, aluno1.sexo, aluno1.idade)
    print(aluno2.matrícula, aluno2.nome, aluno2.sexo, aluno2.idade)