from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='france'),
    path('scenes', views.scenes, name='scenes'),
    path('add-scenes', views.add_scenes, name='add-scenes'),
    path('edit-scenes/<int:scene_id>', views.edit_scenes, name='edit-scenes'),
    path('dialog/<int:id>', views.dialog, name='dialog'),
    path('edit-dialog/<int:id>/<int:phrase>/<str:mode>', views.edit_dialog, name='edit-dialog'),
    path('edit-phrase/<int:scene_pk>', views.add_phrase, name='add-phrase'),
    path('edit-phrase/<int:scene_pk>/<int:phrase_order>', views.edit_phrase, name='edit-phrase'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('add-word/<int:scene_pk>', views.add_word, name='add-word'),
    path('edit-word/<int:word_id>', views.edit_word, name='edit-word'),
    path('delete-word/<int:word_id>', views.delete_word, name='delete-word'),
]