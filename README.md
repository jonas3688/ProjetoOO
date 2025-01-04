# ProjetoOO
Projeto de atividade livre da matéria de Orientação a Objetos 2024/2 ministrado pelo professor Henrique Gomes.
Nome: João Guilherme
Matrícula: 232027476

---

## :warning: Importante :warning:
Este é meu primeiro projeto em python aplicando os conceitos da programação e orientação a objetos,
portanto o código não ficou tão refinado nem totalmente simplificado.

Deixei os arquivos separados para deixar mais modularizado e organizado, mais informações adiante.

---

## Problema a ser resolvido
O problema escolhido foi o gerenciamento de um supermercado tradicional, onde era necessário ter um controle sobre o estoque e preço de diversos produtos.
Considerando que esse supermercado era composto por uma equipe de vários funcionarios, foi necessário criar um sistema de login para poder registrar
quem foi que cadastrou um produto especifico, além de ser necessário um cadastro especial de adminstrador para gerenciar comandos com permissões mais 
restritas.

---
 
## Resumo Funcionalidades
O projeto consiste em um sistema de gerenciamento de um supermercado, capaz de armazenar:

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
O programa já está pronto para uso! Podemos exercutar ele utilizando o comando 
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
A classe produto e seus métodos estão presentes no arquivo mercado.py localizado na pasta arquivosPy

### Usuario
```
Nome de Usuario
Senha
Permissão
```
A classe Usuario e seus métodos estão presentes no arquivo telainicial.py na pasta arquivosPy

## Arquivos

### iniciarApp.sh

### ArquivosPy/start.py

### ArquivosPy/comandos.py

### ArquivosPy/telainicial.py

### ArquivosPy/mercado.py


