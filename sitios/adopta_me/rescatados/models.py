from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Rescatado(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    info = RichTextField(verbose_name="Información personal")
    description = RichTextField(verbose_name="Personalidad")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['created']

    def __str__(self):
        return self.name