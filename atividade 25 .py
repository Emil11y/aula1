def gerenciamento_alunos():
 
    lista_alunos = []  

    while True:
        nomes = input("Digite o nome dos alunos para cadastrar (separados por espaço) ou 'fim' para encerrar: ").split()
        if 'fim' in nomes:
            nomes.remove('fim') 
            break
        lista_alunos.extend(nomes) 
    print("\nAlunos cadastrados:")
    if lista_alunos:
        for aluno in lista_alunos:
            print(f"- {aluno}")
    else:
        print("Nenhum aluno cadastrado.")
        return 

    while True:
        remover = input("\nDeseja remover algum aluno? (sim/não): ").lower()
        if remover == 'sim':
            nome_remover = input("Digite o nome do aluno que deseja remover: ")
            if nome_remover in lista_alunos:
                lista_alunos.remove(nome_remover)
                print(f"Aluno '{nome_remover}' removido.")
                print("\nLista de alunos atualizada:")
                for aluno in lista_alunos:
                    print(f"- {aluno}")
            else:
                print(f"O aluno '{nome_remover}' não está na lista.")
        elif remover == 'não':
            print("\nLista final de alunos:")
            for aluno in lista_alunos:
                print(f"- {aluno}")
            break
        else:
            print("Opção inválida. Digite 'sim' ou 'não'.")

gerenciamento_alunos()

