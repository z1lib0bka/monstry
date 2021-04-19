from django.contrib import admin

from .models import *


@admin.register(Monster)
class MonsterModelAdmin(admin.ModelAdmin):
    list_display = ['name']

    ordering = ['name']


@admin.register(Island)
class IslandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']

    filter_horizontal = ['monsters']

    ordering = ['name']
