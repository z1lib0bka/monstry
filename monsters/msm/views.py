from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView

from django_tables2 import SingleTableView

from .models import Monster
from .tables import MonsterTable

def list_monsters_of_the_island(request):
    monsters = get_list_or_404(Monster, monster_type='USUAL')

    return render(request, 'msm/island.html', {'monsters': monsters})


class MonsterListView(SingleTableView):
    table_class = MonsterTable

    queryset = Monster.objects.filter(monster_type='USUAL')

    template_name = 'msm/island.html'

    context_object_name = 'monsters'






