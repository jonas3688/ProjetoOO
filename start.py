#Arquivo principal do programa, usado para unir os outros sistemas presentes nos outros arquivos

#bibliotecas 
import telainicial
import mercado 

#iniciando o aplicativo

#Armazena na memoria o nome de usuario e sua permissao, caso o login seja bem sucedido
nomeUsuario,permissaoUsuario = telainicial.menu()
if not nomeUsuario == '0': #Caso o login não tenha falhado inicia o sistema do mercado
        mercado.menu(nomeUsuario,permissaoUsuario) #Chama o menu do mercado
        