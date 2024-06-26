#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `PyCharm` no Linux Ubuntu
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `PyCharm` no Linux Ubuntu.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `PyCharm` on Linux Ubuntu._

# ## Revisão(ões)/Versão(ões)

# |Revisão número|Data da revisão|Descrição da revisão|Autor da revisão|
# |:-:|:-:|:-|:-|
# |0|21/11/2023|<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|

# ## Descrição [2]
# 
# ### `PyCharm`
# 
# O PyCharm é um ambiente de desenvolvimento integrado (IDE) altamente conceituado e amplamente utilizado para programação em Python. Desenvolvido pela JetBrains, o PyCharm oferece uma variedade de recursos poderosos e ferramentas de produtividade projetadas especificamente para facilitar o desenvolvimento de aplicativos Python. Ele inclui um editor de código com recursos avançados de autocompletar, realce de sintaxe e depuração, além de suporte a frameworks populares, como Django e Flask. O PyCharm também oferece integração com sistemas de controle de versão, gerenciamento de dependências e ambientes virtuais, simplificando o gerenciamento de projetos Python complexos. Sua interface de usuário intuitiva e personalizável, juntamente com sua extensa coleção de plug-ins e extensões, tornam-no uma escolha preferida para desenvolvedores Python em busca de produtividade e eficiência em seu fluxo de trabalho de programação.

# ## 1. Como configurar/instalar o `hibernate` no Linux Ubuntu [1]
# 
# Para instalar e configurar um servidor SSH no Ubuntu, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja atualizado.
# 
#     2.1 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.2 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.3 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`

# 3. **Instale o Snap (caso ainda não esteja instalado):** O PyCharm pode ser instalado usando o Snap, que é um sistema de empacotamento de aplicativos. Se o Snap não estiver instalado no seu sistema, você pode instalá-lo com o seguinte comando: `sudo apt install snapd -y`
# 
# 4. **Instale o PyCharm Community ou Professional:** Agora você pode instalar o PyCharm Community ou Professional Edition usando o Snap. Escolha a edição que você deseja instalar.
# 
#     4.1 (Opção 1: gratuíta) Para instalar o PyCharm Community Edition, execute o seguinte comando: `sudo snap install pycharm-community --classic`
# 
#     4.2 (Opção 2: paga) Para instalar o PyCharm Professional Edition, execute o seguinte comando: `sudo snap install pycharm-professional --classic`
# 
# 5. **Inicie o PyCharm: ** Depois que a instalação for concluída, você pode iniciar o PyCharm a partir do menu de aplicativos ou usando o seguinte comando no terminal:
# 
#     5.1 Para a versão Community: `pycharm-community`   
# 
#     5.2 Para a versão Professional: `pycharm-professional` 
# 
# O PyCharm será iniciado e você poderá configurá-lo conforme suas preferências.
# 
# Agora você tem o PyCharm instalado no seu sistema Ubuntu e pode começar a desenvolver seus projetos Python.
# 

# ## 2. Código completo
# 
# Para instalar o `PyCharm` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt update -y
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install snapd
#     sudo snap install pycharm-community --classic
#     pycharm-community
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instale o pycharm no ubuntu:*** https://chat.openai.com/c/1d35e7fb-3cd9-4ad1-a53d-34adbb5c5162 (texto adaptado). Acessado em: 21/11/2023 09:45.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 21/11/2023 09:46.
