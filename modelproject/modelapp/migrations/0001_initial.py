# Generated by Django 3.2.4 on 2021-06-22 13:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
                ('postal_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('date_of_resumption', models.DateField(default=datetime.datetime.today)),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.school')),
            ],
        ),
    ]
