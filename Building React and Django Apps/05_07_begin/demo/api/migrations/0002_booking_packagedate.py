# Generated by Django 2.2.1 on 2019-07-17 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
                ('package_date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.PackageDate')),
            ],
        ),
    ]
