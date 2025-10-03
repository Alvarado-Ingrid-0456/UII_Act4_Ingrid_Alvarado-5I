from django.shortcuts import render

# Create your views here.

def index(request):
    usuarios = [
        {'nombre': 'Alice Johnson', 'email': 'alice@example.com', 'edad': 30},
        {'nombre': 'Bob Williams', 'email': 'bob@example.com', 'edad': 24},
        {'nombre': 'Charlie Brown', 'email': 'charlie@example.com', 'edad': 35},
    ]
    contexto = {'usuarios': usuarios}
    return render(request, 'index.html', contexto)