__author__ = 'hadrien'
import random

from django import template
from django.templatetags.static import static

from duxomusic.models import *


register = template.Library()
default_backgrounds = [static('img/forest.jpg'), static('img/crows.jpg'), static('img/cat.jpg')]


@register.assignment_tag()
def get_bg():
    bos = Background.objects.filter(active=True).all()
    if len(bos) == 0:
        backgrounds = default_backgrounds
    else:
        images = bos.reverse()[0].images.all()
        backgrounds = [image.image.url for image in images]
        
    background = random.choice(backgrounds)
    return background
    