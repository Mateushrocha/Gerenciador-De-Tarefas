import json 

condicao = True
bd = []
bdTarefasConcluida = []
nome_arquivo = "bancoDeDados.json"
nome_arquivo_bd2 = "bancoDeDadosTarefasConcluidas.json"

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        bd = json.load(arquivo)
except:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(bd, arquivo, indent=4)

try:
    with open(nome_arquivo_bd2, "r", encoding="utf-8") as arquivo:
        bdTarefasConcluida = json.load(arquivo)
except:
    with open(nome_arquivo_bd2, "w", encoding="utf-8") as arquivo:
        json.dump(bdTarefasConcluida, arquivo, indent=4)

def atualizarBd():
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(bd, arquivo, indent=4)

def atualizarBdConluido():
    with open(nome_arquivo_bd2, "w", encoding="utf-8") as arquivo:
        json.dump(bdTarefasConcluida, arquivo, indent=4)

def adicionarTarefa():
    if tarefa != "":
        if tarefa in bd:
            print("Essa tarefa ja foi adicionada anteriormente! Digite um valor valido.")
            return

        print(f"Sua tarefa é: {tarefa}")

        bd.append(tarefa)
        atualizarBd()
    else:
        print("Escreva uma tarefa valida!")

def listarTarefas():
    for x in bd:
        print(x)
    
    verificacao = True
    while verificacao:
        print("Terminou alguma tarefa?")
        print("1 - Sim")
        print("2 - Não")
        concluiu = input("Digite aqui:")

        if concluiu == "1":
            for y, x in enumerate(bd):
                print(f"id {y + 1} - {x}")
            try:
                tarefaConcluidaId = int(input("Digite o id da tarefa concluida")) - 1
            except:
                print("Digite um id valido!")
                continue

            if tarefaConcluidaId > len(bd):
                print("Digite um id valido!")
                continue
            if tarefaConcluidaId <= len(bd):
                bdTarefasConcluida.append(bd[tarefaConcluidaId])
                del bd[tarefaConcluidaId]
                atualizarBdConluido()
        elif concluiu == "2":
            verificacao = False
        else:
            print("Digite uma opção valida!")
            continue

def listarTarefasConcluida():
    for x in bdTarefasConcluida:
        print(x)
    print("1 - Deseja retorna alguma tarefa para as não concluidas?")
    print("2 - Deseja adicionar novamente uma tarefa que ja foi adicionada anteriormente?")
    print("3 - Voltar")
    escolha = input("Digite sua escolha:")

    while condicao:
        if escolha == "1":
            retornaTarefa()
            condicao == False
        elif escolha == "2":
            adicionarTarefaNovamente()
        elif escolha == "3":
            break
        else:
            print("Escolha uma opção valida!")

def retornaTarefa():
    print( 10* "__")
    print("escolha a tarefa pelo o id: ")
    for y, x in enumerate(bdTarefasConcluida):
        print(f" id {y + 1} - {x}")
    escolha = input("Digite aqui o id: ")
    print(15* "__")
    try:
        escolha = int(escolha)
        escolha -= 1 
        """Esse "1" foi adicionado anteriormnte e agora esta sendo retirado afim de ficar 
        visualmente  mais atrativo ao usuario e o id começar em 1 ao inves de 0 """
        if escolha <= len(bdTarefasConcluida):
            bd.append(bdTarefasConcluida[escolha])
            del bdTarefasConcluida[escolha]
            return
    except:
        print("Digite uma opção valida")
        return
    
def adicionarTarefaNovamente(): 
    print("Qual tarefa você quer adicionar novamente?")
    for y, x in enumerate(bdTarefasConcluida):
        print(f" id {y + 1} - {x}")
    escolha = input("Digite aqui o id: ")
    print(15* "__")
    try:
        escolha = int(escolha)
        bd.append(bdTarefasConcluida[escolha])
    except:
        print("Digite um valor valido")

def excluirTarefa():
    print("Escolha a tarefa que deseja excluir: ")
    
    for i, x in enumerate(bd):
        print(f"id {i}: {x}")
    
    tarefaExcluir = int(input("Digite o id da tarefa: "))  
    
    if 0 <= tarefaExcluir < len(bd):
        del bd[tarefaExcluir]
        print("Tarefa excluída com sucesso!")
    else:
        print("ID inválido!")

def editarTarefa():
    verificao = True
    while verificao:
        print("Selecione a tarefa que deseja alterar:")
        for i, x in enumerate(bd):
            print(f"{i} - {x}")
    
        tarefaEditar = input("Qual tarefa deseja editar: ")
        try:
            tarefaEditar = int(tarefaEditar)
        except:
            print("DIGITE O ID DA TAREFA A SER EDITADA")
            continue

        newTarefa = input("Digite a nova tarefa: ")
        if newTarefa in bd:
            print("Digite uma tarefa que nao foi adicionada!")
            continue
        else:
            bd[tarefaEditar] = newTarefa
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
    elif opcao == "2":
        listarTarefas()
    
    #if responsavel em excluir tarefas 
    elif opcao == "3":
        excluirTarefa()

    #if responsael por editar tarefas 
    elif opcao == "4":
        editarTarefa()

    #if responsavel em listar as tarefas editadas
    elif opcao == "5":
        listarTarefasConcluida()

    #if responsavel em finalizar 
    elif opcao == "6":
        print("Tem certeza que quer sair mesmo?")
        print("S - sim | N - não")
        escolha = input()
        if escolha == "S" or escolha == "s":
            condicao = False
            print("Saindo...")
        elif escolha == "N" or "n":
            print("Que bom que decidiu ficar!")
        else:
            print("Digite um valor valido!")
    
    else:
        ("Digite uma opção valida!")

