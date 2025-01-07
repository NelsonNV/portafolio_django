from django.db import models
from core.models import BaseModel


class SobreMi(BaseModel):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    descripcion = models.TextField()
    perfil = models.ImageField(upload_to="sobremi/")
    fondo = models.ImageField(upload_to="sobremi/")

    def save(self, *args, **kwargs):
        # Permitir solo un registro
        if not self.pk and SobreMi.objects.exists():
            raise ValueError("Solo se permite un registro en la tabla 'SobreMi'.")
        super().save(*args, **kwargs)

    def full_name(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre}"


class SocialLink(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    svg = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class Projecto(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    repository = models.URLField()
    image = models.ImageField(upload_to="project/")
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Experiencia(BaseModel):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    mostrar = models.BooleanField()

    def __str__(self):
        return f"{self.empresa}"


class Estudios(BaseModel):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    description = models.TextField()
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    mostrar = models.BooleanField()
    certificado = models.FileField(upload_to="certificados/", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"
