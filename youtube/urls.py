from django.urls import path
from .views import VideosViews, SingleVideos

urlpatterns = [
    path("list/", VideosViews.as_view()),
    path("list/<int:id>/", SingleVideos.as_view()),
]
