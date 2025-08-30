condicao = True
bancoDeDados = ["estudar", "trabalhar", "caminhar"] 
#banco de dados a principio deveria ficar vazio, porem afim de teste deixe ele com valores ficticio
bancoDeDadosTarefasConcluidas = ["tarefa 1", "tarefa 2", "tarefa 3", "tarefa 4"]

def adicionarTarefa():
    if tarefa != "":
        if tarefa in bancoDeDados:
            print("Essa tarefa ja foi adicionada anteriormente! Digite um valor valido.")
            return

        print(f"Sua tarefa é: {tarefa}")

        bancoDeDados.append(tarefa)
    else:
        print("Escreva uma tarefa valida!")

def listarTarefas():
    for x in bancoDeDados:
        print(x)
    
    verificacao = True
    while verificacao:
        print("Terminou alguma tarefa?")
        print("1 - Sim")
        print("2 - Não")
        concluiu = input("Digite aqui:")

        if concluiu == "1":
            for y, x in enumerate(bancoDeDados):
                print(f"id {y + 1} - {x}")
            try:
                tarefaConcluidaId = int(input("Digite o id da tarefa concluida")) - 1
            except:
                print("Digite um id valido!")
                continue

            if tarefaConcluidaId > len(bancoDeDados):
                print("Digite um id valido!")
                continue
            if tarefaConcluidaId <= len(bancoDeDados):
                bancoDeDadosTarefasConcluidas.append(bancoDeDados[tarefaConcluidaId])
                del bancoDeDados[tarefaConcluidaId]
        if concluiu == "2":
            verificacao = False
        else:
            print("Digite uma opção valida!")
            continue

def listarTarefasConcluida():
    for x in bancoDeDadosTarefasConcluidas:
        print(x)
    print("1 - Deseja retorna alguma tarefa para as não concluidas?")
    print("2 - Deseja adicionar novamente uma tarefa que ja foi adicionada anteriormente?")
    print("3 - Voltar")
    escolha = input("Digite sua escolha:")

    while condicao:
        if escolha == "1":
            retornaTarefa()
            condicao == False
        if escolha == "2":
            ...
        if escolha == "3":
            break
        else:
            ...

def retornaTarefa():
    print( 10* "__")
    print("escolha a tarefa pelo o id: ")
    for y, x in enumerate(bancoDeDadosTarefasConcluidas):
        print(f" id {y + 1} - {x}")
    escolha = input("Digite aqui o id: ")
    print(15* "__")
    try:
        escolha = int(escolha)
        escolha -= 1 
        """Esse "1" foi adicionado anteriormnte e agora esta sendo retirado afim de ficar 
        visualmente  mais atrativo ao usuario e o id começar em 1 ao inves de 0 """
        if escolha <= len(bancoDeDadosTarefasConcluidas):
            bancoDeDados.append(bancoDeDadosTarefasConcluidas[escolha])
            del bancoDeDadosTarefasConcluidas[escolha]
            return
    except:
        print("Digite uma opção valida")
        return
    
"""
Duas novas opções:
adicionar novamente a tarefa que ja foi concluida, caso ele conclua ela nova mente 
ter a opção de adicionar mais uma vez a tarefa concluida, para concluir mais uma vez 
"""

def excluirTarefa():
    print("Escolha a tarefa que deseja excluir: ")
    
    for i, x in enumerate(bancoDeDados):
        print(f"id {i}: {x}")
    
    tarefaExcluir = int(input("Digite o id da tarefa: "))  
    
    if 0 <= tarefaExcluir < len(bancoDeDados):
        del bancoDeDados[tarefaExcluir]
        print("Tarefa excluída com sucesso!")
    else:
        print("ID inválido!")

def editarTarefa():
    verificao = True
    while verificao:
        print("Selecione a tarefa que deseja alterar:")
        for i, x in enumerate(bancoDeDados):
            print(f"{i} - {x}")
    
        tarefaEditar = input("Qual tarefa deseja editar: ")
        try:
            tarefaEditar = int(tarefaEditar)
        except:
            print("DIGITE O ID DA TAREFA A SER EDITADA")
            continue

        newTarefa = input("Digite a nova tarefa: ")
        if newTarefa in bancoDeDados:
            print("Digite uma tarefa que nao foi adicionada!")
            continue
        else:
            bancoDeDados[tarefaEditar] = newTarefa
            verificao = False
    
while condicao:

    #menu de opções
    print(15*"-")
    print("Selecione uma opção:")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefa")
    print("3 - Excluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Listar tarefas concluidas")
    print("6 - Sair")
    print("  ")

    opcao = input("Digite o número da opção desejada: ") 
    print(15*"-")
     
     #if responsavel por adicionar tarefas
    if opcao == "1":
        tarefa = input("Digite sua tarefa: ")
        adicionarTarefa()

    #if responsavel por mostrar as tarefas na tela
    if opcao == "2":
        listarTarefas()
    
    #if responsavel em excluir tarefas 
    if opcao == "3":
        excluirTarefa()

    #if responsael por editar tarefas 
    if opcao == "4":
        editarTarefa()

    #if responsavel em listar as tarefas editadas
    if opcao == "5":
        listarTarefasConcluida()

    #if responsavel em finalizar 
    if opcao == "6":
        print("Tem certeza que quer sair mesmo?")
        escolha = input("S - sim | N - não")
        if escolha == "S" or escolha == "s":
            condicao = False
            print("Saindo...")
        if escolha == "N" or "n":
            print("Que bom que decidiu ficar!")
        else:
            print("Digite um valor valido!")
    
    else:
        ("Digite uma opção valida!")