from django.shortcuts import render, get_object_or_404


from .models import Monster, Island
from .tables import MonsterTable, BreedingStrategiesTable


def search_results(request):
    if request.method == 'POST':
        searched = str(request.POST['searched'])
        # Note: you should remove capitalize method when using different DB, rather then SQLite.
        monster_search_results = Monster.objects.filter(name__contains=searched.capitalize())

        return render(request, 'msm/search_results.html', {'searched': searched,
                                                           'search_results': monster_search_results})
    else:
        return render(request, 'msm/search_results.html', {})


def list_monsters_of_the_island(request, island_slug):
    island = Island.objects.get(slug=island_slug)

    usual_table = MonsterTable(island.monsters.filter(monster_type='USUAL'))

    rare_table = MonsterTable(island.monsters.filter(monster_type='RARE'))

    epic_table = MonsterTable(island.monsters.filter(monster_type='EPIC'))

    return render(request, 'msm/island.html', {'usual_monsters': usual_table,
                                               'rare_monsters': rare_table,
                                               'epic_monsters': epic_table,
                                               'island': island,
                                               })


def monster_detail(request, monster_id, island_slug=None):
    monster = get_object_or_404(Monster, id=monster_id)

    breeding_strategies = BreedingStrategiesTable(monster.how_to_breed.all())

    if breeding_strategies.rows.__len__() == 0:
        breeding_strategies = None

    return render(request, 'msm/monster_detail.html', {'monster': monster,
                                                       'breeding_strats': breeding_strategies,
                                                       'island_slug': island_slug,
                                                       })



