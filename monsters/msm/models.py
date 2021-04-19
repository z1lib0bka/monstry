from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=32, verbose_name='Monster name')

    # image = models.ImageField()
    # convert ot many to many, different islands different strategy
    # how_to_breed = models.CharField(max_length=512, verbose_name='Breed Strategy')

    # time = models.CharField(max_length=32, verbose_name='Time')

    buy_cost = models.IntegerField(verbose_name='Buy cost')

    sell_cost = models.IntegerField(verbose_name='Sell cost')

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
