from django.db import models

# Create your models here.

class Cliente(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    idCredito = models.CharField(max_length=10)
    valor = models.CharField(max_length=10)
    plazo = models.CharField(max_length=2)
    cuota = models.CharField(max_length=10
    )

    def __str__(self):
        texto = "{0}, ({1}), {2}, {3}, {4}, {5}"
        return texto.format(self.nombre, self.identificacion, self.idCredito, self.valor, self.plazo, self.cuota)
    


