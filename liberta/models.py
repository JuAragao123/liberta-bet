from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha_hash = models.CharField(max_length=255)
    dias_sem_apostar = models.IntegerField()
    data_ultimo_reset = models.DateTimeField()

    def __str__(self):
        return self.nome


class Depoimento(models.Model):
    nome_usuario = models.CharField(max_length=255)
    idade = models.IntegerField()
    texto = models.TextField()
    exibir = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_usuario


class MensagemDoChat(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_hora = models.DateTimeField()

    def __str__(self):
        return f'{self.usuario.nome}: {self.mensagem[:30]}...'


class Autoavaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_resposta = models.DateTimeField()
    pontuacao_total = models.IntegerField()

    def __str__(self):
        return f'Avaliação de {self.usuario.nome} em {self.data_resposta.date()}'


class PerguntaAutoavaliacao(models.Model):
    texto_pergunta = models.TextField()
    tipo_resposta = models.CharField(max_length=100)

    def __str__(self):
        return self.texto_pergunta[:50]


class RespostaAutoavaliacao(models.Model):
    avaliacao = models.ForeignKey(Autoavaliacao, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(PerguntaAutoavaliacao, on_delete=models.CASCADE)
    resposta = models.TextField()

    def __str__(self):
        return f'Resposta para "{self.pergunta}"'


class Site(models.Model):
    def __str__(self):
        return f"Site {self.id}"


class ComparativoInvestimentoAposta(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.tipo


class ConteudoApp(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Recado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField()
    descricao = models.TextField()
    sentimento = models.CharField(max_length=100)

    def __str__(self):
        return f'Recado de {self.usuario.nome} ({self.sentimento})'
