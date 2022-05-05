from django import forms
from .models import Scenes, Phrase

class ScenesCreateForm(forms.ModelForm):
    class Meta:
        model = Scenes
        fields = ('name', 'description')


class PhraseCreateForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ('scenes', 'character_name', 'sentence', 'order')