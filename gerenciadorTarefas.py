condicao = True
bancoDeDados = []
id = 0

def adicionarTarefa():
    if tarefa != "":
        print(f"Sua tarefa é: {tarefa}")

        bancoDeDados.append(tarefa)
    else:
        print("Escreva uma tarefa valida!")

def listarTarefas():
    for x in bancoDeDados:
        print(x)
    
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
     
     #if responsavel por adicionar tarefas
    if opcao == "1":
        tarefa = input("Digite sua tarefa: ")
        adicionarTarefa()

    #if responsavel por mostrar as tarefas na tela
    if opcao == "2":
        listarTarefas()
    
    #if responsavel em finalizar 
    if opcao == "3":
        condicao = False
        print("Saindo...")
        ...