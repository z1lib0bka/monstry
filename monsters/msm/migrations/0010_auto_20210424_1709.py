# Generated by Django 3.2 on 2021-04-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msm', '0009_auto_20210424_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='test',
        ),
        migrations.AddField(
            model_name='monster',
            name='monster_type',
            field=models.CharField(choices=[('USUAL', 'Usual'), ('RARE', 'Rare'), ('EPIC', 'Epic')], default=('USUAL', 'Usual'), max_length=5, verbose_name='Monster type'),
        ),
    ]
