from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Character, CharacterClass, Race


class CharacterListlView(ListView):
    model = Character
    template_name = 'Charlist/Charlist.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        return self.model.objects.all()
    
class CharacterDetailView(DetailView):
    model = Character
    template_name = 'Charlist/character_detail.html'
    context_object_name = 'character'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_object(self, queryset=None):
        name = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(self.model, **{self.slug_field: name})


    