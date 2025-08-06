condicao = True
bancoDeDados = {}
id = 1

while condicao:

    #menu de opções
    print(15*"-")
    print("Selecione uma opção:")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefa")
    print("3 - Sair")
    print("  ")

    opcao = input("Digite o número da opção desejada: ") 

    print(15*"-")

    if opcao == "1":
        tarefa = input("Digite sua tarefa: ")

        print(f"Sua tarefa é: {tarefa}")

        #Confirma se a tarefa foi adicionada
        if tarefa != "":
            print("Tarefa adicionada com sucesso!")

            bancoDeDados[id] = tarefa
            id += 1
        else:
            print("Você não digitou nenhuma tarefa. Tente novamente.")
    
    if opcao == "2":

        if id > 0:
            print(f"Você tem {id} tarefa(s) cadastrada(s).")

            apresentarTarefas = 1
            tarefa = 1

            while apresentarTarefas <= id:
                print(f"Tarefa {apresentarTarefas}: {bancoDeDados[tarefa]}")
                tarefa = tarefa + 1
                apresentarTarefas += 1

        else:
            print("Você não tem tarefas cadastradas.")
    
    if opcao == "3":
        condicao = False
        print("Saindo...")
