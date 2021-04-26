from django import forms
from django.conf import settings
from durationwidget.widgets import TimeDurationWidget

from .models import Monster, BreedingStrategy


class MonsterForm(forms.ModelForm):
    image = forms.ClearableFileInput()

    default_time = forms.DurationField(widget=TimeDurationWidget(),
                                       required=True,
                                       initial=settings.INITIAL_DEFAULT_TIME,
                                       )

    advanced_time = forms.DurationField(widget=TimeDurationWidget(),
                                        required=True,
                                        initial=settings.INITIAL_ADVANCED_TIME,
                                        )

    class Meta:
        model = Monster

        fields = ['name', 'monster_type', 'image', 'default_time',
                  'advanced_time', 'buy_cost', 'sell_cost', 'how_to_breed']
