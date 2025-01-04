# ProjetoOO MERCADO
Projeto de atividade livre da matéria de Orientação a Objetos 2024/2 ministrado pelo professor Henrique Gomes.

Nome: João Guilherme

Matrícula: 232027476

## :warning: Importante :warning:
Este é meu primeiro projeto em python aplicando os conceitos da programação e orientação a objetos,
portanto o código não ficou tão refinado nem totalmente simplificado.

Deixei os arquivos separados para deixar mais modularizado e organizado, mais informações adiante.

---

# Sumário
1. [Problema a ser resolvido](#problema-a-ser-resolvido)
2. [Resumo Funcionalidades](#resumo-funcionalidades)
3. [Instalação](#instalação)
4. [Classes utilizadas](#classes-utilizadas)
5. [Arquivos](#arquivos)


## Problema a ser resolvido
O problema escolhido foi o gerenciamento de um supermercado tradicional, onde era necessário ter um controle sobre o estoque e preço de diversos produtos.
Considerando que esse supermercado era composto por uma equipe de vários funcionarios, foi necessário criar um sistema de login para poder registrar
quem foi que cadastrou um produto especifico, além de ser necessário um cadastro especial de adminstrador para gerenciar comandos com permissões mais 
restritas.

---
 
## Resumo Funcionalidades
O projeto consiste em um sistema de gerenciamento de um supermercado, capaz de armazenar as seguintes informações sobre um produto:

- Nome;
- Preço;
- Quantidade em estoque;
- Descrição;
- Usuário que registrou o produto.

Junto ao sistema principal de gerenciamento de um mercado, o projeto contém um sistema de login, que permite identificar as modificações feitas no sistema
sejam monitoradas, colaborando para o melhor funcionamento do sistema quando aliado a uma equipe de funcionários.

---

## Instalação
Esse projeto foi testado utilizando o sistema operacional Linux Mint 21.3 com o kernel 6.8.0-50-generic

Para inciarmos a instalação primeiramente atualizaremos os pacotes do sistema com o respectivo comando:
```
sudo apt update -y && sudo apt upgrade -y
```
Agora iremos clonar o repositório para o sistema local:
```
git clone https://github.com/jonas3688/ProjetoOO
```
Agora que já temos o repositório na maquina, iremos acessar o mesmo com o seguinte comando:
```
cd ProjetoOO/
```
Após isso instalamos o python caso ele não esteja instalado no sistema:
```
sudo apt install -y python3
```
Após instalado o python no sistema, iremos instalar pip (gerenciador de pacotes do python) no sistema:
```
sudo apt install -y python3-pip
```
Diante disso, iremos baixar as bibliotecas utilizadas no programa usando o pip, com o seguinte comando:
```
pip install -r requirements.txt
```
Dentro do repósitorio já tem um scrip que irá executar o programa, apenas precisamos torná-lo executavel, que pode ser feito com o comadno:
```
chmod +x iniciarApp.sh
```
O programa já está pronto para uso! Podemos exercutar ele utilizando o comando:
```
./iniciarApp.sh
```
---

## Classes utilizadas
### Produto
Atributos:
```
Nome
Preço
Quantidade em estoque 
Descrição
Usuario registrador
```
A classe produto e seus métodos estão presentes no arquivo mercado.py localizado na pasta arquivosPy.

### Usuario
```
Nome de Usuario
Senha
Permissão
```
A classe Usuario e seus métodos estão presentes no arquivo telainicial.py na pasta arquivosPy.

---

## Arquivos
Segue um breve resumo do conteúdo presente nos arquivos do projeto.
Para informações mais detalhadas do funcionamento dos métodos verifique os comentários no próprio codigo

### iniciarApp.sh
Script responsável por iniciar o programa no sistema operacional linux, simplismente executa o arquivo start.py dentro da pasta arquivosPy usando o python3.

---

### ArquivosPy/start.py
Responsável por unir os dois sistemas principais.
O arquivo direciona o usuário para o login, presente no arquivo telainical.py e espera o retorno do arquivo, que dependendo ou encerra o programa inteiro ou redireciona o 
usuário para o sistema presente no mercado.py.

---

### ArquivosPy/comandos.py
Arquivo feito para organização e simplificação dos outros dois arquivos principais. 
Os métodos presentes nesse arquivo foram muito utilizados no projeto inteiro, portanto fiz esse arquivo para deixar
os demais arquivos mais simplificados

#### Métodos:
##### pressioneParaContinuar()
>Imprime uma mensagem na tela do usuario e aguarda ele apertar qualquer tecla para continuar a execução do programa.

##### limpaTela()
>Usa a biblioteca os para limpar o terminal do linux .

---

### ArquivosPy/telainicial.py
Arquivo onde a classe Usuario está presente, junto a ela está presente o sistema de login e cadastro que foi utilizado no projeto.

#### Classe:
Atributos:
```
usuario (Nome de usuário que é utilizado no login)
senha (senha que será utilizada para fazer o login)
permissao (permissão do usuario, 1 representa administrador e 0 representa usuario comum)
```
##### Métodos de classe:
###### verificaSenha()
>confere se a senha armazenada no objeto é igual a senha que foi utilizada para fazer o login.

#### Métodos:
##### telaLogado(objetoUsuario)
>Redireciona o usuario para a tela pós login dependendo de sua permissão.

##### telaLogadoAdmin(nomeUsuario)
>Mostra o menu de pós-login do usuário com permissão de administrador e as opções de escolha do mesmo.

##### telaLogadoFuncionario(nomeUsuario)
>Mostra o menu de pós-login do usuário com permissão comum e as opções de esoclha do mesmo.

##### menu()
>Mostra o menu pré-login ao usuário, é por onde começa a execução do arquivo, solicitado pelo arquivo start.py

##### opcoesMenu()
>Mostra ao usuario as opções de escolha na tela pré-login

##### criaArquivo()
>Cria o arquivo usuarios.bin, onde o objeto será serializado

##### carregarLogins()
>Carrega para a memoria os logins que estão presentes no arquivo

##### salvarLogins(usuarios)
>Salva no arquivo os objetos presentes na memoria

##### login()
>Faz o login no sistema verificando a senha que o usuario forneceu de entrada com a senha salva no arquivo

##### editaLogins()
>Edita os atributos do objeto registrado no sistema

##### cadastroDeUsuarios()
>Responsável por registrar usuários no sistema de login

---

### ArquivosPy/mercado.py
Arquivo onde está presente a classe Produto, junto a ela está o sistema de cadastro e monitoramento de produtos do supermercado.

#### Classe:
Atributos:
```
nome (Nome do produto)
quantidade (Quantidade em estoque do produto)
preco (Preço do produto)
usuarioRegistrador (Nome de usuário que cadastrou o produto no sistema)
descricao (Descrição do produto)
```

#### Métodos:
##### criaArquivo()
>Cria o arquivo estoque.bin, que será utilizado para salvar os dados dos produtos

##### carregarDadosArquivo()
>Carrega os dados presentes no arquivo para a memoria

##### salvarProdutosArquivo(produtos)
>Salva os dados presentes na memoria para o arquivo

##### menu(nomeUsuario,permissaoUsuario)
>Esse método que inicia a execução do aplicativo, sendo chamado pelo arquivo start.py
>Redireciona o usuário para seu menu do aplicativo dependendo de sua permissão

##### menuAdmin(nomeUsuario)
>Menu principal com as escolhas do usuário com permissão de administrador

##### menuFuncionario(nomeUsuario)
>Menu principal com as escolhas do usuário comum

##### cadastraProduto(nomeUsuario)
>Cadastra os produtos no sistema

##### listaProdutos()
>Lista todos os produtos cadastrados no sistema

##### editarProdutos()
>Permite a edição de produtos cadastrados no sistema

##### escolhaInvalida()
>Mostra ao usuario uma mensagem de escolha invalida

##### apresentaOpcoesAdmin(nomeUsuario)
>Imprime na tela as opções que podem ser utilizadas no menu do usuario adminstrador

##### apresentaOpcoesFuncionario(nomeUsuario)
>Imprime na tela as opções que podem ser utilizadas no menu do usuario comum

