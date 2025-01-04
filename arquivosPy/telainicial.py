
#Bibliotecas
import os
import pickle
import comandos

#Este arquivo é responsavel pelo sistema de cadastros e logins de usuarios no sistema

#Classe que armazena o par usuario/senha 
class Usuario:
    def __init__(self,usuario,senha,permissao):
        self.usuario = usuario
        self.senha = senha
        self.permissao = permissao # (1) para administrador e (0) para usuario comum

    def verificaSenha(self,inputSenha,): #Retorna 1 caso as senhas sejam iguais e 0 caso as senhas sejam diferentes 
        if self.senha == inputSenha:
            return 1
        else:
            return 0 
        
#Direciona o programa para a tela pós login dependendo do nivel de permissao do usuario logado     
def telaLogado(objetoUsuario):

    comandos.limpaTela()
    if objetoUsuario.permissao == 1:
        return telaLogadoAdmin(objetoUsuario.usuario) #Se a permissão for de administrador enviar o user para a tela de admin 
    else:
        return telaLogadoFuncionario(objetoUsuario.usuario) #Envia o usuario para tela de usuario comum

#Tela pós login do usuario com permissao de administrador 
def telaLogadoAdmin(nomeUsuario):
    while True:
        
        comandos.limpaTela()
        print(f"Usuario: {nomeUsuario} \ Permissão: Administrador\n")
        
        #Escolhas do usuario
        print("1.Acessar sistema")
        print("2.Trocar usuário")
        print("3.Sair do programa")
        print("4.Editar cadastros")
        print("5.Apagar todos os cadastros\n")

        #Entrada do usuario
        escolha = int(input("Selecione a opção desejada: \n"))
        match escolha:

            case 1:
                return 1 # Acessa o sistema do mercado

            case 2:
                return 2 # Retorna pra tela inicial 

            case 3:
                return 3 # Encerra o programa 

            case 4:
                comandos.limpaTela()
                editaLogins() #Chama a função para editar dados dos logins 

            case 5:

                comandos.limpaTela()
                #Aguarda a confirmação do usuario
                if int(input("Isso irá deletar todos os dados salvos, deseja prosseguir?\n1.Sim\n0.Não\n")) == 1:
                    
                    #Apaga os dados do arquivo
                    with open("usuarios.bin",'w') as arquivo:
                        pass
                    
                    comandos.limpaTela()
                    print("Dados apagados com sucesso!")
                    comandos.pressioneParaContinuar()
                    return 2 
                else:
                    print("Operação cancelada!")     
                    comandos.pressioneParaContinuar()

            case _:
                print("Escolha inválida!")
                comandos.pressioneParaContinuar()

def telaLogadoFuncionario(nomeUsuario):
    while True:
        
        comandos.limpaTela()
        print(f"Usuario: {nomeUsuario} \ Permissão: Funcionário\n")
        
        #Escolhas do usuario
        print("1.Acessar sistema")
        print("2.Trocar usuário")
        print("3.Sair do programa\n")

        #entrada do usuario
        escolha = int(input("Selecione a opção desejada: \n"))

        match escolha:
            case 1:
                return 1 #Acessa o sistema do mercado 
            case 2:
                return 2 #retorna pra tela inicial
            case 3:
                return 3 #Encerra o programa 
            case _:
                print("Escolha inválida!")
                comandos.pressioneParaContinuar()

    
#Função principal do arquivo, é a tela incial do aplicativo e a que retorna o resultado final do sistema
def menu():

    while True:
        try:
            comandos.limpaTela()
            
            #Apresenta as opÇões de escolha do usuario
            opcoesMenu()

            #Entrada do usuario
            escolha = input("Selecione a opção desejada:")
            match escolha:
                case '1': #Usuario escolheu a opção de login 

                    comandos.limpaTela()
                    #Chama a função que será responsavel por fazer o login 
                    objetoUsuario = login()

                    #Se o objeto não está vazio, o sistema ira passar para a tela pós o login
                    if not objetoUsuario == {}:

                        match telaLogado(objetoUsuario):
                            case 1: #Usuario escolheu acessar o sistema, retorna o nome de usuario e sua permissao para o start.py
                                return (objetoUsuario.usuario,objetoUsuario.permissao)
                            case 2:
                                pass #usuario escolheu trocar de usuario, assim essa escolha retorna ao inicio do loop
                            case 3:
                                return ('0','0') #Usuario escolheu sair do aplicativo, retorna '0' e ´0' para o start.py


                case '2': #usuario escolheu a opção de cadastrar usuario
                    #chama a função que ira cadastrar usuarios no sistema 
                    cadastroDeUsuarios()

                case '0': #Usuario encerrou o aplicativo
                    print("Aplicativo encerrado com sucesso!")
                    return ('0','0')

#Tratamento de entradas invalidas 
                case _:
                    print("Escolha inválida!")
                    comandos.pressioneParaContinuar()
        except ValueError:
            print("Escolha inválida!")
            comandos.pressioneParaContinuar()        

#Imprime as opções do menu no terminal
def opcoesMenu():
    print("1. Login\n2. Cadastro\n0. Sair\n")

#Cria o arquivo que será utilizado para armazenar os logins (sem criptografia)
def criaArquivo():
    with open("usuarios.bin",'a') as arquivo:
        pass

#Carrega para a memória os logins presentes no arquivo(Retorna os logins ou retorna {} caso o arquivo esteja vazio)
def carregarLogins():
    if os.path.exists('usuarios.bin') and os.path.getsize('usuarios.bin') > 0: #Verifica se o arquivo existe e não está vazio
        with open('usuarios.bin', 'rb') as arquivo:
            return pickle.load(arquivo)
    return {}

#Salva os login da memória para o arquivo 
def salvarLogins(usuarios):
    with open("usuarios.bin",'wb') as arquivo:
        pickle.dump(usuarios,arquivo)
    
#Faz login verificando as entradas do usuario com as do arquivo
def login():
    
    #Carrega os objetos presentes no arquivo para a variavel usuarios
    usuarios = carregarLogins()
    
    usuarioLogin = input("Digite o seu nome de usuário: ")
    if not usuarioLogin in usuarios: #Caso a entrada do usuario nao seja encontrada no arquivo retorna {}
        print("Usuário não encontrado!")
        comandos.pressioneParaContinuar()
        return {}
    else:
        
        #Carrega na memoria o objeto especifico com o mesmo nome digitado pelo usuario
        objetoUsuario = usuarios[usuarioLogin]
        
        comandos.limpaTela( )
        senhaDigitada = input(f"Digite a senha do usuário {usuarioLogin}: ")
        
        #Caso a entrada de senha do usuario seja igual a armazenada no arquivo
        if objetoUsuario.verificaSenha(senhaDigitada) == 1:
            print("Login bem sucedido!")
            comandos.pressioneParaContinuar()
            return objetoUsuario #Retorna o nome de usuario 
        else:
            print("Senha inválida, tente novamente!")
            comandos.pressioneParaContinuar()
            return {}

def editaLogins():
    
    #Carrega os logins presentes no arquivo para a memoria 
    usuarios = carregarLogins()

    #Se o arquivo não está vavzio 
    if not usuarios == {}:

        #Entrada do usuario 
        nomeUsuario = input("Digite o nome de usuário que deseja editar: \n")
        if nomeUsuario in usuarios: #verifica se existe algum login com o mesmo nome da entrada do usuario
            
            #Carrega o objeto que vai ser modificado na memoria 
            usuarioModificando = usuarios[nomeUsuario]

            #Menu de escolhas do usuario
            print("\nO que você deseja editar?")
            print("1. Usuario")
            print("2. Senha")

            escolhaEdicao = int(input("\nQual opção deseja editar: "))
            match escolhaEdicao:
                case 1: #Usuario escolheu editar o nome de usuario 
                    
                    comandos.limpaTela()
                    novoUsuario = input("Digite o novo nome de usúario: ")
                    if novoUsuario in usuarios: #Verifica se existe algum usuario com esse mesmo nome
                        print("Já existe um usúario com esse mesmo nome!")
                        comandos.limpaTela()
                        return
                    else:
                        #Salva o novo nome de usuario na memoria e deleta o antigo
                        usuarioModificando.usuario = novoUsuario
                        usuarios[novoUsuario] = usuarioModificando
                        del usuarios[nomeUsuario]

                case 2: #usuario escolheu editar a senha do lgoin 
                    comandos.limpaTela()
                    #Entrada do usuario
                    novaSenha = input(f"Digite a nova senha para o usuário {usuarioModificando.usuario}:")
                    #Validação da senha 
                    while True:
                        if len(novaSenha) < 8:
                            novaSenha = input("Senha inválida, digite uma senha com pelomenos 8 caracteres: ")
                        else:
                            break

                    comandos.limpaTela()
                    #Entrada novamente do usuario
                    senhaConfirma = input("Confirme a senha: ")
                    
                    #Verifica se as senhas batem e dá ao usuario a opção de cancelar digitando "SAIR"
                    while True:
                        if senhaConfirma != novaSenha and senhaConfirma != "SAIR":
                            print("As senhas não conferem! Tente novamente ou digite SAIR para sair: ")
                            senhaConfirma = input()
                        else:
                           break
                    
                    #Verifica se o usuario quis cancelar a operaÇão       
                    if senhaConfirma == "SAIR":
                        print("Operação cancelada.")
                        return
                    else:
                        print("Senha confirmada com sucesso!")
                    comandos.pressioneParaContinuar
                    
                    #Define a nova senha no lugar da anterior                             
                    usuarioModificando.senha = novaSenha
                    
                #Caso o usuario digite alguma entrada invalida no menu 
                case _:
                    print("Escolha inválida!")
                    comandos.pressioneParaContinuar()
                    
            #Salva os objetos presentes na memoria para o arquivo
            salvarLogins(usuarios)
        
        #Caso o usuario tente editar um login que não existe  
        else:
            print(f"Usuário {nomeUsuario} não encontrado!")
            comandos.pressioneParaContinuar()
            
    #caso não tenha nenhum login presente no arquivo        
    else:
        print("Nenhum usuário cadastrado!")
        comandos.pressioneParaContinuar()
         


#Função responsavel por armazenar e validar as entradas de cadastros para a memoria 
def cadastroDeUsuarios():

    comandos.limpaTela()
    #Carrega os logins presentes no arquivo para a memoria 
    usuarios = carregarLogins()
    
    #Verifica se o é o primeiro cadastro do programa, sendo assim o programa ira definir o primeiro cadastro como administrador 
    if usuarios == {}:
        print("Foi identificado que esse é o primeiro cadastro do programa, o usuário a seguir terá permissões de administrador.\n")
        permissaoAdmin = 1
    else:
        permissaoAdmin = 0

    while True:
        #Entrada do usuario
        novoUsuario = input("Digite o nome de usuário que deseja cadastrar: ")
        
        #Validação da entrada de usuario 
        while len(novoUsuario) == 0 or len(novoUsuario) > 30:
           novoUsuario = input("Usuário inválido, Digite um usuário entre 1 a 30 caracteres: ")
           comandos.limpaTela()

        #Verifica se já existe um usuario com esse nome 
        if novoUsuario in usuarios:
            print("Usuário já cadastrado!")
        else:
            break

    comandos.limpaTela()
    #Entrada do usuario
    senha = input(f"Digite a senha para o usuário {novoUsuario}:")
    
    #Validação da senha 
    while True:
        if len(senha) < 8:
            senha = input("Senha inválida, digite uma senha com pelomenos 8 caracteres: ")
        else:
            break

    comandos.limpaTela()
    
    #Confirmação da senha
    senhaConfirma = input("Confirme a senha: ")
    while True:
        if senhaConfirma != senha  and senhaConfirma != "SAIR":
            print("As senhas não conferem! Tente novamente ou digite SAIR para sair: ")
            senhaConfirma = input()
        else:
            break
    
    #Verifica se o usuario cancelou a operação
    if senhaConfirma == "SAIR":
        print("Operação cancelada.")
        return
    else:
        print("Senha confirmada com sucesso!")
    comandos.pressioneParaContinuar()
    
    #Salva os cadastros presentes na memoria para o arquivo 
    objetoUsuario = Usuario(novoUsuario,senha,permissaoAdmin)
    usuarios[novoUsuario] = objetoUsuario
    salvarLogins(usuarios)

