from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Tarefa
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.forms.models import model_to_dict

def index(request):
    context = {
        'tarefas_andamento': 5,  # Dados fictícios
        'tarefas_pendentes': 2,
        'tarefas_finalizadas': 8,
    }
    return render(request, 'index.html', context)


def editar_email(request):
    if request.method == 'POST':
        novo_email = request.POST.get('email')

        return HttpResponse(f'O novo email é: {novo_email}')
    return render (request, 'editar_email.html')

def cronograma(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'cronograma.html', {'tarefas': tarefas})


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

def criar_atividade(request):
    if request.method == "POST":
        materia = request.POST["materia"]
        conteudo = request.POST["conteudo"]
        status = request.POST["status"]
        prazo = request.POST["prazo"]
        
        return redirect('cronograma')  # Redireciona para o cronograma
   
    return render(request, "criar_atividade.html")


def listar_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades/atividade_list.html', {'atividades': atividades})

def editar_atividade(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)


    if request.method == "POST":
        tarefa.materia = request.POST["materia"]
        tarefa.conteudo = request.POST["conteudo"]
        tarefa.status = request.POST["status"]
        tarefa.prazo = request.POST["prazo"]
        tarefa.save()
        return redirect("cronograma")


    return render(request, "editar_tarefa.html", {"tarefa": tarefa})


def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = "Finalizada"  # Altere conforme sua lógica de status
    tarefa.save()
    return redirect('cronograma')  
   

def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == "POST":
        atividade.delete()
        return redirect('listar_atividades')
    return render(request, 'atividades/atividade_confirm_delete.html', {'atividade': atividade})




