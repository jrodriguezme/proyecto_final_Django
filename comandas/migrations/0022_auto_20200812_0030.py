# Generated by Django 3.0.8 on 2020-08-12 05:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0021_auto_20200811_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formato',
            name='pedido_ptr',
        ),
        migrations.AddField(
            model_name='formato',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formato',
            name='pedido_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='comandas.Pedido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formato',
            name='fecha_hoy',
            field=models.CharField(default=datetime.date(2020, 8, 12), max_length=50),
        ),
    ]