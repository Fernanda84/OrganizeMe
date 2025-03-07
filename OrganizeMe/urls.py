from django.urls import path
from . import views
from .views import logout_usuario, login_view, cadastro_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('cronograma/', views.cronograma, name='cronograma'),
    path('criar_atividade/', views.criar_atividade, name='criar_atividade'),
    path('editar/<int:atividade_id>/', views.editar_atividade, name='editar_atividade'),
    path('excluir/<int:atividade_id>/', views.excluir_atividade, name='excluir_atividade'),
    path('concluir/<int:atividade_id>/', views.concluir_atividade, name='concluir_atividade'),
    path('cadastro/', cadastro_usuario, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/<int:perfil_id>/', views.editar_perfil, name='editar_perfil'),
    path('logout/', logout_usuario, name='logout'),
    path('resetar-senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('resetar-senha/sucesso/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetar-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetar-senha/completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]