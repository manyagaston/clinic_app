# Generated by Django 5.0.2 on 2024-02-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infirmiers', '0002_remove_infirmiers_id_infirmiers_agents_ptr'),
        ('malade', '0004_remove_malade_infirmier'),
    ]

    operations = [
        migrations.AddField(
            model_name='malade',
            name='infirmier',
            field=models.ManyToManyField(to='infirmiers.infirmiers'),
        ),
    ]
