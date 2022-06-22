from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#  create a Chat Bot

chatbot = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english.conversation')

while True:
    query = str(input("--> "))
    print(chatbot.get_response(query))
    if "exit" in query:
        break

