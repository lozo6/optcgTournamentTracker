from django import forms
from .models import Tournament

# Create your forms here
class TournamentForm(forms.ModelForm):
    class Meta: # meta data
        model = Tournament
        fields = ['date_of_event', 'tournament_owner', 'leader', 'decklist']
