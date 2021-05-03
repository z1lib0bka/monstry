from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^(?P<monster_id>\d+)/$', views.monster_detail, name='monster_detail'),
    url(r'^(?P<island_slug>\w+)/$', views.list_monsters_of_the_island, name='monster_list'),
    url(r'^(?P<island_slug>\w+)/(?P<monster_id>\d+)/$', views.monster_detail, name='monster_detail'),

]
