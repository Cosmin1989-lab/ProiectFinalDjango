# Generated by Django 5.1.2 on 2024-10-13 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Apartament",
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
                ("numar", models.CharField(max_length=10)),
                ("scara", models.CharField(max_length=10)),
                ("etaj", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Avizier",
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
                ("titlu", models.CharField(max_length=100)),
                ("mesaj", models.TextField()),
                ("data_postarii", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Locatar",
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
                ("telefon", models.CharField(blank=True, max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "apartament",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="locatari.apartament",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FacturaIntretinere",
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
                ("luna", models.CharField(max_length=20)),
                ("valoare", models.DecimalField(decimal_places=2, max_digits=7)),
                ("achitata", models.BooleanField(default=False)),
                (
                    "locatar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locatari.locatar",
                    ),
                ),
            ],
        ),
    ]
