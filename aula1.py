# 1. crie um programa que leia dois números e mostre a soma entre eles
x=10
y=5
print(x+y)

#2 faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
x=input("insira algo: ")
print(type(x))

# 3. faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
x=int(input("insira um numero: "))
s = x + 1
a = x - 1
txt=f"o {x} tem como antecessor {a} e sucessor {s}"
print(txt)

# 5. desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
media = nota1 + nota2
media = media / 2
print(f'A média é {media}')

# 6. faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada(lembrando que não aprendemos laço nessa linguagem ainda)
n = int(input("Digite o número para ver a tabuada: "))
print(f'1 X {n} = {1*n}')
print(f'2 X {n} = {2*n}')
print(f'3 X {n} = {3*n}')
print(f'4 X {n} = {4*n}')
print(f'5 X {n} = {5*n}')
print(f'6 X {n} = {6*n}')
print(f'7 X {n} = {7*n}')
print(f'8 X {n} = {8*n}')
print(f'9 X {n} = {9*n}')
print(f'10 X {n} = {10*n}')

# 7. faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input("Digite o valor do produto: "))
produto = produto * 0.95
print(f'O valor final é {produto}')
