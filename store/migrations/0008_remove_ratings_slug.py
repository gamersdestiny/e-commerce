# Generated by Django 3.2.6 on 2021-08-16 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210816_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='slug',
        ),
    ]
