# Generated by Django 5.0.2 on 2024-02-27 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('malade', '0003_remove_malade_infirmier_malade_infirmier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='malade',
            name='infirmier',
        ),
    ]
