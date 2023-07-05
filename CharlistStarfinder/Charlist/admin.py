from django.contrib import admin
from .models import Character, Race, CharacterClass, CharacterTheme, Weapon

class ModelAdmin(admin.ModelAdmin):
    readonly_fields = ('hit_points', 'dex_modifier', 'strength_modifier', 'con_modifier', 'intelligence_modifier', 'wis_modifier', 'cha_modifier')

admin.site.register(Character, ModelAdmin)
admin.site.register(Race)
admin.site.register(CharacterClass)
admin.site.register(CharacterTheme)
admin.site.register(Weapon)

