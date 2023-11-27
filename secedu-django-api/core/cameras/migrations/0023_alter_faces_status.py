# Generated by Django 4.2.7 on 2023-11-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0022_frequenciasescolar_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faces',
            name='status',
            field=models.CharField(choices=[('Criado', 'Criado'), ('Processado', 'Processado'), ('Error', 'Error')], default='Criado', max_length=20),
        ),
    ]
