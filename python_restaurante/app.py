import os

restaurantes = [{'nome' : 'pizza boa', 'categoria' : 'pizzaria', 'ativo' : False}, 
                {'nome' : 'pão fresco', 'categoria' : 'padaria', 'ativo' : True}, 
                {'nome' : 'churraco show', 'categoria' : 'carne', 'ativo' : False}]

def exibir_nome_programa():
    '''Exibe o nome do programa na tela'''
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    ''')

def exibir_opcoes():
    '''Exibe as opções disponiveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status restaurante')
    print('4. Sair')

def finalizar_app():
    '''Exibe mensagem de encerramento do app'''

    exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar para o menu principal
    
    Outputs:
    - Retorna ao menu'''

    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    '''Exibe o subtitulo na tela
    
    Inputs:
    - texto: str - O texto do subtítulo'''

    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print('*', texto, '*')
    print(linha)
    print()

def opcao_invalida():
    '''Exibe mensagem de opção invalida e retorna ao menu
    
    Outputs:
    - Retorna ao menu'''

    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes'''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def lista_restaurante():
    '''Essa função é responsável por listar os restaurantes cadastrados
    
    Outputs:
    - Exibe a lista de restaurantes na tela'''

    exibir_subtitulo('Listando os restaurantes')

    print('Nome do restaurante'.ljust(22), '|', 'Categoria'.ljust(20), '|', 'Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} -')

    voltar_ao_menu_principal()

def alternar_status_restaurante():
    '''Essa função é responsável por alterar o status do restaurante
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação'''

    exibir_subtitulo('Alterando o status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escoher(): 
    ''' Solicita e executa a opção escolhida
    
    Outputs:
    - Executa a opção escolhida pelo usuário'''

    try:
        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            lista_restaurante()
        elif escolha == 3:
            alternar_status_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escoher()

if __name__ == '__main__':
    main()