# Generated by Django 3.0.8 on 2020-08-13 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0035_auto_20200812_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='vincu',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comandas.Formato'),
        ),
    ]
