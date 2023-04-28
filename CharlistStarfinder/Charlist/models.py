from django.db import models
from django.core.validators import  MaxValueValidator

# Раса персонажа
class Race(models.Model):
    name_race = models.CharField('Класс', max_length=50)
    hit_points = models.IntegerField('Здоровье')
    size = models.IntegerField('Размер')
    subtype = models.CharField('Тип', max_length=50)
    strength = models.IntegerField('Сила', validators= (MaxValueValidator(5),))
    dex = models.IntegerField('Ловкость', validators= (MaxValueValidator(5),))
    con = models.IntegerField('Выносливость', validators= (MaxValueValidator(5),))
    intelligence = models.IntegerField('Интелект', validators= (MaxValueValidator(5),))
    wis = models.IntegerField('Мудрость', validators= (MaxValueValidator(5),))
    cha = models.IntegerField('Харизма', validators= (MaxValueValidator(5),))

    def __str__(self):
        return f"{self.name_race}"

# Класс персонажа
class Character_class(models.Model):
    name_class = models.CharField('Класс', max_length=50)
    stamina_points = models.IntegerField('Живучесть')
    hit_points = models.IntegerField('Здоровье')
    spell_class = models.TextField(max_length=1000, blank=None)
    features_class = models.TextField(max_length=1000, blank=None)

    def __str__(self):
        return f"{self.name_class}"

# Персонаж
class Character(models.Model):
    name = models.CharField('Имя', max_length=50)
    # Характеристики
    strength = models.IntegerField('Сила', validators= (MaxValueValidator(25),))
    dex = models.IntegerField('Ловкость', validators= (MaxValueValidator(25),))
    con = models.IntegerField('Выносливость', validators= (MaxValueValidator(25),))
    intelligence = models.IntegerField('Интелект', validators= (MaxValueValidator(25),))
    wis = models.IntegerField('Мудрость', validators= (MaxValueValidator(25),))
    cha = models.IntegerField('Харизма', validators= (MaxValueValidator(25),))
    rase = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='characters_as_race')
    character_class = models.ForeignKey(Character_class, on_delete=models.CASCADE, related_name='characters_as_class')
    # Здоровье и решимость
    hit_points = models.IntegerField('Здоровье', default=0, editable=False)

    def __str__(self):
        return f"{self.name}{self.strength}"

    @property
    def calculate_health(self):
        hit_points = self.rase.hit_points + self.character_class.hit_points
        return hit_points

    def save(self, *args, **kwargs):
        self.hit_points = self.calculate_health
        self.strength = self.rase.strength + self.strength
        self.dex = self.rase.dex + self.dex
        self.con = self.rase.con + self.con
        self.intelligence = self.rase.intelligence + self.intelligence
        self.wis = self.rase.wis + self.wis
        self.cha = self.rase.cha + self.cha
        super(Character, self).save(*args, **kwargs)


