classe = []
alunos = ["bEmily", "Lary", "Bianca", "Gustavo", "vitor", "Ana"]

for aluno in alunos:
    resposta = input(f"{aluno} está presente ou faltou ? : ")
    if resposta == "presente":
        classe.append(aluno)

print(f"Total de alunos presentes: {classe}")

buscar = input("Deseja buscar o nome de um aluno? sim ou não: ")
if buscar == "sim":
    nome = input("Digite o nome do aluno: ")
    if nome in classe:
        print(f"{nome} estava presente.")
    else:
        print(f"{nome} faltou.")
else:
    print(f"os  alunos presentes são {classe}")
    