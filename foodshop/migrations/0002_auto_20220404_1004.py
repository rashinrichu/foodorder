# Generated by Django 3.1.3 on 2022-04-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categ',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='categ',
            name='price',
        ),
    ]
