# Consuelo-chatbot-Python
# Feito por Rodrigo Smith

Um simples chatbot, feito com Python, Machine Learning, Chatterbot e PySimpleGUI. 
Utiliza a biblioteca ChatterBot para o aprendizado da máquina. Necessita de um database de conversas iniciais,
que é disponibilizado em https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese e
https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english. 
A partir disso, conforme se conversa com o bot, ele aprende novas perguntas e respostas. 
Como ele não está conectado a um banco de dados público e não são salvas as conversas no computador em que ele é executado,
o conhecimento do bot é reiniciado toda vez que o aplicativo é fechado.

Também utilizei a biblioteca PySimpleGUI, que permite criar interfaces gráficas facilmente com Python.
