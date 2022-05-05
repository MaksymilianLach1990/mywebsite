# Generated by Django 4.0.4 on 2022-05-05 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=300)),
                ('created_at', models.DateField(db_index=True, default=datetime.date.today)),
            ],
            options={
                'ordering': ('name', 'created_at'),
            },
        ),
    ]