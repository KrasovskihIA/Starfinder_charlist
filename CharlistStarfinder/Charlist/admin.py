from django.contrib import admin
from .models import Character, Race, CharacterClass

class ModelAdmin(admin.ModelAdmin):
    readonly_fields = ('hit_points',)

admin.site.register(Character, ModelAdmin)
admin.site.register(Race)
admin.site.register(CharacterClass)

