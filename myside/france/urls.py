from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='france'),
    path('/scenes', views.scenes, name='scenes'),
    path('/add-scenes', views.add_scenes, name='add-scenes'),
    path('/add-dialog', views.add_dialog, name='add-dialog'),
]