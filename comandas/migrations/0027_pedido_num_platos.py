# Generated by Django 3.0.8 on 2020-08-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0026_auto_20200812_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='num_platos',
            field=models.IntegerField(default=0),
        ),
    ]
