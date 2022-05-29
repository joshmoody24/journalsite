from django.urls import path
from .views import indexPageView, entryPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("entries/<str:date>/", entryPageView, name="entry"),
]                  

