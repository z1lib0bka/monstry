# Generated by Django 3.2 on 2021-04-20 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msm', '0003_auto_20210419_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='advanced_time',
            field=models.DurationField(default=datetime.timedelta(seconds=32400), verbose_name='Advanced Time to breed'),
        ),
        migrations.AddField(
            model_name='monster',
            name='default_time',
            field=models.DurationField(default=datetime.timedelta(seconds=43200), verbose_name='Default Time to breed'),
        ),
    ]
