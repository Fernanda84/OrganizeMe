from django.urls import path
from .views import login, redefinir_senha

urlpatterns = [
    path('login/', login, name='login'),
    path('redefinir_senha/', redefinir_senha, name='redefinir_senha'),
]
