# Generated by Django 3.0.7 on 2020-07-16 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20200715_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='foto',
        ),
    ]
