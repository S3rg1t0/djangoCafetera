from django.db import models

# Create your models here.


class Date(models.Model):

    title = models.CharField(max_length=200, verbose_name="título")
    laboral = models.CharField(verbose_name="Horario L-V", max_length=100, default="")
    saturday = models.CharField(verbose_name="Horario Sábado", max_length=100, default="")
    sunday = models.CharField(verbose_name="Horario Domingo", max_length=100, default="")
    street = models.CharField(verbose_name="Calle", max_length=200, default="")
    city = models.CharField(verbose_name="Población", max_length=200, default="")
    phone = models.CharField(verbose_name="Teléfono", max_length=100, default="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "horario"
        verbose_name_plural = "horarios"
        ordering = ["-created"]

    def __str__(self):
        return self.title




