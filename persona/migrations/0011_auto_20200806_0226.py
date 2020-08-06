# Generated by Django 3.0.7 on 2020-08-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0010_auto_20200804_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='id_trabajo',
            field=models.IntegerField(default=models.CharField(choices=[('administrador', 'ADMINISTRADOR'), ('jefe de cocina', 'JEFE DE COCINA'), ('jefe de almacen', 'JEFE DE ALMACEN'), ('recepcionista', 'RECEPCIONISTA'), ('cajero', 'CAJERO'), ('mesero', 'MESERO'), ('bartender', 'BARTENDER'), ('cocinero', 'COCINERO'), ('otro', 'VARIOS')], default='otro', max_length=100)),
        ),
    ]
