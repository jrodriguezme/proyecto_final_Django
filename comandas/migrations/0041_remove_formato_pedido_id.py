# Generated by Django 3.0.8 on 2020-08-13 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0040_formato_pedido_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formato',
            name='pedido_id',
        ),
    ]
