from django.db import models
from django.conf import settings


class Monster(models.Model):
    name = models.CharField(max_length=32, verbose_name='Monster name')

    # image = models.ImageField()
    # convert to many to many, different islands different strategy
    # how_to_breed = models.CharField(max_length=512, verbose_name='Breed Strategy')

    default_time = models.DurationField(verbose_name='Default Time to breed',
                                        default=settings.INITIAL_DEFAULT_TIME)

    advanced_time = models.DurationField(verbose_name='Advanced Time to breed',
                                         default=settings.INITIAL_ADVANCED_TIME)

    buy_cost = models.fields.PositiveIntegerField(verbose_name='Buy cost')

    sell_cost = models.fields.PositiveIntegerField(verbose_name='Sell cost')

    # make islands
    # food (???) maybi potom

    def __str__(self):
        return "{}".format(self.name)


class Island(models.Model):
    name = models.CharField(max_length=32, verbose_name='Island name')

    level = models.IntegerField(verbose_name='Level')

    cost = models.IntegerField(verbose_name='Cost')

    mirror_cost = models.IntegerField(verbose_name='Mirror cost')

    monsters = models.ManyToManyField(to='Monster', verbose_name='Monsters')

    # uluchsheniya maybi potom
