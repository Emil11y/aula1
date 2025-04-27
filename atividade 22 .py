verificacao = 0
senha = 'emily123'
usuario = 'emily'
for tentativa in range(3):
    usuario = str(input('Digite o usuário: '))
    senha = str(input('Digite a senha: '))
    if usuario == 'emily' and senha == 'emily123':
        verificacao = 1
        break
    else:
        print('Usuário ou senha errados, tente novamente')
if verificacao == 1:
    print('Acesso autorizado!')
else:
    print('Acesso negado!')