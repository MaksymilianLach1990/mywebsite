from django.shortcuts import render

# Create your views here.

def space(request):

    context = {}

    return render(request, 'space/space.html', context)