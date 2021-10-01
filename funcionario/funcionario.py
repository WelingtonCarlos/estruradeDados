class Funcionario(object):

    def _init_(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self, nome):
        return self.nome

    def get_salario(self, salario):
        return self.salario
