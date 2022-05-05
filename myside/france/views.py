from django.shortcuts import render

# Create your views here.

def home(request):

    context = {}

    return render(request, 'france/home.html', context)

def scenes(request):

    context = {}

    return render(request, 'france/scenes.html', context)

def add_scenes(request):

    context = {}

    return render(request, 'france/add_scenes.html', context)

def add_dialog(request):

    context = {}

    return render(request, 'france/add_dialog.html', context)