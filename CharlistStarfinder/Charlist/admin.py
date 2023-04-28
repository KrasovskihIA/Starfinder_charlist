from django.contrib import admin
from .models import Character, Race, Character_class

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Character_class)

class YourModelAdmin(admin.ModelAdmin):
    readonly_fields = ('hit_points',)