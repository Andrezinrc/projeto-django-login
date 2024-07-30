from django.db import models

class Register(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    senha = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.nome
