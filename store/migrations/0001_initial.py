# Generated by Django 3.2.6 on 2021-08-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(max_length=3)),
                ('dateAdded', models.DateTimeField()),
            ],
        ),
    ]
