__author__ = 'hadrien'
import random

from django import template
from django.templatetags.static import static

from duxomusic.models import *


register = template.Library()
default_backgrounds = [static('img/forest.jpg'), static('img/crows.jpg'), static('img/cat.jpg')]
DEFAULT_COLOR = '000'
DEFAULT_SPLIT_SIZE = '480'

@register.assignment_tag()
def get_bg():
    
    bos = Background.objects.filter(active=True).all()
    color = DEFAULT_COLOR
    split = DEFAULT_SPLIT_SIZE
    
    if len(bos) == 0:
        backgrounds = default_backgrounds
    else:
        bo = bos.reverse()[0]
        images = bo.images.all()
        backgrounds = [image.image.url for image in images]
        color = bo.color
        split = bo.no_background_split
        
    background = {
        'url' : random.choice(backgrounds),
        'color' : color,
        'split_size' : split,
    }
    
    return background
    