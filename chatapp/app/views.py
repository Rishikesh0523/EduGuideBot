from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapter=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
    }
])

list_to_train = [
    "Hi", #question1
    "Hi there!", #answer1
    "Hello",
    "Hello I am EduGuideBot",
    "What's your name?",
    "I am EduGuideBot",
    "What is your job?",
    "I am here to guide you about IOE Admission"
    "What is the full form of IOE?",
    "The full form of IOE is Institute of Engineering"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'app/index.html')

def specific(request):
    return HttpResponse("number")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    if chatResponse == "":
        chatResponse = "I'm sorry, I don't understand. Could you please rephrase?"
    return HttpResponse(chatResponse)