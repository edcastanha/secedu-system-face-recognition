# Generated by Django 4.2.5 on 2023-10-03 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='escalas',
            options={'ordering': ['horario_inicio'], 'verbose_name': 'Escala', 'verbose_name_plural': 'Escalas'},
        ),
        migrations.AlterModelOptions(
            name='escolas',
            options={'ordering': ['nome'], 'verbose_name': 'Escola', 'verbose_name_plural': 'Escolas'},
        ),
    ]
