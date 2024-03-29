# Generated by Django 4.0.4 on 2022-05-17 16:49

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=10)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=5, populate_from='room', unique_with=('pub_date',))),
            ],
        ),
        migrations.CreateModel(
            name='ScannerRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biometrics.scanners', verbose_name='Room')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Student')),
            ],
        ),
    ]
