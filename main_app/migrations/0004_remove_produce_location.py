# Generated by Django 2.0.2 on 2018-02-18 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_produce_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produce',
            name='location',
        ),
    ]
