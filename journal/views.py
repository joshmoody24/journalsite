from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def indexPageView(request):
    entries = Entry.objects.filter(public=True).order_by('-date')
    context = {"journal_entries": entries}
    return render(request, "index.html", context)

def entryPageView(request, date):
    entry = Entry.objects.get(date=date)
    context = {"journal_entries": [entry]}
    return render(request, "index.html", context)
