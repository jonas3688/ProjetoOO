# ProjetoOO
Projeto de atividade livre da matéria de Orientação a Objetos 2024/2

## Resumo Funcionalidades
O projeto consiste em um sistema de gerenciamento de um supermercado, capaz de armazenar:

- Nome
- Preço
- Quantidade em estoque
- Descrição
- Usuário que registrou o produto

Junto ao sistema principal de gerenciamento de um mercado, o projeto contém um sistema de login, que permite identificar as modificações feitas no sistema
sejam monitoradas, colaborando para o melhor funcionamento do sistema quando aliado a uma equipe de funcionários

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
