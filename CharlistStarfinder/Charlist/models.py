from django.db import models
from django.core.validators import  MaxValueValidator
from accounts.models import Profile
from django.contrib.auth.models import User



# Генерация пути для аватара персонажа
def character_avatar_path(instance, filename):
        return f'{instance.name}/avatar/{filename}'

# Оружие
class Weapon(models.Model):
    KEY_CHARACTERISKIC = [
        ('near', 'Оружие ближнего боя'),
        ('further', 'Оружие дальнего боя'),
    ]

    name = models.CharField('Название', max_length=50)
    level = models.IntegerField('Уровень оружия', default=0, editable=True)
    price = models.IntegerField('Цена', default=0, editable=True)
    damage = models.CharField('Урон', max_length=10)
    crete = models.CharField('Крит', max_length=10)
    features = models.CharField('Особые свойства', max_length=10)
    distance = models.CharField(max_length=20, choices=KEY_CHARACTERISKIC, default='near')

    def __str__(self):
        return f"{self.name}"


# Абстрактный класс характеристик
class AbstractCharacteristics(models.Model):
    strength = models.IntegerField('Сила', validators= (MaxValueValidator(26),))
    dex = models.IntegerField('Ловкость', validators= (MaxValueValidator(26),))
    con = models.IntegerField('Выносливость', validators= (MaxValueValidator(26),))
    intelligence = models.IntegerField('Интеллект', validators= (MaxValueValidator(26),))
    wis = models.IntegerField('Мудрость', validators= (MaxValueValidator(26),))
    cha = models.IntegerField('Харизма', validators= (MaxValueValidator(26),))

    class Meta:
        abstract = True

# Раса персонажа
class Race(AbstractCharacteristics):
    name_race = models.CharField('Название расы', max_length=50)
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
        ('intelligence', 'Интеллект'),
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


# Тема персонажа
class CharacterTheme(AbstractCharacteristics):
    name_theme = models.CharField('Тема персонажа', max_length=50)
    description = models.TextField('Описание')
    abilities = models.TextField('Способности')

    def __str__(self):
        return f"{self.name_theme}"


# Персонаж
class Character(AbstractCharacteristics):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters_as_author')
    name = models.CharField('Имя', max_length=50)
    avatar = models.ImageField(upload_to=character_avatar_path, blank=True)
    rase = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='characters_as_race')
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE, related_name='characters_as_class')
    theme = models.ForeignKey(CharacterTheme, on_delete=models.CASCADE, related_name='characters_as_theme', default=None)
    # Здоровье и решимость
    hit_points = models.IntegerField('Здоровье', default=0, editable=True)
    # Оружие и одежда
    cha_weapon = models.ManyToManyField(Weapon, related_name='characters_weapon')
    # Модификаторы характеристик
    strength_modifier = models.IntegerField('Модификатор силы', default=0, editable=True)
    dex_modifier = models.IntegerField('Модификатор ловкости', default=0, editable=True)
    con_modifier = models.IntegerField('Модификатор выносливости', default=0, editable=True)
    intelligence_modifier = models.IntegerField('Модификатор интеллекта', default=0, editable=True)
    wis_modifier = models.IntegerField('Модификатор мудрости', default=0, editable=True)
    cha_modifier = models.IntegerField('Модификатор харизмы', default=0, editable=True)

    def __str__(self):
        return f"{self.name}"

    # Калькулятор модификатора
    def calculate_modifiers(self):
        fields = [field for field in self._meta.get_fields() if not field.name.endswith('_modifier')]
        modifier = {0:-5, 1: -5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:+1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8}
        for field in fields:
            if isinstance(field, models.IntegerField) and field.name != 'id' and field.name != 'hit_points':
                field_value = getattr(self, field.name)
                race_field_value = getattr(self.rase, field.name)
                theme_field_value = getattr(self.theme, field.name)
                setattr(self, f'{field.name}_modifier', modifier[field_value + race_field_value + theme_field_value])
        
    # Рассчет пунктов здоровья
    @property
    def calculate_health(self):
        hit_points = self.rase.hit_points + self.character_class.hit_points
        return hit_points

    def save(self, *args, **kwargs):
        self.calculate_modifiers()
        self.hit_points = self.calculate_health
        super().save(*args, **kwargs)


