from django.http import HttpResponse
from django.template import loader

from .models import Button


def index(request):
    light_on = Button.objects
    #[:1].get().light_on
    print("LIGHT_ON", light_on)
    template = loader.get_template('lazy_light/index.html')
    context = {
        'light_on': light_on,
    }
    return HttpResponse(template.render(context, request))

