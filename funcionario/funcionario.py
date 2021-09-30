class Funcionario(object):
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def __repr__(self):
        return "Nome:%s salário:%s" % (self.__nome, self.__salario)

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__salario
