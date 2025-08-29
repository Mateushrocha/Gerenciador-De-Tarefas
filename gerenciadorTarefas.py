condicao = True
bancoDeDados = []

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

    
while condicao:

    #menu de opções
    print(15*"-")
    print("Selecione uma opção:")
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefa")
    print("3 - Excluir tarefa")
    print("4 - Sair")
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

    #if responsavel em finalizar 
    if opcao == "4":
        condicao = False
        print("Saindo...")