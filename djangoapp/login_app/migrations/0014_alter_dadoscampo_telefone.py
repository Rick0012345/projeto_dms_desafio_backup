# Generated by Django 5.1 on 2024-09-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_app", "0013_dadoscampo_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dadoscampo",
            name="telefone",
            field=models.CharField(max_length=11),
        ),
    ]
