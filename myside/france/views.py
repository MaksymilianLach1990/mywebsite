from django.shortcuts import render, redirect
from .forms import ScenesCreateForm, PhraseCreateForm
from .models import Scenes, Phrase

# Create your views here.

def home(request):

    context = {}

    return render(request, 'france/home.html', context)

def scenes(request):

    scenes_list = Scenes.objects.all()

    context = {
        'scenes_list': scenes_list,
        'message': 'Nie ma scenek!',
        }

    return render(request, 'france/scenes.html', context)

def add_scenes(request):

    if request.method == 'POST':
        form = ScenesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/france/add-dialog/<str:form.name>')
        else:
            return redirect("/france/add-scenes")

    context = {
        'form': ScenesCreateForm,
        }
    return render(request, 'france/add_scenes.html', context)

def add_dialog(request):

    if request.method == 'POST':
        form = PhraseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/france/add-dialog')
    context = {
        'form': PhraseCreateForm,
        }

    return render(request, 'france/add_dialog.html', context)

def dialog(request, id):
    
    if request.method == 'POST':
        form = PhraseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(f'/france/dialog/{id}')

    situation = Scenes.objects.get(id=id)
    dialog_list = Phrase.objects.filter(scenes=id).order_by('order')

    context = {
        'dialog_list': dialog_list,
        'situation': situation,
        'form': PhraseCreateForm,
        }

    return render(request, 'france/dialog.html', context)