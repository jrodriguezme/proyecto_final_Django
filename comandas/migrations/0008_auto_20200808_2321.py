# Generated by Django 3.0.8 on 2020-08-09 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0007_formato_fecha_hoy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formato',
            name='fecha_hoy',
            field=models.CharField(default=datetime.date(2020, 8, 8), max_length=50),
        ),
        migrations.AlterField(
            model_name='formato',
            name='numero_comensales',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='formato',
            name='numero_mesa',
            field=models.IntegerField(default=0),
        ),
    ]