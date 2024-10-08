# Generated by Django 5.1 on 2024-08-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campo",
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
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            options={
                "verbose_name": "Campo",
                "verbose_name_plural": "Campos",
            },
        ),
    ]
