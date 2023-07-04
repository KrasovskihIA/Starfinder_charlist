from django.urls import path
from django.views.generic import TemplateView
from .views import CharacterListlView, CharacterDetailView, CharacterCreateView, CharacterEditView, CharacterDeleteView


urlpatterns = [
    path('', CharacterListlView.as_view(), name='character_list'),
    path(f'character/<str:name>/', CharacterDetailView.as_view(), name='character_detail'),
    path('create/', CharacterCreateView.as_view(), name ='character_create'),
    path('character/<str:name>/edit', CharacterEditView.as_view(), name='character_edit'),
    path('character/<str:name>/delete', CharacterDeleteView.as_view(), name='character_delete'),
    
]