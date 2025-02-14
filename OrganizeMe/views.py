from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Atividade
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.forms.models import model_to_dict

def index(request):
    return render (request, "index.html")


def editar_email(request):
    if request.method == 'POST':
        novo_email = request.POST.get('email')

        return HttpResponse(f'O novo email é: {novo_email}')
    return render (request, 'editar_email.html')

def cronograma(request):
    if request.method == 'POST':
        materia = request.POST.get('materia')
        conteudo = request.POST.get('conteudo')
        prazo = request.POST.get('prazo')

        Atividade.objects.create(materia=materia, conteudo=conteudo, prazo=prazo, status='em andamento')
        
        return HttpResponse('Atividade adicionada com sucesso')

    atividades = Atividade.objects.all()
    return render(request, 'cronograma.html', {'atividades':atividades})
    


def perfil (request):
    if request.method == 'POST':
        estudante = request.POST.get('estudante')

    return render(request, 'perfil.html', {'estudante:estudante'})

def redefinir_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:  
            send_mail(
                'Recuperação de Senha',
                'Clique no link abaixo para redefinir sua senha: <link_de_redefinicao>',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            mensagens(request, 'Instruções de redefinição de senha foram enviadas para o seu e-mail.')

            return redirect('redefinir_senha')
        else:
            messages.error(request, 'Por favor, forneça um e-mail válido.')

    return render(request, 'redefinir_senha.html')




