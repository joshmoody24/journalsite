from django.urls import path
from .views import indexPageView, entryPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("entry/<str:date>/", entryPageView, name="entry"),
]                  

