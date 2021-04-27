# Generated by Django 3.2 on 2021-04-26 10:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msm', '0011_alter_monster_monster_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='advanced_time',
            field=models.DurationField(default=datetime.timedelta(seconds=32400), verbose_name='Улучшенное время выведения'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='default_time',
            field=models.DurationField(default=datetime.timedelta(seconds=43200), verbose_name='Обычное время выведения'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='image',
            field=models.ImageField(null=True, upload_to='image', verbose_name='Картинка монстра'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Имя монстра'),
        ),
        migrations.CreateModel(
            name='BreedingStrategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeding_monster1', to='msm.monster', verbose_name='Монстр 1')),
                ('monster2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeding_monster2', to='msm.monster', verbose_name='Монстр 2')),
                ('result_monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeding_monster_result', to='msm.monster', verbose_name='Результат')),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='how_to_breed',
            field=models.ManyToManyField(to='msm.BreedingStrategy', verbose_name='Стратегия вывежения'),
        ),
    ]