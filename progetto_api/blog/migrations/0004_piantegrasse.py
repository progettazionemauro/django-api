# Generated by Django 4.2.9 on 2024-09-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_piante"),
    ]

    operations = [
        migrations.CreateModel(
            name="piantegrasse",
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
                ("specie", models.CharField(max_length=255)),
            ],
        ),
    ]
