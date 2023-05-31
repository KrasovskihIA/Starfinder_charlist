from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'rase', 'character_class', 'strength', 'dex', 'con', 'intelligence', 'wis', 'cha' ]
        labels = {
                'name': 'Введите Имя',
                'rase': 'Выберите расу',
                'character_class': 'Выберите класс',
                'strength': 'Сила',
                'dex': 'Ловкость',
                'con': 'Выносливость',
                'intelligence': 'Интеллект',
                'wis': 'Мудрость',
                'cha': 'Харизма',
            }
        widgets = {
                'name': forms.Textarea(attrs={
                    'class':'form-control', 
                    'placeholder':'Имя персонажа'
                    }),
                'strength': forms.NumberInput(attrs={'max': 26}),
                'dex': forms.NumberInput(attrs={'max': 26}),
                'con': forms.NumberInput(attrs={'max': 26}),
                'intelligence': forms.NumberInput(attrs={'max': 26}),
                'wis': forms.NumberInput(attrs={'max': 26}),
                'cha': forms.NumberInput(attrs={'max': 26}),
            }
    
 