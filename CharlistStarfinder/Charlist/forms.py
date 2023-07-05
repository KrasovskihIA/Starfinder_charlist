from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['avatar', 'name', 'rase', 'character_class', 'theme', 'cha_weapon', 'strength', 'dex', 'con', 'intelligence', 'wis', 'cha' ]
        labels = {
                'avatar' : 'Загрузите изображение ',
                'name': 'Введите Имя',
                'rase': 'Выберите расу',
                'character_class': 'Класс персонажа',
                'theme' : 'Тема персонажа' ,
                'cha_weapon': 'Оружие',
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
                'avatar': forms.ClearableFileInput(attrs={
                    'class': 'form-control-file',
                    'type': 'file'
                })
            }
    
 