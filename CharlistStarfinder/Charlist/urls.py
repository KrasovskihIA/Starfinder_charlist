from django.urls import path
from .views import CharacterListlView, CharacterDetailView, CharacterCreateView


urlpatterns = [
    path('', CharacterListlView.as_view(), name='character_list'),
    path(f'character/<str:name>/', CharacterDetailView.as_view(), name='character_detail'),
    path('create/', CharacterCreateView.as_view(), name ='character_create'),
]