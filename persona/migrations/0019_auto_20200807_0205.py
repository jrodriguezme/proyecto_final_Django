# Generated by Django 3.0.7 on 2020-08-07 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0018_cliente_comandas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comanda',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='comanda',
            old_name='plato_id',
            new_name='dish',
        ),
    ]