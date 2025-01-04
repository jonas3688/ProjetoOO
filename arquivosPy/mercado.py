#Arquivo que possui o sistema de produtos de um mercado sendo o principal sistema do aplicativo todo 

#bibliotecas
import comandos
import pickle
import os

#classe do produto
class Produto:
    def __init__(self, nome, quantidade, preco,descricao,usuarioRegistrador):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.usuarioRegistrador = usuarioRegistrador
        self.descricao = descricao

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade em estoque: {self.quantidade} | Registrado por: {self.usuarioRegistrador}\nDescrição: {self.descricao}\n"

#Cria o arquivo que será utilizado para armazenar os dados dos produtos (sem criptografia)
def criaArquivo():
    with open("estoque.bin",'a') as arquivo:
        pass

#Carrega os dados presentes no arquivo para a memoria, retorna {} caso o arquivo não existe ou esteja vazio
def carregarDadosArquivo():
    if os.path.exists('estoque.bin') and os.path.getsize('estoque.bin') > 0: #verifica se o arquivo existe e não esta vazio 
        with open('estoque.bin', 'rb') as arquivo:
            return pickle.load(arquivo)
    return {}

#Salva os produtos que estao na memória para o arquivo 
def salvaProdutosArquivo(produtos):
    with open("estoque.bin",'wb') as arquivo:
        pickle.dump(produtos,arquivo)

#A função menu irá redirecionar o usuario para a sua tela principal dependendo da sua permissao
def menu(nomeUsuario,permissaoUsuario):

    criaArquivo()
    if permissaoUsuario == 1:
        menuAdmin(nomeUsuario) #Envia o usuario para a tela do administrador
    else:
        menuFuncionario(nomeUsuario) #Envia o usuario para a tela de usuario comum
    
#Tela principal do usuario adminstrador                     
def menuAdmin(nomeUsuario):
    while True:
        try:
            #apresenta as opções de escolha do usuario
            apresentaOpcoesAdmin(nomeUsuario)
            
            #entrada do usuario
            escolhaMenu = int(input("Digite a opção desejada: "))
            match escolhaMenu:

                #cadastrar produto
                case 1:
                    cadastraProduto(nomeUsuario)
                    
                #listar produtos 
                case 2:
                    listaProdutos()
                    
                #Editar produtos
                case 3:
                    if not listaProdutos() == 0: #Caso o arquivo não esteja vazio redireciona o usuario a edição
                        editarProdutos()
                        
                #Apagará os dados presentes no arquivo estoque.bin 
                case 4:
                    comandos.limpaTela()
                    
                    #Solicita a confirmação do usuario para deletar os dados 
                    if int(input("Isso irá deletar todos os dados salvos, deseja prosseguir?\n1.Sim\n0.Não\n")) == 1:
                        with open("estoque.bin",'w') as arquivo:
                            pass
                        comandos.limpaTela()
                        print("Dados apagados com sucesso!")
                        comandos.pressioneParaContinuar()  
                    else:
                        print("Operação cancelada!")     
                        comandos.pressioneParaContinuar()   
                        
                #Encerra o programa dando break no loop
                case 5:
                    print("Fechando o aplicativo!")
                    comandos.pressioneParaContinuar()
                    break
                
#Tratamento de entradas invalidas do usuarios
                case _:
                    comandos.limpaTela()
                    escolhaInvalida()
        except ValueError:
            comandos.limpaTela()
            escolhaInvalida()
            continue

#Menu principal de usuarios com permissão comuns 
def menuFuncionario(nomeUsuario):
    
    while True:
        try:
            #apresenta menu de escolha dos funcionarios 
            apresentaOpcoesFuncionario(nomeUsuario)
            #entrada do usuario
            escolhaMenu = int(input("Digite a opção desejada: "))
            match escolhaMenu:

                #cadastrar produto
                case 1:
                    cadastraProduto(nomeUsuario)
                #listar produtos 
                
                case 2:
                    listaProdutos()
                #Editar produtos
                
                case 3:
                    if not listaProdutos() == 0: #Caso o arquivo não esteja vazio redireciona o usuario para edicao de daods
                        editarProdutos()
                        
                #Encerra o programa dando break no loop
                case 4:
                    print("Fechando o aplicativo!")
                    comandos.pressioneParaContinuar()
                    break
                
#Tratamento de entradas invalidas do usuario
                case _:
                    comandos.limpaTela()
                    escolhaInvalida()
        except ValueError:
            comandos.limpaTela()
            escolhaInvalida()
            continue


#Função responsavel por cadastrar produtos no sistema
def cadastraProduto(nomeUsuario):

    comandos.limpaTela()
    #Carrega os produtos presentes no arquivo para a memoria
    produtosArquivo = carregarDadosArquivo()
    
    #Entrada do usuario 
    nome = input("Digite o nome do produto: ")
    
    #Verifica se existe um produto com mesmo nome já registrado
    if nome in produtosArquivo: 
        comandos.limpaTela()
        print("Produto com mesmo nome já registrado!")
        comandos.pressioneParaContinuar()
        return {}
    
    while True:
        try:
            comandos.limpaTela()
            #Entrda do usuario
            preco = float(input("Digite o Preço do produto: "))
            #Valida o preço digitado pelo usuario
            if not preco > 0:
                print("Preço inválido, tente novamente.")
                comandos.pressioneParaContinuar()
                continue    
            break
        #Tratamento de entrada invalida do usuario
        except ValueError:
            print("Preço inválido, tente novamente.")
            comandos.pressioneParaContinuar()
            continue
    
    while True:
        try:
            comandos.limpaTela()
            #entrada do usuario 
            quantidade = int(input("Digite a quantidade: "))
            #valida a quantidade digitada pelo usuario
            if not quantidade > 0:
                print("Quantidade inválida, tente novamente.")
                comandos.pressioneParaContinuar()
                continue
            break         
        #Tratamento de entrda invalida do usuario
        except ValueError:
            print("Quantidade inválida, tente novamente.")
            comandos.pressioneParaContinuar()
            continue

    #Entrda do usuario
    descricao = input("Digite a descrição do produto: ")

    #Salva o cadastro da memoria para o arquivo
    produto = Produto(nome,quantidade,preco,descricao,nomeUsuario)
    produtosArquivo[nome] = produto
    salvaProdutosArquivo(produtosArquivo)

    #Confirma para o usuario que o cadastro foi bem sucedido
    print("Produto cadastrado com sucesso!")
    comandos.pressioneParaContinuar
    return

#Função responsavel por listar os produtos presentes no arquivo 
def listaProdutos():

    comandos.limpaTela()
    #Carrega os produtos presentes no arquivo para a memoria 
    produtos = carregarDadosArquivo()
    
    #Verifica se o arquivo está vazio 
    if produtos == {}:
        print("Nenhum produto cadastrado!")
        comandos.pressioneParaContinuar()
        return 0 #Retorno da função caso o arquivo esteja vazio
    else:
        #Imprime os produtos presentes no arquivo
        for nome, produto in produtos.items():
            print(produto)  
    comandos.pressioneParaContinuar()

#Função responsavel por editar os dados de produtos presentes nos arquivos
def editarProdutos():
    
    #carrega os produtos do arquivo para a memoria 
    produtosArquivo = carregarDadosArquivo()

    #Entrada do usuario
    nome = input("Digite o nome do produto que deseja editar: ")
    
    #Verifica se existe algum produto com o mesmo nome da entrada do usuario
    if nome in produtosArquivo:
        
        #Armazena o produto selecionado na variavel produto
        produto = produtosArquivo[nome]

        # Opções de edição
        print("\nO que você deseja editar?")
        print("1. Nome")
        print("2. Preço")
        print("3. Quantidade")
        print("4. Descrição")
        print("5. Cancelar")
        
        #Menu de escolha do que será editado 
        escolhaEditar = int(input("\nQual opção deseja editar: \n"))
        match escolhaEditar:
            
            case 1: #Usuario escolheu editar o nome 
                
                #Entrda do usuario
                novoNome = input("Digite o novo nome do produto: \n")
                
                #Verifica se existe outro produto com o mesmo nome 
                if novoNome in produtosArquivo:
                    print("Já existe um produto com esse nome!")
                    comandos.pressioneParaContinuar()
                    return
                else:
                    #salva o produto após a edição na memoria e apaga o antigo
                    produto.nome = novoNome
                    produtosArquivo[novoNome] = produto
                    del produtosArquivo[nome]
                    
            case 2: #Usuario escolheu editar o preço
                while True:
                    try:
                        #Entrada do usuario
                        novoPreco = float(input("Digite o novo preço do produto: \n"))
                        #Validação do preço digitado pelo usuario
                        if not novoPreco > 0:
                            print("Preço inválido, tente novamente.")
                            comandos.pressioneParaContinuar()
                            continue
                        break
                    #tratamento de entradas invalida do usuario
                    except ValueError:
                        print("Preço inválido, tente novamente.")
                        comandos.pressioneParaContinuar()
                        continue
                #Substitui o preço antigo pelo novo 
                produto.preco = novoPreco
                
            case 3: #Usuario escolheu editar a quantidade 
                while True:
                    try:
                        #Entrada do usuario
                        novaQuantidade = int(input("Digite a nova quantidade em estoque do protudo: \n"))
                        #Validação da nova quantidade digitada pelo usuario 
                        if not novaQuantidade > 0:
                            print("Quantidade inválida,tente novamente.")
                            comandos.pressioneParaContinuar()
                            continue
                        break
                    #Tratamento de entradas invalidas pelo usuario
                    except ValueError:
                        print("Quantidade inválida, tente novamente.")
                        comandos.pressioneParaContinuar()
                        continue
                #substitui a quantidade antiga pela nova 
                produto.quantidade = novaQuantidade
                
            case 4: #usuario esoclheu editar a descrição do produto
                #Entrada do usuario 
                novaDescricao = input("Digite a nova descrição do produto: \n")
                #Substitui a descricao antiga pela nova 
                produto.descricao = novaDescricao
                
            case 5: #Usuario escolheu cancelar a edição do produto             
                comandos.pressioneParaContinuar()
                return
            
            case _: #Usuario fez uma escolha invalida 
                escolhaInvalida()
                return
        
        #Armazena as edições que foram feitas para o arquivo
        salvaProdutosArquivo(produtosArquivo)
        print("\nEdição bem sucedida!")
        comandos.pressioneParaContinuar()
        
    #Caso não exista um produto com o mesmo nome fornecido na entrada do usuario
    else:
        print("\nProduto não encontrado!")
        comandos.pressioneParaContinuar()

    
#apresenta a mensagem de escolha invalida e aguarda o usuario apertar alguma tecla 
def escolhaInvalida():
    print("\nEscolha inválida!")
    comandos.pressioneParaContinuar()
        
#apresentando as opcoes de escolha do menu ao usuario adminstrador
def apresentaOpcoesAdmin(nomeUsuario):
    
    comandos.limpaTela()
    print(f"Logado como: {nomeUsuario}")
    print("\n1.Cadastrar produto")
    print("2.Listar produtos")
    print("3.Editar produtos")
    print("4.Apagar dados")
    print("5.Sair\n")
    
#apresentando as opcoes de escolha do menu ao usuario comum
def apresentaOpcoesFuncionario(nomeUsuario):
    comandos.limpaTela()
    print(f"Logado como: {nomeUsuario}")
    print("\n1.Cadastrar produto")
    print("2.Listar produtos")
    print("3.Editar produtos")
    print("4.Sair\n")
