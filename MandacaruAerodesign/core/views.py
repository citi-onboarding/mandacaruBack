from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from templated_email import send_templated_mail

# Create your views here.
def index(request):
    if request.method == 'POST': #se um formulário foi submetido por um usuário
        nome = request.POST.get('nome') #retornando valor da chave nome
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        foi = send_templated_mail(
        template_name='email', 
        from_email=email,
        recipient_list=[''], #email do cliente/de quem enviar o email
        context={
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'mensagem': mensagem
        },
        )   
    infos = infoPS.objects.first()

    contexto = { 'infos_ativo': infos.ativo }

    return render(
        request, 'index.html', contexto
    )