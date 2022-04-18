from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<center><h1>Olá {nome}! Você tem {idade} anos !!!</h1></center>')


def soma(request, n1, n2):
    return HttpResponse(f'<h1><center>A soma entre {n1} e {n2} é igual a {n1 + n2} !</h1></center>')


def subtracao(request, n1, n2):
    return HttpResponse(f'<h1><center>A subtração entre {n1} e {n2} é igual a {n1 - n2} !</h1></center>')


def multiplicacao(request, n1, n2):
    return HttpResponse(f'<h1><center>A multiplicação entre {n1} e {n2} é igual a {n1 * n2} !</h1></center>')


def divisao(request, n1, n2):
    return HttpResponse(f'<h1><center>A divisão entre {n1} e {n2} é igual a {n1 / n2} !</h1></center>')

