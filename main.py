from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot")

pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   [" + intencao[0]['intent'] + "]")

while (intencao[0]['intent'] != "despedida"):
    if (intencao[0]['intent'] != "saudacao"):
        pergunta = input("Posso lhe ajudar com algo a mais?\n")
    else:
        pergunta = input("Como posso te ajudar?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
