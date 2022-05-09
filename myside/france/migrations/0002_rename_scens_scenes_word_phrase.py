# Generated by Django 4.0.4 on 2022-05-09 15:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('france', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scens',
            new_name='Scenes',
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_pl', models.CharField(max_length=100)),
                ('word_fr', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('phonetic', models.CharField(blank=True, max_length=100)),
                ('scenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='france.scenes')),
            ],
            options={
                'ordering': ('word_pl', 'word_fr'),
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=100)),
                ('sentence', models.TextField(max_length=400)),
                ('order', models.IntegerField()),
                ('created_at', models.DateField(db_index=True, default=datetime.date.today)),
                ('scenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='france.scenes')),
            ],
            options={
                'ordering': ('scenes', 'order'),
            },
        ),
    ]