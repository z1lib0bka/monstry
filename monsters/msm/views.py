from django.shortcuts import render, get_object_or_404

from django_tables2 import SingleTableView

from .models import Monster, Island
from .tables import MonsterTable, BreedingStrategiesTable


def list_monsters_of_the_island(request, island_slug):
    island = Island.objects.get(slug=island_slug)

    usual_table = MonsterTable(island.monsters.filter(monster_type='USUAL'))

    rare_table = MonsterTable(island.monsters.filter(monster_type='RARE'))

    epic_table = MonsterTable(island.monsters.filter(monster_type='EPIC'))

    return render(request, 'msm/island.html', {'usual_monsters': usual_table,
                                               'rare_monsters': rare_table,
                                               'epic_monsters': epic_table,
                                               'island_slug': island_slug,
                                               })


class MonsterListView(SingleTableView):
    table_class = MonsterTable

    queryset = Monster.objects.filter(monster_type='USUAL')

    table_data = queryset

    template_name = 'msm/island.html'

    context_object_name = 'monsters'


def monster_detail(request, monster_id, island_slug=None):
    monster = get_object_or_404(Monster, id=monster_id)

    breeding_strategies = BreedingStrategiesTable(monster.how_to_breed.all())

    return render(request, 'msm/monster_detail.html', {'monster': monster,
                                                       'breeding_strats': breeding_strategies,
                                                       })



