from django.urls import path
from .views import ArtileListView, ArtileDetailView

urlpatterns = [
    path('',ArtileListView.as_view()),
    path('<pk>',ArtileDetailView.as_view())
]