#fiz esse arquivo para armazenar os comandos que usei em vários arquivos para facilitar e simplificar os códigos e não ficar repetindo

#Bibliotecas
import os 
import getch

#Imprime uma mensagem na tela e pede para o usuario pressionar qualquer tecla para continuar
def pressioneParaContinuar():
    print("\nPressione qualquer tecla para continuar...")
    getch.getch()

#limpar o terminal do linux
def limpaTela():
    os.system('clear')