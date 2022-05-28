from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def indexPageView(request):
    entries = Entry.objects.filter(public=True)
    context = {"journal_entries": entries}
    return render(request, "index.html", context)
