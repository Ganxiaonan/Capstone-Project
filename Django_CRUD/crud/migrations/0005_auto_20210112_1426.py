# Generated by Django 3.1.5 on 2021-01-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20210112_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcellist',
            name='destination',
            field=models.CharField(default='undefined', max_length=100),
        ),
    ]
