# Generated by Django 5.1 on 2024-08-15 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Campo",
            new_name="Coordenada",
        ),
        migrations.AlterModelOptions(
            name="coordenada",
            options={
                "verbose_name": "Coordenada",
                "verbose_name_plural": "Coordenadas",
            },
        ),
    ]
