# Generated by Django 5.1 on 2024-09-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login_app", "0010_alter_coordenada_valor_hora_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reservas",
            new_name="Reserva",
        ),
    ]
