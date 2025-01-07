from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Iconos(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    icono = models.FileField(upload_to="iconos/")
    logo = models.FileField(upload_to="iconos/")
    activo = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"
