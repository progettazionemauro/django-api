# Generated by Django 4.2.9 on 2024-05-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_api_for_wagtail", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomFeature",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
            ],
        ),
    ]