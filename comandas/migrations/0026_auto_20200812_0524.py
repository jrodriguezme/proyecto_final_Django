# Generated by Django 3.0.8 on 2020-08-12 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0025_auto_20200812_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formato',
            name='pedido_id',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='num_platos',
        ),
    ]
