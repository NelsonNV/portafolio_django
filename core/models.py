from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Iconos(BaseModel):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    icono = models.FileField(upload_to="iconos/")
    logo = models.FileField(upload_to="iconos/")
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Ícono"
        verbose_name_plural = "Íconos"

    def save(self, *args, **kwargs):
        # Si este registro se marca como activo, desactiva los demás
        if self.activo:
            Iconos.objects.filter(activo=True).exclude(pk=self.pk).update(activo=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre}"
