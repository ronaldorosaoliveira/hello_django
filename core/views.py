from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<center><h1>Olá {nome}! Você tem {idade} anos !!!</h1></center>')
