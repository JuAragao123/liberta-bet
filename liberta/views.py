from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect

usuarios = []  

def cadastro_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuarios.append({
            'usuario': usuario,
            'email': email,
            'senha': senha
        })

        return redirect('login')

    return render(request, 'cadastro.html')



def login_view(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        senha_input = request.POST.get('senha')

        for user in usuarios:
            if user['usuario'] == usuario_input and user['senha'] == senha_input:
                return redirect('pagina_inicial')

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
