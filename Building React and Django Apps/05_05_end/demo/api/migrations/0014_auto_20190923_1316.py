# Generated by Django 2.2.4 on 2019-09-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190923_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='street_address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
