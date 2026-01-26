from django.shortcuts import render, redirect
from .models import Atividade  
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    andamento = Atividade.objects.filter(status='Em andamento').count()
    pendente = Atividade.objects.filter(status='Pendente').count()
    finalizadas = Atividade.objects.filter(status='Finalizada').count()

    return render(request, 'index.html', {
        'andamento': andamento,
        'pendente': pendente,
        'finalizadas': finalizadas
    })
def pagina_inicial(request):
    return render(request, 'index.html')

def cronograma(request):
    atividades = Atividade.objects.all().order_by('prazo')

    return render(request, 'cronograma.html', {
        'atividades': atividades
    })

def criar_tarefa(request):
    return render(request, 'criar_tarefa.html')

def criar_atividade(request):
    if request.method == "POST":
        materia = request.POST.get("materia")
        conteudo = request.POST.get("conteudo")
        prazo = request.POST.get("prazo")

        Atividade.objects.create(
            materia=materia,
            conteudo=conteudo,
            prazo=prazo,
            status="Pendente"
        )

        return redirect("cronograma")

    return render(request, "criar_atividade.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')