# Generated by Django 5.0.6 on 2024-07-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_acessorio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessório", "verbose_name_plural": "Acessórios"},
        ),
    ]
