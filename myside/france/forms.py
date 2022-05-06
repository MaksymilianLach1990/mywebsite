from django import forms
from .models import Scenes, Phrase, World

class ScenesCreateForm(forms.ModelForm):
    class Meta:
        model = Scenes
        fields = ('name', 'description')


class PhraseCreateForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ('character_name', 'sentence')


class WorldCreateForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ('scenes', 'world_pl', 'world_fr', 'description', 'phonetic')