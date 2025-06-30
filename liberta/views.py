from django.shortcuts import render, redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login

from django.shortcuts import render

def autoavaliacao_view(request):
    resultado = None

    if request.method == 'POST':
        sim_count = sum(
            1 for i in range(1, 6)
            if request.POST.get(f"q{i}") == "sim"
        )

        if sim_count >= 3:
            resultado = {
                "classe": "alerta",
                "texto": (
                    f'Você respondeu "Sim" em {sim_count} de 5 perguntas. '
                    'Recomendamos procurar ajuda profissional. '
                    'Ligue para 188 ou procure um serviço especializado.'
                )
            }
        else:
            resultado = {
                "classe": "sucesso",
                "texto": (
                    f'Você respondeu "Sim" em {sim_count} de 5 perguntas. '
                    'Parabéns, você está indo bem! Continue atento(a) aos seus hábitos.'
                )
            }

    return render(request, "perguntas.html", {
        "resultado": resultado
    })



usuarios = []  

def cadastro_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=usuario).exists():
            return render(request, 'cadastro.html', {'erro': 'Usuário já existe'})

        user = User(username=usuario, email=email)
        user.set_password(senha)  
        user.save()

        return redirect('login')

    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        senha_input = request.POST.get('senha')

        user = authenticate(username=usuario_input, password=senha_input)

        if user is not None:
            login(request, user)  
            return redirect('pagina_inicial')
        else:
            erro = "Usuário ou senha incorretos"
            return render(request, 'index.html', {'erro': erro})

    return render(request, 'index.html')



def pagina_inicial_view(request):
    return render(request, 'paginainicial.html')

def diferenca_view(request):
    contexto = {
        "investimento": [
            "Estudo e análise",
            "Rentabilidade no longo prazo",
            "Riscos calculados",
            "Regulado por órgãos oficiais",
            "Pode gerar patrimônio"
        ],
        "aposta": [
            "Impulsividade",
            "Ganho rápido (ou perda rápida)",
            "Alta dependência da sorte",
            "Riscos não controlados",
            "Pode causar vício"
        ]
    }
    return render(request, 'diferencas.html', contexto)

def depoimentos_view(request):
    return render(request, 'depoimentos.html')

def apoio_view(request):
    return render(request, 'apoio.html')

def chat_view(request):
    return render(request, 'chat.html')

def progresso_view(request):
    return render(request, 'progresso.html')
