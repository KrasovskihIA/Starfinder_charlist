from django.db import models
from django.contrib.auth.models import User


# Класс профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_data = models.DateField('Дата регистрации', blank=False, auto_now_add=True, null=False)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.username}'
