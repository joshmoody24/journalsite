from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def indexPageView(request):
    entries = Entry.objects.all()
    context = {"journal_entries": entries}
    return render(request, "index.html", context)
