from django.shortcuts import render, redirect
from .forms import ScenesCreateForm, PhraseCreateForm, WorldCreateForm
from .models import Scenes, Phrase, World

# Create your views here.

def home(request):

    scenes_list = Scenes.objects.all()

    context = {'scenes_list': scenes_list}

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
            scene_id = Scenes.objects.filter(name=request.POST['name']).first()
            print(scene_id.id)
            return redirect(f'/france/dialog/{scene_id.id}')
        else:
            return redirect("/france/add-scenes")

    context = {
        'form': ScenesCreateForm,
        }
    return render(request, 'france/add_scenes.html', context)

def dictionary(request):

    if request.method == 'POST':
        form = WorldCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/france/dictionary')
    context = {
        'form': WorldCreateForm,
        'dictionary': World.objects.all(),
        }

    return render(request, 'france/dictionary.html', context)

def dialog(request, id):
    
    situation = Scenes.objects.get(id=id)
    dialog_list = Phrase.objects.filter(scenes=id).order_by('order')

    context = {
        'dialog_list': dialog_list,
        'situation': situation,
        }

    return render(request, 'france/dialog.html', context)

def edit_dialog(request, id, phrase, mode):

    if mode == 'delete-phrase':
        delete_phrase = Phrase.objects.filter(id=phrase).first()
        delete_phrase.delete()

        return redirect(f'/france/edit-dialog/{id}/0/edit')

    


    if request.method == 'POST':
        form = PhraseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(f'/france/edit-dialog/{id}')


    situation = Scenes.objects.get(id=id)
    dialog_list = Phrase.objects.filter(scenes=id).order_by('order')

    context = {
        'dialog_list': dialog_list,
        'situation': situation,
        'form': PhraseCreateForm,
        }

    return render(request, 'france/edit_dialog.html', context)