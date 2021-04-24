from django.db import models
from django.conf import settings


class Monster(models.Model):
    name = models.CharField(max_length=32, verbose_name='Monster name')

    image = models.ImageField(upload_to='image', null=True, verbose_name='Monster image')
    # convert to many to many, different islands different strategy
    # how_to_breed = models.CharField(max_length=512, verbose_name='Breed Strategy')

    default_time = models.DurationField(verbose_name='Default Time  to breed',
                                        default=settings.INITIAL_DEFAULT_TIME)

    advanced_time = models.DurationField(verbose_name='Advanced Time to breed',
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

    """def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s">' % escape(self.image.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True"""

    def __str__(self):
        return "{}".format(self.name)


class Island(models.Model):
    name = models.CharField(max_length=32, verbose_name='Island name')

    level = models.fields.PositiveIntegerField(verbose_name='Level')

    cost = models.fields.PositiveIntegerField(verbose_name='Cost')

    mirror_cost = models.fields.PositiveIntegerField(verbose_name='Mirror cost')

    monsters = models.ManyToManyField(to='Monster', verbose_name='Monsters')

    # uluchsheniya maybi potom
