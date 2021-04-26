from django.contrib import admin

from .models import Monster, Island, BreedingStrategy
from .forms import MonsterForm


@admin.register(Monster)
class MonsterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'default_time', 'advanced_time', 'monster_type']

    ordering = ['name']

    filter_horizontal = ['how_to_breed']

    form = MonsterForm


@admin.register(Island)
class IslandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']

    filter_horizontal = ['monsters']

    ordering = ['name']


@admin.register(BreedingStrategy)
class BreedingStrategyModelAdmin(admin.ModelAdmin):
    list_display = ['monster1', 'monster2', 'result_monster']
