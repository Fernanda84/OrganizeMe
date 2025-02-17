from django.shortcuts import render

def login(request):
    return render(request, 'usuario/login.html')

def redefinir_senha(request):
    return render(request, 'redefinir_senha.html')
