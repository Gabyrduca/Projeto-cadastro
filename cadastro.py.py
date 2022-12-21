
#Cadastro de pacientes 


pacientes = []
endereco  = []


def cadastro():
    
    while True:
        print('[Forneça as informações do paciente!]')

        dados = {} #Dicionário que será passado com todos os dados para a lista 'pacientes'
        dados['nomeComp'] = (input('Nome: '))
        dados['senha'] = (input('Senha: '))

        #1 - Endereço de e-mail
        dados['email'] = input('E-mail: ')
        lista = {i['email']: i for i in pacientes} #Variavel usada com indice e laço 'for': verifica repetições por meio de chaves.
        while dados['email'] in lista: #Caso o dado já esteja em uso, o programa solicita um dado diferente.
            dados['email'] = input('[E-mail em uso, tente novamente!] E-mail: ')

        #2 - Login do paciente
        dados['login'] = input('Login: ')
        lista = {i['login']: i for i in pacientes}
        while dados['login'] in lista:
            dados['login'] = input('[Login em uso, tente novamente!] Login: ')

        #3 - Telefone do usuário:
        dados['telefone'] = int(input('Telefone: '))
        lista = {i['telefone']: i for i in pacientes}
        while dados['telefone'] in lista: 
             dados['telefone'] = int(input('[Telefone em uso, tente novamente!] Telefone: '))

        pacientes.append(dados) #Metodo append irá adicionar os dados na lista 

        print('[OK! Cadastro concluído.]')
        opcao = input('Dseja cadastrar mais alguém? (S/N): ').strip().lower()
        if(opcao == 'n'):  #Caso o administrador não queira novos usuários o laço 'while true' se encerra
            menu()
            break

def cadEndereco():
    while True:

        print('[Forneça um login de usuário!]')
        lista = {i['login']: i for i in pacientes}
        pesq = input('Login: ')

        if pesq in lista:
            print('[Forneça o endereço do paciente: ]')
            destino = {}
            destino['id'] = pesq
            destino['estado'] = input('Estado: ')
            destino['cidade'] = input('Cidade: ')
            destino['rua'] = input('Rua e Número: ')
            destino['cep'] = input('CEP: ')
            endereco.append(destino) #Será aramazenado em outra lista 

        else:
            print('')
            print('[Usuário não encontrado]')
            print('')

        opcao = input('Deseja cadastrar outro endereço? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarDados():

    while True:
        print('[Forneça o LOGIN para consultar os dados de um usuário!]')

        lista = {i['login']: i for i in pacientes}
        lista2 = {i['id']: i for i in pacientes}

        pesq = input('Login: ')

        if pesq in lista and pesq not in lista2:

            print(f'Dados do paciente [{pesq.upper()}]: {lista[pesq]}') 

            print('')
            print('[Endereço não  cadastrado!]')
            print('')

        elif pesq in lista and pesq in lista2:

            print('')
            print(f'Ddos do paciente [{pesq.upper()}]:')
            print('')
            print(f'Endereço do paciente [{pesq.upper()}]:')
            print('')
            resultado = list(filter(lambda item: item['id'] == pesq, endereco))
            for i in resultado:
                print(i)
            print('')

        else:
            print('')
            print('[Usuário não encontrado!]')
            print('')

        opcao = input('Deseja consultar outro paciente? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarPacientes(): 

    while True:
        print('')
        print('[Usuários cadastrados: ]')
        print('')

        for i in pacientes: #Variavel 'i' passa na lista 'pacientes' buscando apenas as informações com indice 'login' e 'nomeComp' logo ap´s retornando o output dos daoss 

            print('Nome:', i['nomeCamp'], 'Login:', i['login'])

        print('')

        opcao = input('Dseja conferir novamente? (S/N): ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def menu():
    

    print('*************************************')
    print('*************************************')
    print('Bem Vindo ao Hospital Paulista\n')
    print('Sistemas de Cadastro de Pacientes\n')
    print('*************************************')
    print('*************************************')
    print('[1] Cadastrar paciente')
    print('[2] Cadastrar endereço do paciente')
    print('[3] Cnsultar paciente')
    print('[4] Consultar banco de dados')
    print('[0] Sair')
    print('*************************************')
    print('*************************************')

menu()

while True:

    x = int(input('Escolha > [1] [2] [3] [4] [0]: '))
    
    while x > 4 or x < 0:
        x = int(input('[Erro, tente novamente!] Escolha uma opção: ')) #Caso os números não estejam prontos no menu, o programa irá repeto-lo

    if x == 1:
        cadastro()
    elif x == 2:
        cadEndereco()
    elif x == 3:
        mostrarDados()
    elif x == 4:
        mostrarPacientes()
    else:
        print('')
        print('[Programa encerrado!]')
        print('')
        break








