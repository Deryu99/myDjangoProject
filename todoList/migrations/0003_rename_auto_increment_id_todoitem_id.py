# Generated by Django 3.2 on 2021-05-10 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_auto_20210510_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='auto_increment_id',
            new_name='id',
        ),
    ]
