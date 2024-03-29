# Generated by Django 4.2.7 on 2024-01-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lost_and_found_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
