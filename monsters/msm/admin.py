from django.contrib import admin

from .models import Monster, Island
from .forms import MonsterForm


@admin.register(Monster)
class MonsterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'default_time', 'advanced_time']

    ordering = ['name']

    form = MonsterForm


@admin.register(Island)
class IslandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']

    filter_horizontal = ['monsters']

    ordering = ['name']
