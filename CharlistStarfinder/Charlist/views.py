from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Character, CharacterClass, Race
from .forms import CharacterForm
from django.urls import reverse_lazy
from django.utils.text import slugify

# Отображение персонажей
class CharacterListlView(ListView):
    model = Character
    template_name = 'Charlist/Charlist.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        return self.model.objects.all()

# Детальное представление персонажей
class CharacterDetailView(DetailView):
    model = Character
    template_name = 'Charlist/character_detail.html'
    context_object_name = 'character'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_object(self, queryset=None):
        name = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(self.model, **{self.slug_field: name})

# Создание персонажей 
class CharacterCreateView(CreateView):
    form_class = CharacterForm
    template_name = 'Charlist/character_create.html'
    success_url = reverse_lazy('character_list')
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context['character_was_created'] = True  
            context['form'] = self.form_class         
        else:
            context['character_was_created_with_errors'] = True
            context['form'] = form
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('character_list')



    