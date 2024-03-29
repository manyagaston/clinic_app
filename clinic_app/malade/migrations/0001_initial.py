# Generated by Django 5.0.2 on 2024-02-27 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docteurs', '0003_remove_docteur_id_docteur_agents_ptr'),
        ('infirmiers', '0002_remove_infirmiers_id_infirmiers_agents_ptr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('post_nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('sexe', models.CharField(max_length=8)),
                ('docteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docteurs.docteur', unique=True)),
                ('infirmier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infirmiers.infirmiers', unique=True)),
            ],
            options={
                'verbose_name': 'Malade',
                'verbose_name_plural': 'Malades',
            },
        ),
    ]
