# Generated by Django 5.1.1 on 2024-10-19 06:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locatari", "0002_locatar_first_name_locatar_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avizier",
            name="data_postarii",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
