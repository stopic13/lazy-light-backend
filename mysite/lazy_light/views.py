from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from .models import Button


def index(request):
    button = get_object_or_404(Button)
    #[:1].get().light_on
    light_on = button.light_on
    print("LIGHT_ON", light_on)
    return render(request, 'lazy_light/index.html', {'light_on': light_on})

def toggleLight(request):
    # Get your button instance here
    button = get_object_or_404(Button)
    button.light_on = not button.light_on
    button.save()
   # light_on = get_object_or_404(Button).light_on

    return redirect('lazy_light:index')
