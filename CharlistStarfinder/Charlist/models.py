from django.db import models
from django.core.validators import  MaxValueValidator

# Абстрактный класс характеристик
class AbstractCharacteristics(models.Model):
    strength = models.IntegerField('Сила', validators= (MaxValueValidator(25),))
    dex = models.IntegerField('Ловкость', validators= (MaxValueValidator(25),))
    con = models.IntegerField('Выносливость', validators= (MaxValueValidator(25),))
    intelligence = models.IntegerField('Интелект', validators= (MaxValueValidator(25),))
    wis = models.IntegerField('Мудрость', validators= (MaxValueValidator(25),))
    cha = models.IntegerField('Харизма', validators= (MaxValueValidator(25),))

    class Meta:
        abstract = True

# Раса персонажа
class Race(AbstractCharacteristics):
    name_race = models.CharField('Класс', max_length=50)
    hit_points = models.IntegerField('Здоровье')
    size = models.IntegerField('Размер')
    subtype = models.CharField('Тип', max_length=50)

    def __str__(self):
        return f"{self.name_race}"


# Класс персонажа
class CharacterClass(models.Model):
    KEY_CHARACTERISKIC = [
        ('strength', 'Сила'),
        ('dex', 'Ловкость'),
        ('con', 'Выносливость'),
        ('intelligence', 'Интелект'),
        ('wis', 'Мудрость'),
        ('cha', 'Харизма'),
    ]

    name_class = models.CharField('Класс', max_length=50)
    stamina_points = models.IntegerField('Живучесть')
    hit_points = models.IntegerField('Здоровье')
    spell_class = models.TextField(max_length=1000, blank=None)
    features_class = models.TextField(max_length=1000, blank=None)
    key_characteristic = models.CharField(max_length=20, choices=KEY_CHARACTERISKIC, default='strength')

    def __str__(self):
        return f"{self.name_class}"

# Персонаж
class Character(AbstractCharacteristics):
    name = models.CharField('Имя', max_length=50)
    rase = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='characters_as_race')
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE, related_name='characters_as_class')
    # Здоровье и решимость
    hit_points = models.IntegerField('Здоровье', default=0, editable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def calculate_health(self):
        hit_points = self.rase.hit_points + self.character_class.hit_points
        return hit_points

    def save(self, *args, **kwargs):
        self.hit_points = self.calculate_health
        super(Character, self).save(*args, **kwargs)


