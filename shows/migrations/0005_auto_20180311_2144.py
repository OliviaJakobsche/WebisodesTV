# Generated by Django 2.0.1 on 2018-03-11 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20180311_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link',
            new_name='url',
        ),
    ]
