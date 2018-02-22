# Generated by Django 2.0.2 on 2018-02-22 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('main_app', '0017_auto_20180222_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
            ],
        ),
    ]
