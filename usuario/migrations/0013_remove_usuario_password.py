# Generated by Django 3.0.7 on 2020-08-06 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_auto_20200806_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
    ]
