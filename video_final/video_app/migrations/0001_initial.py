# Generated by Django 4.1 on 2022-09-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("video", models.FileField(upload_to="video/%y")),
                ("thumb", models.FileField(blank=True, upload_to="thumb/%y")),
            ],
        ),
    ]