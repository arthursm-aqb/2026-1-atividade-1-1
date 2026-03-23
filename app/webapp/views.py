from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Arthur Mariz em SO!")

# Create your views here.
