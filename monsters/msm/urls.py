from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.ProblemListView.as_view(), name='problem_list'),
    path('', views.list_monsters_of_the_island),
    url(r'^(?P<monster_id>\d+)', views.monster_detail, name='monster_detail'),
]
