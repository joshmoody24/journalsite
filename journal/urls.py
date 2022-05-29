from django.urls import path
from .views import indexPageView, entryPageView, tagPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("entry/<str:date>/", entryPageView, name="entry"),
    path("tag/<str:tag>/", tagPageView, name="tag"),
]                  

