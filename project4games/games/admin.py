from django.contrib import admin

from .models import Game, GameGenre

admin.site.register(Game)
admin.site.register(GameGenre)
