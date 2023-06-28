from django.urls import path
from .views import CharacterListlView, CharacterDetailView, CharacterCreateView, CharacterEditView


urlpatterns = [
    path('', CharacterListlView.as_view(), name='character_list'),
    path(f'character/<str:name>/', CharacterDetailView.as_view(), name='character_detail'),
    path('create/', CharacterCreateView.as_view(), name ='character_create'),
    path('character/<str:name>/edit', CharacterEditView.as_view(), name='character_edit'),
]