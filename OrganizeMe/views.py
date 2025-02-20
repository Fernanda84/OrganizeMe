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
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('prazo')
    

        Atividade.objects.create(materia=materia, descricao=descricao , prazo=prazo, status='em andamento')
        
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

def criar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'atividades/atividade_form.html', {'form': form})

def listar_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades/atividade_list.html', {'atividades': atividades})

def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == "POST":
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('listar_atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'atividades/atividade_form.html', {'form': form})

def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    if request.method == "POST":
        atividade.delete()
        return redirect('listar_atividades')
    return render(request, 'atividades/atividade_confirm_delete.html', {'atividade': atividade})




