# Generated by Django 4.1.1 on 2022-09-08 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instargram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='massage',
            new_name='content',
        ),
    ]