# Generated by Django 3.0.7 on 2020-08-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0014_auto_20200806_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='id_trabajo',
        ),
        migrations.AlterField(
            model_name='personal',
            name='dni',
            field=models.CharField(max_length=100),
        ),
    ]