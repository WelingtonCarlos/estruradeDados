from funcionario.funcionario import Funcionario


def main():

    funcionarios = [nome:Guilherme salario:3.45
                    nome:Moisés salario:2.49,
                    nome:Rafael salario:3.45,
                    nome:Raimundo salario:4.3,
                    nome:Welington salario:10.0,
                    nome:Carlos salario:8.5
                    nome:Andrey salario:3.45,
                    nome:Gabriel salario:4.3,
                    nome:Daniel salario:10.0,
                    nome:João salario:8.5]

    print(funcionarios)

    print(funcionarios_ordenados1=sorted(funcionarios,
          key=Funcionario.get_salario))
    print(funcionarios_ordenados2=sorted(
        funcionarios, key=Funcionario.get_nome))

    print(funcionarios_ordenados3=sorted(funcionarios,
          key=Funcionario.get_salario, reverse=True))
    print(funcionarios_ordenados4=sorted(
        funcionarios, key=Funcionario.get_nome, reverse=True))


main()
