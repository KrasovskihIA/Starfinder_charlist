# Generated by Django 4.2 on 2023-06-22 12:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Charlist', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Сила')),
                ('dex', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Ловкость')),
                ('con', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Выносливость')),
                ('intelligence', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Интеллект')),
                ('wis', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Мудрость')),
                ('cha', models.IntegerField(validators=[django.core.validators.MaxValueValidator(26)], verbose_name='Харизма')),
                ('name_theme', models.CharField(max_length=50, verbose_name='Тема персонажа')),
                ('description', models.TextField(verbose_name='Описание')),
                ('abilities', models.TextField(verbose_name='Способности')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='character',
            name='theme',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='characters_as_theme', to='Charlist.charactertheme'),
        ),
    ]