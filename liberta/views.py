from django.shortcuts import render

def login_view(request):
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
