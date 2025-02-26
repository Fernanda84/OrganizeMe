from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cronograma/', views.cronograma, name='cronograma'),
    path('', views.listar_atividades, name='listar_atividades'),
    path('criar_atividade/', views.criar_atividade, name='criar_atividade'),
    path('editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
    path('excluir/<int:id>/', views.excluir_atividade, name='excluir_atividade'),
    path('concluir/<int:pk>/', views.concluir_atividade, name='concluir_atividade'),

]