from django.contrib import admin
from . import models 
# Register your models here.

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    pass