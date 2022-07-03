from django.urls import path
from .views import VideosViews

urlpatterns = [
    path("list/", VideosViews.as_view()),
]
