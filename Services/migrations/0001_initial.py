# Generated by Django 4.2.5 on 2023-09-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_created=True, verbose_name="creación"),
                ),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                (
                    "subtitle",
                    models.CharField(max_length=200, verbose_name="subtítulo"),
                ),
                ("content", models.TextField(verbose_name="contenido")),
                ("image", models.ImageField(upload_to="", verbose_name="imagen")),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="actualizado"),
                ),
            ],
        ),
    ]
