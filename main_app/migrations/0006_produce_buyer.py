# Generated by Django 2.0.2 on 2018-02-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20180219_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='buyer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
