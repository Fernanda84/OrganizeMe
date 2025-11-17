from django.shortcuts import render
from .models import Atividade  

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

def redefinir_senha(request):
    return render(request, 'redefinir_senha.html')

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
