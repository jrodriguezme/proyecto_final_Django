# Generated by Django 3.0.7 on 2020-08-13 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0041_remove_formato_pedido_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formato',
            name='fecha_hoy',
            field=models.CharField(blank=True, default=datetime.date(2020, 8, 13), max_length=50, null=True),
        ),
    ]