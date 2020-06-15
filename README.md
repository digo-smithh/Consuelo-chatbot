# 👩 Consuelo-chatbot-Python 👩
### Feito por Rodrigo Smith, em Python

Um simples chatbot, feito com Python; conceitos de Machine Learning e as bibliotecas Chatterbot e PySimpleGUI. 

## 📓 Machine Learning 📓
Machine learning (aprendizado de máquina) é um sistema que pode modificar seu próprio comportamento autonomamente tendo como base a sua própria experiência — a interferência humana é mínima. Nesse caso, a experiência é o database inicial + nossas conversas com o bot.

## 💬 Chatterbot 💬
Utilizei a biblioteca Chatterbot para o aprendizado da máquina. Necessita de um database de conversas iniciais,
que está disponibilizado em

##### https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese e
##### https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english. 

A partir disso, conforme se conversa com o bot, ele aprende novas perguntas e respostas. 
Como ele não está conectado a um banco de dados público e não são salvas as conversas no computador em que ele é executado,
o conhecimento do bot é reiniciado toda vez que o aplicativo é fechado.

## 🎨 PySimpleGUI 🎨
Também utilizei a biblioteca PySimpleGUI, que permite criar interfaces gráficas facilmente com Python (isso pode ser percebido observando o meu código, que é muito sucinto, porém, funcional).

# ❓ Como usar ❓

### Preparação
Ao fazer download dos arquivos necessários, compile e execute o arquivo Consuelo.py. Para isso, é necessário ter o Python instalado (recomendo a versão 3.7.7) e uma IDE de sua preferência, como Anaconda ou Visual Studio Code (instale a extensão "Python").
##### Para mais detalhes, leia https://docs.microsoft.com/pt-br/learn/modules/python-install-vscode/

### Execução
Ao abrir a interface, digite alguma mensagem e aperte "Enviar" ou [Enter]. Observe que a Consuelo percebe quando você envia mensagens sem nenhum conteúdo! A Consuelo é capaz de falar inglês e português, INICIALMENTE.
