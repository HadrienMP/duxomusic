from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = ImageWrapper


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    
# admin.site.register(ImageWrapper)
# admin.site.register(Background)