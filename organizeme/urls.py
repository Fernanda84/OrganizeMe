from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('cronograma/', views.cronograma, name='cronograma'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
