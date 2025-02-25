from django.shortcuts import render, redirect
from .models import Atividade
from django.conf import settings
from django.forms.models import model_to_dict
from .forms import AtividadeForm

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
    return render(request, "cronograma.html", {'atividade': atividades})

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


