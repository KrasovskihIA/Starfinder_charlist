from django.urls import path
from .views import CharacterListlView, CharacterDetailView

urlpatterns = [
    path('', CharacterListlView.as_view(), name='character_list'),
    path('character/<str:name>/', CharacterDetailView.as_view(), name='character_detail'),
]