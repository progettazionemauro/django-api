# Generated by Django 4.2.9 on 2024-05-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=255)),
                ("text", models.TextField()),
                ("file_name", models.CharField(max_length=255, unique=True)),
                ("image_name", models.CharField(max_length=255)),
                ("image_link", models.URLField()),
            ],
        ),
    ]
