from django.contrib import admin
from .models import Scenes, Phrase

# Register your models here.

@admin.register(Scenes)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'created_at')
    list_display = ('name', 'created_at')
    ordering = ('name', 'created_at')


@admin.register(Phrase)
class EventAdmin(admin.ModelAdmin):
    fields = ('scenes', 'character_name', 'sentence', 'order', 'created_at')
    list_display = ('scenes', 'order', 'created_at')
    ordering = ('scenes', 'created_at')