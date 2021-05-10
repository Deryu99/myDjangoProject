# Generated by Django 3.2 on 2021-05-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=160)),
                ('deadline', models.DateTimeField()),
                ('percent', models.IntegerField()),
            ],
        ),
    ]