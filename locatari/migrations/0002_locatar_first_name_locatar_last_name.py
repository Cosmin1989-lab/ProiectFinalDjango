# Generated by Django 5.1.2 on 2024-10-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locatari", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="locatar",
            name="first_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="locatar",
            name="last_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
