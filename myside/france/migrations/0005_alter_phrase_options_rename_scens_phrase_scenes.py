# Generated by Django 4.0.4 on 2022-05-05 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('france', '0004_alter_phrase_sentence'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phrase',
            options={'ordering': ('scenes', 'order')},
        ),
        migrations.RenameField(
            model_name='phrase',
            old_name='scens',
            new_name='scenes',
        ),
    ]
