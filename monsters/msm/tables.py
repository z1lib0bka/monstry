import django_tables2 as tables
from .models import Monster


class MonsterTable(tables.Table):
    class Meta:
        model = Monster
        template_name = 'django_tables2/bootstrap.html'
        fields = ("name", "image", "default_time", "advanced_time",)

