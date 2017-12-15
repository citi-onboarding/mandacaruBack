from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST': #se um formulário foi submetido por um usuário
        contato = formContato(request.POST) #pegando as respostas preenchidas pelo usuário
        if contato.is_valid:
            nome = contato.cleaned_data.get('nome') #retornando valor da chave nome
            email = contato.cleaned_data.get('email')
            telefone = contato.cleaned_data.get('telefone')
            mensagem = contato.cleaned_data.get('mensagem')
            send_message()
    else: #GET request
        contato = FormContato() #apenas mostra o formulário para ser preenchido

    return render(
        request, 'index.html',
    )