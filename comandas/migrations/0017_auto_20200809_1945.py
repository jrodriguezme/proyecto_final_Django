# Generated by Django 3.0.8 on 2020-08-10 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0004_platos_precio'),
        ('comandas', '0016_auto_20200809_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='platos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='platos.Platos'),
        ),
    ]
