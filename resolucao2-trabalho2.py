'''
Faça um algoritmo que implemente o menu abaixo.

MENU
1- Cadastrar Login e Senha
2- Aumento de 10%
3- Relatório
4- Cadastrar Funcionário
Escolha:

Para implementar seu código você deverá utilizar
as seguintes listas:
login = []
senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


Descrição:
Na opção 1 - Você deverá cadastrar login e senha nas listas correspondentes.
             Critério: login não poderá se repetir. Verificar se nome consta
             na lista de funcionarios.

Para executar as opções 2 e 3, você deverá validar seu login e senha

Na opção 2 - Após validar login e senha, seu código deverá aumentar
             o salário dos funcionários em 10%. Mas somente
             se o funcionário ganhar abaixo da média em relação
             a lista de salarios.

Na opção 3 - Após confirmar login e senha, você deverá fazer um
             relatório mostrando o nome e o salario, conforme exemplo:

                 Maria Clara  - 7450.23
                 João Antonio - 5677.33
                 Carlos       - 3970.34
                 Pedro        - 3470.00
                 Ana          - 2200.00

Na opção 4 - Você deverá cadastrar o nome e o salário de um
             novo funcionário.

'''

lista_login = []
lista_senha = []
funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]


while True:
    escolha = input(
    '''
    
    MENU
    1- Cadastrar Login e Senha
    2- Aumento de 10%
    3- Relatório
    4- Cadastrar Funcionário
    Escolha: '''
    )

    if escolha == '1':
        nome = input("Nome: ")
        if nome in funcionarios:
            novo_login = input("Login: ")
            if novo_login not in lista_login:
                nova_senha = input("Senha: ")
                lista_login.append(novo_login)
                lista_senha.append(nova_senha)
        
    if escolha == '2':
        log = input("Login: ")
        sen = input("Senha: ")
        # Validar login e senha
        for indice , login in enumerate(lista_login):
            if login == log and lista_senha[indice] == sen:
                # Calcular media
                media = sum(salarios) / len(salarios)
                # Atualizar salários menores que a média
                for ind, salario in enumerate(salarios):
                    if salario < media:
                        salarios[ind] = salarios[ind] * 1.1
                                    # *= 1.1 (maneira curta de escrever)                

        """for indice in range(len(lista_login)):
            if log == lista_login[indice] and sen == lista_senha[indice]:
            FAZ A MESMA COISA QUE O FOR DE CIMA + ENUMERATE + IF
            """
        
    if escolha == '3':
        log = input("Login: ")
        sen = input("Senha: ")
        # Validar login e senha
        for indice , login in enumerate(lista_login):
            if login == log and lista_senha[indice] == sen:
                for ind, fun in enumerate(funcionarios):
                    print(f"Funcionário: {fun.ljust(20,'.')} - R$ {salarios[ind]}")
                            # {fun.ljust()} Justificar a esquerda (numero de caracteres, caracter)
                            
    
    if escolha == '4':
        novo_nome = input("Novo Funcionário: ")
        novo_salario = float(input("Salário: "))
        funcionarios.append(novo_nome)
        salarios.append(novo_salario)



        
            
