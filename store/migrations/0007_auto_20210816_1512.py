# Generated by Django 3.2.6 on 2021-08-16 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 8, 16, 15, 12, 19, 939646, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
