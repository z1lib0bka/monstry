# Generated by Django 3.2 on 2021-04-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msm', '0007_alter_monster_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='monster_type',
            field=models.CharField(choices=[('USUAL', 'Usual'), ('RARE', 'Rare'), ('EPIC', 'Epic')], default=None, max_length=5, verbose_name='Monster type'),
        ),
    ]
