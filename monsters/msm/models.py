from django.db import models
from django.conf import settings
from django.urls import reverse


class Monster(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя монстра')

    image = models.ImageField(upload_to='image', null=True, verbose_name='Картинка монстра')

    how_to_breed = models.ManyToManyField(to='BreedingStrategy', verbose_name='Стратегия выведения')

    default_time = models.DurationField(verbose_name='Обычное время выведения',
                                        default=settings.INITIAL_DEFAULT_TIME)

    advanced_time = models.DurationField(verbose_name='Улучшенное время выведения',
                                         default=settings.INITIAL_ADVANCED_TIME)

    buy_cost = models.fields.PositiveIntegerField(verbose_name='Buy cost')

    sell_cost = models.fields.PositiveIntegerField(verbose_name='Sell cost')

    monster_type = models.CharField(max_length=5,
                                    choices=settings.MONSTER_TYPES,
                                    default=settings.MONSTER_TYPES[0][0],
                                    verbose_name='Monster type',
                                    )

    # make islands
    # food (???) maybi potom

    def get_absolute_url(self):
        return reverse('islands:monster_detail', args=[self.id])

    def __str__(self):
        return "{}".format(self.name)


class Island(models.Model):
    name = models.CharField(max_length=32, verbose_name='Island name')

    level = models.fields.PositiveIntegerField(verbose_name='Level')

    cost = models.fields.PositiveIntegerField(verbose_name='Cost')

    mirror_cost = models.fields.PositiveIntegerField(verbose_name='Mirror cost')

    monsters = models.ManyToManyField(to='Monster', verbose_name='Monsters')

    # uluchsheniya maybi potom


class BreedingStrategy(models.Model):
    monster1 = models.ForeignKey(to='Monster',
                                 verbose_name='Монстр 1',
                                 on_delete=models.CASCADE,
                                 related_name='breeding_monster1',
                                 )

    monster2 = models.ForeignKey(to='Monster',
                                 verbose_name='Монстр 2',
                                 on_delete=models.CASCADE,
                                 related_name='breeding_monster2',
                                 )

    result_monster = models.ForeignKey(to='Monster',
                                       verbose_name='Результат',
                                       on_delete=models.CASCADE,
                                       related_name='breeding_monster_result',
                                       )

    # island = models.ForeignKey(to='Island', verbose_name='Остров')

    def __str__(self):
        return '{} + {}'.format(self.monster1.name, self.monster2.name)
