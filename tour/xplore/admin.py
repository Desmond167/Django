from django.contrib import admin
from .models import xplore


class XploreAdmin(admin.ModelAdmin):
    list_display = ("user","mail","loc")


# Register your models here.
admin.site.register(xplore, XploreAdmin)