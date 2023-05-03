from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Character, CharacterClass, Race

class CharacterListlView(ListView):
    model = Character
    template_name = 'Charlist/Charlist.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        return self.model.objects.all()


    