from funcionario.funcionario import Funcionario


def main():

    [nome:chocolate salario:3.45,
     nome:biscoito salario:2.49,
     nome:cafe salario:3.45,
     nome:suco salario:4.3,
     nome:feijao salario:10.0,
     nome:arroz salario:8.5
     nome:cafe salario:3.45,
     nome:suco salario:4.3,
     nome:feijao salario:10.0,
     nome:arroz salario:8.5]

    print(funcionarios)

    print(funcionarios_ordenados1=sorted(funcionarios,
          key=Funcionario.get_salario, reverse=True))
    print(funcionarios_ordenados2=sorted(
        funcionarios, key=Funcionario.get_nome, reverse=True))

    print(funcionarios_ordenados3=sorted(funcionarios,
          key=Funcionario.get_salario, reverse=True))
    print(funcionarios_ordenados4=sorted(
        funcionarios, key=Funcionario.get_nome, reverse=True))


main()
