from django.urls import path

from . import views

app_name = 'lazy_light'
urlpatterns = [
    path('', views.index, name='index'),
    path('toggleLight', views.toggleLight, name='toggleLight'),
]