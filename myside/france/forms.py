from django import forms
from .models import Scenes, Phrase, Word

class ScenesCreateForm(forms.ModelForm):
    class Meta:
        model = Scenes
        fields = ('name', 'description')


class PhraseCreateForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ('character_name', 'sentence')


class WordCreateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('scenes', 'word_pl', 'word_fr', 'description', 'phonetic')