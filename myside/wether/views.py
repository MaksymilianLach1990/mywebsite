from django.shortcuts import render

# Create your views here.

def wether(request):
    context = {}
    return render(request, 'wether/wether.html', context)