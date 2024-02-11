# Generated by Django 4.2.7 on 2024-01-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lost_and_found_app", "0002_user_last_login_alter_user_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="LostItem",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("item_name", models.CharField(max_length=100)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("date", models.DateField()),
                ("description", models.TextField()),
                ("reward", models.CharField(blank=True, max_length=100)),
                (
                    "item_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="lost_item_images/"
                    ),
                ),
            ],
        ),
    ]
