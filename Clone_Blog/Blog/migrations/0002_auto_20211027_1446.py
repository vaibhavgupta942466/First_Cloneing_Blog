# Generated by Django 3.2.5 on 2021-10-27 09:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 9, 16, 11, 463695, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 9, 16, 11, 462697, tzinfo=utc)),
        ),
    ]