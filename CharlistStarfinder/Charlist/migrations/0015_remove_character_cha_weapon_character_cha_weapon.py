# Generated by Django 4.2 on 2023-07-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Charlist', '0014_alter_character_cha_weapon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='cha_weapon',
        ),
        migrations.AddField(
            model_name='character',
            name='cha_weapon',
            field=models.ManyToManyField(related_name='characters_weapon', to='Charlist.weapon'),
        ),
    ]
