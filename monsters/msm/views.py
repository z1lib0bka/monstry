from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from django_tables2 import SingleTableView

from .models import Monster
from .tables import MonsterTable


def list_monsters_of_the_island(request):
    usual_table = MonsterTable(Monster.objects.filter(monster_type='USUAL'))

    rare_table = MonsterTable(Monster.objects.filter(monster_type='RARE'))

    epic_table = MonsterTable(Monster.objects.filter(monster_type='EPIC'))

    return render(request, 'msm/island.html', {'usual_monsters': usual_table,
                                               'rare_monsters': rare_table,
                                               'epic_monsters': epic_table,
                                               })


class MonsterListView(SingleTableView):
    table_class = MonsterTable

    queryset = Monster.objects.filter(monster_type='USUAL')

    table_data = queryset

    template_name = 'msm/island.html'

    context_object_name = 'monsters'


def monster_detail(request, monster_id):
    monster = get_object_or_404(Monster, id=monster_id)

    return render(request, 'msm/monster_detail.html', {'monster': monster})



