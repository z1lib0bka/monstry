# Generated by Django 3.2 on 2021-04-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msm', '0006_auto_20210421_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='image',
            field=models.ImageField(null=True, upload_to='image', verbose_name='Monster image'),
        ),
    ]