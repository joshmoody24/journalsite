from django.contrib import admin
from .models import *


class EntryAdmin(admin.ModelAdmin):
    fields = ('date', 'title', 'content', 'tags', 'public')
    ordering = ('-date',)

# Register your models here.
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
