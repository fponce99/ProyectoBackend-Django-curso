# Generated by Django 2.1.5 on 2020-09-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCursos', '0005_auto_20200905_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='asistido',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]
