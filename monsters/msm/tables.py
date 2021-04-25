import django_tables2 as tables
from django.utils.html import format_html

from .models import Monster


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            '<img src="../media/{url}" height="50px", width="50px">',
            url=value
        )


class MonsterTable(tables.Table):
    image = ImageColumn()

    class Meta:
        model = Monster

        template_name = 'django_tables2/bootstrap4.html'

        orderable = False

        fields = ("name", "image", "default_time", "advanced_time",)

        order_by = ("name",)

        attrs = {'class': 'table table-hover',
                 'thead': {
                     'class': 'thead-light',
                 },
                 }
