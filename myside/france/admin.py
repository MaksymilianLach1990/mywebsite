from django.contrib import admin
from .models import Scenes, Phrase, World

# Register your models here.

@admin.register(Scenes)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'created_at')
    list_display = ('name', 'description', 'created_at')
    ordering = ('name', 'created_at')


@admin.register(Phrase)
class EventAdmin(admin.ModelAdmin):
    fields = ('scenes', 'character_name', 'sentence', 'order', 'created_at')
    list_display = ('scenes', 'character_name', 'sentence', 'order', 'created_at')
    ordering = ('scenes', 'created_at')


@admin.register(World)
class EventAdmin(admin.ModelAdmin):
    fields = ('scenes', 'world_pl', 'world_fr', 'description', 'phonetic')
    list_display = ('world_pl', 'world_fr', 'description', 'phonetic')
    ordering = ('world_pl', 'world_fr')