from django.urls import path
from .views import CharacterListlView

urlpatterns = [
    path('', CharacterListlView.as_view(), name='character_list'),
]