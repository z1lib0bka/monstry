import django_tables2 as tables
from .models import Monster


class MonsterTable(tables.Table):
    # name = tables.Column(verbose_name='Name')

    class Meta:
        model = Monster

        template_name = 'django_tables2/bootstrap4.html'

        fields = ("name", "image", "default_time", "advanced_time",)

        order_by = ("name",)

        attrs = {'class': 'table table-sm',
                 'thead': {
                     'class': 'thead-light',
                 }
        }
