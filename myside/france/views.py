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
######################
def edit_dialog(request, id, phrase, mode):

    if phrase == 0 and mode == 'delete-scene':
        delete_scene = Scenes.objects.filter(id=id).first()
        delete_scene.delete()

        return redirect('/france/scenes')

    if mode == 'delete-phrase':
        delete_phrase = Phrase.objects.filter(id=phrase).first()
        delete_phrase.delete()

        return redirect(f'/france/edit-dialog/{id}/0/edit')

    if mode == 'order-up':
        if phrase == 1:
            return redirect(f'/france/edit-dialog/{id}/0/edit')

        Phrase().go_up(phrase, id)
        
        return redirect(f'/france/edit-dialog/{id}/0/edit')

    if mode == 'order-down':
        if phrase == max([phrase.order for phrase in Phrase.objects.filter(scenes=id).all()]):
            return redirect(f'/france/edit-dialog/{id}/0/edit')

        Phrase().go_down(phrase, id)

        return redirect(f'/france/edit-dialog/{id}/0/edit')

    if mode == 'edit':

        test = "Message"

        situation = Scenes.objects.get(id=id)
        dialog_list = Phrase.objects.filter(scenes=id).order_by('order')

        context = {
            'dialog_list': dialog_list,
            'situation': situation,
            'test': test,
            }

        return render(request, 'france/edit_dialog.html', context)

    else:
        return redirect('/france/')
##############################

def add_phrase(request, scene_pk):


    if request.method == 'POST':
        scene = Scenes.objects.get(id=scene_pk)
        name = request.POST['character_name']
        sentence = request.POST['sentence']

        phrases = Phrase.objects.filter(scenes=scene_pk).all()

        if len(phrases) == 0:
            order_num = 1
        else:
            order_max = [phrase.order for phrase in phrases]
            order_num = max(order_max)

        form = Phrase(scenes=scene, character_name=name, sentence=sentence, order=order_num)
        
        form.save()

        return redirect(f'/france/edit-dialog/{scene_pk}/0/edit')

    context = {
        'title': 'Dodaj wypowiedź',
        'form': PhraseCreateForm,
        }
    return render(request, 'france/edit_phrase.html', context)


def edit_phrase(request, scene_pk, phrase_order):

    phrase = Phrase.objects.get(scenes=scene_pk, order=phrase_order)

    if request.method == 'POST':
        phrase.character_name = request.POST['character_name']
        phrase.sentence = request.POST['sentence']

        phrase.save()

        return redirect(f'/france/edit-dialog/{scene_pk}/0/edit')
        

    context = {
        'title': 'Edytuj wypowiedź',
        'form': PhraseCreateForm(instance=phrase),
        }
    return render(request, 'france/edit_phrase.html', context)