# Generated by Django 5.0.2 on 2024-02-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agents',
            name='fonction',
        ),
        migrations.DeleteModel(
            name='Fonction',
        ),
    ]
