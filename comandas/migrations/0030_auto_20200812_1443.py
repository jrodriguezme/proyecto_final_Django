# Generated by Django 3.0.8 on 2020-08-12 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0029_pedido_formato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='formato',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='comandas.Formato'),
        ),
    ]