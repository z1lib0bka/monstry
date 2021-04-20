from django import forms
from django.conf import settings
from durationwidget.widgets import TimeDurationWidget

from .models import Monster


class MonsterForm(forms.ModelForm):
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

        fields = ['name', 'default_time', 'advanced_time', 'buy_cost', 'sell_cost']