# Generated by Django 2.2.1 on 2019-08-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_packagepermission'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='packagepermission',
            constraint=models.UniqueConstraint(fields=('user', 'package',), name='unique_owner'),
        ),
    ]
