# Generated by Django 3.0.7 on 2020-07-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20200724_0529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='id_dni',
            new_name='id_trabajo',
        ),
        migrations.AddField(
            model_name='personal',
            name='dni',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
