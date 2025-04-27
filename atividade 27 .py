p1=float(input("Digite a 1° nota: "))
p2=float(input("digite 2° nota: "))
media= (p1+p2)/2
if p1>p2:
    print(f'sua maior nota foi {p1}, e a média das notas é {media}')
else:
    print(f'sua maior nota foi {p2}, e a média das notas é {media}')