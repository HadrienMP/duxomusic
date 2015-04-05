__author__ = 'hadrien'
import random

from django import template


register = template.Library()
backgrounds = ['forest.jpg', 'crows.jpg', 'cat.jpg']


@register.assignment_tag()
def get_bg():
    return random.choice(backgrounds)