from django.shortcuts import render

from .models import *


def sound_detail(request, slug):
    sound = Sound.objects.get(slug=slug)
    return render(request, "dux_news/sound_app.html", {'instance': {'sound': sound}})