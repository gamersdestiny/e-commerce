# Generated by Django 3.2.6 on 2021-08-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_fkeymodel_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fkeymodel',
            name='fName',
            field=models.CharField(max_length=30),
        ),
    ]
