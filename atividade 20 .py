quantidade_pares = 0
quantidade_impares = 0

for numero in range(10):  
    numero = int(input('Insira um número inteiro: '))
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print(f'Foram digitados {quantidade_pares} números pares e {quantidade_impares} números ímpares.')