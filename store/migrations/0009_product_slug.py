# Generated by Django 3.2.6 on 2021-08-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_ratings_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='arabian nights'),
            preserve_default=False,
        ),
    ]