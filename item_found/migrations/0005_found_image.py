# Generated by Django 5.0.1 on 2024-01-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_found', '0004_rename_found_place_found_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='found',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]