# Generated by Django 3.0.8 on 2020-08-09 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0021_merge_20200808_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id_cliente',
        ),
    ]
