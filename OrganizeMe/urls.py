from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('editar-email/', views.editar_email, name='editar_email'),
    path('cronograma/', views.cronograma, name='cronograma'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_email/', views.editar_email, name='editar_email'),
    path('redefinir_senha/', views.redefinir_senha, name='redefinir_senha'),
    path('', views.listar_atividades, name='listar_atividades'),
    path('nova/', views.criar_atividade, name='criar_atividade'),
    path('editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
    path('excluir/<int:id>/', views.excluir_atividade, name='excluir_atividade'),
   
]