# Generated by Django 3.0.7 on 2020-08-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20200805_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cargo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_trabajo',
            field=models.CharField(max_length=100),
        ),
    ]
