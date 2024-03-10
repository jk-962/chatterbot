from django.shortcuts import render,redirect
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot=ChatBot('chatbot',read_only=False,logic_adapters=
            [
                {
                'import_path':'chatterbot.logic.BestMatch',
                'default_response':'Sorry,I dont know what that means'
                }
                ])

ChatterBotCorpusTrainer=ChatterBotCorpusTrainer(bot)

ChatterBotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,"index.html")

def spec(request):
    return HttpResponse("This is the specific url")

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    return HttpResponse(userMessage)
    





# Create your views here.

































