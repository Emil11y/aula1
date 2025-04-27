compras = []  

while True:
    escolha = str(input('Adicione um item na lista: '))
    compras.append(escolha)
    
    escolha2 = str(input('Deseja adicionar outros itens? Sim ou Não: '))
    if escolha2.lower() == 'não':  
        break

print(f'Os itens da lista de compras são: {compras}')
