from django.db import models
from django.contrib.auth.models import User

class RecoveryProgress(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   days_clean = models.PositiveIntegerField(default=0)
   last_reset = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user.username} - {self.days_clean} dias sem apostar"

class AppContent(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField(blank=True)
   content_type = models.CharField(max_length=50, choices=[
       ('article', 'Artigo'),
       ('video', 'Vídeo'),
       ('tip', 'Dica')
   ])
   order = models.PositiveIntegerField(default=0)

   def __str__(self):
       return f"{self.title} ({self.content_type})"

class QuickAccess(models.Model):
   name = models.CharField(max_length=100)
   icon = models.CharField(max_length=20)
   route = models.CharField(max_length=255)

   def __str__(self):
       return self.name
   
class Diferenca(models.Model):
    titulo = models.CharField(max_length=100)
    texto_investimento = models.TextField()
    texto_aposta = models.TextField()
