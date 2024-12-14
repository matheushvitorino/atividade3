from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)  

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.IntegerField(max_length=11)  
    usuario_id = models.ForeignKey(
        Usuario,  
        on_delete=models.CASCADE,  
        related_name='telefones'  
    )

    def __str__(self):
        return str(self.numero)
