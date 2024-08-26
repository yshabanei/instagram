# Generated by Django 5.1 on 2024-08-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                    "created_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created_time"
                    ),
                ),
                (
                    "modified_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="modified_time"
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="title")),
                ("points", models.JSONField(verbose_name="points")),
            ],
            options={
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
            },
        ),
    ]
