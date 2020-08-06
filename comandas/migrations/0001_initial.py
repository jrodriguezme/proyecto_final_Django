# Generated by Django 3.0.7 on 2020-08-05 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hoy', models.DateTimeField(default=datetime.date(2020, 8, 5))),
                ('numero_mesa', models.IntegerField()),
                ('numero_comensales', models.IntegerField()),
                ('id_camarero', models.CharField(max_length=100)),
                ('id_platos', models.CharField(max_length=100)),
            ],
        ),
    ]
