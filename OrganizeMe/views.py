from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Atividade
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.forms.models import model_to_dict
from .forms import AtividadeForm
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def index(request):
    tarefas_em_andamento = Atividade.objects.filter(status="em andamento")
    tarefas_pendentes = Atividade.objects.filter(status="pendente")
    tarefas_finalizadas = Atividade.objects.filter(status="finalizada")

    context = {
        "tarefas_em_andamento": tarefas_em_andamento,
        "tarefas_pendentes": tarefas_pendentes,
        "tarefas_finalizadas": tarefas_finalizadas
    }
    
    return render(request, "index.html", context)

def cronograma(request):
    atividades = Atividade.objects.all().order_by('prazo')  # Ordena pelo prazo
    return render(request, "cronograma.html", {"atividades": atividades})

def criar_atividade(request):
    if request.method == "POST":
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cronograma")
    else:
        form = AtividadeForm()
    
    return render(request, "criar_atividade.html", {"form": form})

def listar_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, "listar_atividades.html", {"atividades": atividades})

def editar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    
    if request.method == "POST":
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect("listar_atividades")
    else:
        form = AtividadeForm(instance=atividade)
    
    return render(request, "editar_atividade.html", {"form": form, "atividade": atividade})

def excluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    
    if request.method == "POST":
        atividade.delete()
        return redirect("listar_atividades")
    
    return render(request, "excluir_atividade.html", {"atividade": atividade})

def concluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.status = "concluida"
    atividade.save()
    return redirect("listar_atividades")

@login_required
def perfil(request):
    usuario = request.user

    if request.method == "POST" and request.FILES.get("foto"):
        usuario.foto = request.FILES["foto"]
        usuario.save()
        return redirect("perfil")

    return render(request, "perfil.html", {"usuario": usuario})

@login_required
def editar_email(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "editar_email.html", {"form": form})

@login_required
def editar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            return redirect("perfil")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "editar_senha.html", {"form": form})

       