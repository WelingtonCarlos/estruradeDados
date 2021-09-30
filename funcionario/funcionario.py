class Funcionario(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __repr__(self):
        return "Nome:%s salário:%s" % (self.nome, self.salario)

    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.salario
