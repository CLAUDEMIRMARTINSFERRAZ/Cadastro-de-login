'''O sistema de login deve peritir que novos usuários seja cadastrados, e que os usuário existentes possam fazer login. O sistema deve alertar caso a senha e login não estejam corretos'''
# * O sistema não deve permitir que usuários duplicados sejam cadastrados.
# * O sistema deve alertar caso a senha e o login não estejam corretos.


'''
1. Quais são os dados de entrada necessaria?
    - usuario, senha

2. O que devo fazer com esses dados?
    -Eu devo registrar o usuario e senha que foi digitado

3. Quais são as restrtições desse problemas? 
    -Não devo peritir cadastro de usuários ja existentes.

4. Qual é o resultado esperado?
    - Um novo usuário e senha cadastrados

5. Qual é a segêscia de passos necessario para chegar no resultado final?
    - Receber o usuário
    - receber a senha
    - verificar se o usuário já existe
    - caso não existe, cadastrar aquele usuário e senha.
'''
resposta = input('[1] - Cadastrar novo usuario:  [2] Fazer login: ')

#Armazenando os usuários existentes
usuarios= ['Debora','Amanda','Igor', 'Gustavo']
senhas = ['123456','abcdef','123abc','654321']
#if condicao == condicao

    # *O sistema de login deve permitir que novos usuários sejam cadastrados.
if resposta == '1':
        #Receber um usuário
    usuario_digitado = input('Digite seu usuário: ')
    if usuario_digitado in usuarios:
        print('Usuario existente!')
    else:
        #Recebendo uma senha.
        senha_digitada = input('Digite sua senha: ')
        # caso não existe, cadastrar aquele usuário e senha.
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)
elif resposta == '2':
    # *Permitir que usuários existentes possam fazer login.
    # Pedir o usuário.
    usuario_digitado =input('Digite o seu usuario: ')
    # Pedir a  senha,
    senha_digitada = input('Digite a sua senha: ')
    # verficar se usuario existe na lista

    # preciso verficar se a senha digitada pelo usuário é aquela mesma que esta na nossa lista de senhas.
    encontrado = False
    for indice,item in enumerate(usuarios):
        if usuario_digitado == item and senha_digitada == senhas[indice]:
            print('Login realizado com Sucesso.')
            encontrado= True
        elif encontrado == False:
            print('Usuario ou senha incorreto!')
else:
    print('Digite 1 ou 2')