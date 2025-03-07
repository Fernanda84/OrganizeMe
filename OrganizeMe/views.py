from django.shortcuts import render, redirect, get_object_or_404
from .models import Atividade, Perfil
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import AtividadeForm, CadastroForm, LoginForm, EditarPerfilForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    tarefas_em_andamento = Atividade.objects.filter(status="em andamento",estudante=request.user) if request.user.is_authenticated else [] 
    tarefas_pendentes = Atividade.objects.filter(status="pendente",estudante=request.user) if request.user.is_authenticated else [] 
    tarefas_finalizadas = Atividade.objects.filter(status="concluido",estudante=request.user) if request.user.is_authenticated else [] 

    context = {
        "tarefas_em_andamento": tarefas_em_andamento,
        "tarefas_pendentes": tarefas_pendentes,
        "tarefas_finalizadas": tarefas_finalizadas
    }
    
    return render(request, "index.html", context)

@login_required
def cronograma(request):
    atividades = Atividade.objects.filter(estudante=request.user).order_by('prazo')  # Ordena pelo prazo
    
    paginator = Paginator(atividades, 9)
    numero_da_pagina = request.GET.get('pagina')  
    atividades_paginadas = paginator.get_page(numero_da_pagina)
    
    return render(request, "cronograma.html", {'atividades': atividades_paginadas})

@login_required
def criar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.estudante = request.user
            atividade.save()
            return redirect("cronograma")
    else:
        form = AtividadeForm()
    
    return render(request, "criar_atividade.html", {"form": form})


@login_required
def editar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect("cronograma")
    else:
        form = AtividadeForm(instance=atividade)
    
    return render(request, "editar_atividade.html", {"form": form, "atividade": atividade})

@login_required
def excluir_atividade(request, atividade_id):
    
    if request.method == 'POST':
       atividade = get_object_or_404(Atividade, id=atividade_id)
       atividade.delete()
       return JsonResponse({"success": True})
    return JsonResponse({"success":False}, status=400)
    

@login_required
def concluir_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    atividade.status = "concluida"
    atividade.save()
    return redirect("cronograma")

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user)
            login(request, user) 
            return redirect('index') 
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('perfil')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def perfil(request):
    perfil = Perfil.objects.filter(usuario=request.user)
    return render(request, "perfil.html", {'perfil': perfil})

def logout_usuario(request):
    logout(request) 
    return redirect('login')

@login_required
def editar_perfil(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id, usuario=request.user)
    
    if request.method == 'POST':
        # Preenche o formulário com os dados enviados para edição
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido atualizado com sucesso!")
            return redirect('carrinho')  # Redireciona para o carrinho ou outra página
    else:
        # Inicializa o formulário com os dados atuais do pedido
        form = EditarPerfilForm(instance=perfil)
    return render(request, "editar_perfil.html", {"form": form})


@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Atualiza a sessão do usuário para evitar logout
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('perfil')  # Redireciona para a página de perfil
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'alterar_senha.html', {'form': form})