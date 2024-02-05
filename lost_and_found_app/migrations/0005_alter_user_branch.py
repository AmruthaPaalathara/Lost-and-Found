# Generated by Django 4.2.7 on 2024-02-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lost_and_found_app", "0004_founditem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="branch",
            field=models.CharField(
                choices=[
                    ("ba", "BA"),
                    ("bba", "BBA"),
                    ("bsds", "BSC Data Science"),
                    ("bsea", "BSC Economic Analytic"),
                    ("msds", "MSC Data Science"),
                    ("mba", "MBA"),
                ],
                max_length=100,
            ),
        ),
    ]