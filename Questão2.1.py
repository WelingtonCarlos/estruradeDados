class Funcionario:

    def __init__(self, nome, salario):

        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def __repr__(self):
        return "Nome:%s salário:%s" % (self.nome, self.salario)


funcionarios = []

funcionarios.append(Funcionario("Guilherme", 3.45))
funcionarios.append(Funcionario("Moisés", 2.49))
funcionarios.append(Funcionario("Rogerio", 10.45))
funcionarios.append(Funcionario("Raimundo", 4.3))

print(funcionarios[1].getNome())
print(funcionarios[1].getSalario())
print(funcionarios[1].__repr__())

funcionarios_ordenados = sorted(funcionarios, key=Funcionario.getSalario)
funcionarios_ordenados_n = sorted(funcionarios, key=Funcionario.getNome)

print(funcionarios_ordenados_n)
