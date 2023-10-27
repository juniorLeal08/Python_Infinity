# Modulo_Cadastro_de_Alunos

alunos = {}

def adicionar_aluno(matricula,nome):
    if matricula not in alunos:
        alunos[matricula] = nome
        print(f"Aluno Com Matricula{matricula} Adicionado Com Sucesso. ")
    else:
        print(f"Aluno Com Matricula{matricula} Já Existe. ")

def remover_aluno(matricula):
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno Com Matricula{matricula} Removido Com Sucesso. ")
    else:
        print(f"Aluno Com Matricula{matricula} Não Encontrado. ")

def atualizar_aluno(matricula,novo_nome):
    if matricula in alunos:
        alunos[matricula] = novo_nome
        print(f"Nome Do Aluno Com Matricula{matricula} Atualizado Com Sucesso. ")
    else:
        print(f"Aluno Com Matricula{matricula} Não Encontrado. ")

def lista_alunos():
    if not alunos:
        print("Nenhum Aluno Cadastrado. ")
    else:
        print("Lista De Alunos: ")
        for matricula, nome in alunos.items():
            print(f"Matricula: {matricula}, Nome: {nome}")


if __name__ == "__main__":
    while True:
        print("\nOpções: ")
        print("1.Adicionar Aluno ")
        print("2.Remover Aluno ")
        print("3.Atualizar Aluno ")
        print("4.Ver Lista De Alunos Cadastrado ")
        print("5.Sair ")
        opcao = input("Escolha Uma Opção: (1/2/3/4/5): ")

        if opcao == "1":
            matricula = int(input("Digite A Matricula Do Aluno: "))
            nome = str(input("Digite O Nome Do Aluno: "))
            adicionar_aluno(matricula,nome)
        elif opcao == "2":
            matricula = int(input("Digite A Matricula Do Aluno A Ser Removido: "))
            remover_aluno(matricula)
        elif opcao == "3":
            matricula = int(input("Digite A Matricula Do Aluno A Ser Atualizada: "))
            novo_nome = str(input("Digite O Novo Nome Do Aluno: "))
            atualizar_aluno(matricula,novo_nome)
        elif opcao == "4":
            lista_alunos()
        elif opcao == "5":
            break
        else:
            print("Opção Invalida Tente Novamente. ")















