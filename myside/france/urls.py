from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='france'),
    path('scenes', views.scenes, name='scenes'),
    path('add-scenes', views.add_scenes, name='add-scenes'),
    path('dialog/<int:id>', views.dialog, name='dialog'),
    path('edit-dialog/<int:id>/<int:phrase>/<str:mode>', views.edit_dialog, name='edit-dialog'),
    path('edit-phrase/<int:scene_pk>', views.add_phrase, name='add-phrase'),
    path('edit-phrase/<int:scene_pk>/<int:phrase_order>', views.edit_phrase, name='edit-phrase'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('add-world/<int:scene_pk>', views.add_world, name='add-world'),
    path('edit-world/<int:world_id>', views.edit_world, name='edit-world'),
    path('delete-world/<int:world_id>', views.delete_world, name='delete-world'),
]