# Generated by Django 5.0.1 on 2024-01-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_found', '0002_remove_found_found_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='found',
            name='found_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='found',
            name='department',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='found',
            name='item_category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='found',
            name='item_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='found',
            name='student_name',
            field=models.CharField(max_length=25),
        ),
    ]