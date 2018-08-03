from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Game


class IndexView(generic.ListView):
    model = Game


class DetailView(generic.DetailView):
    model = Game


class GameCreate(CreateView):
    model = Game
    fields = ['name', 'description', 'source_link', 'play_link', 'genre']
    labels = {
        'name':'Game Name',
        'description':'Description',
        'source_link':'Source URL',
        'play_link':'Play URL',
        'genre':'Game Genre'
    }
    template_name_suffix = '_create_form'


class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'description', 'source_link', 'play_link', 'genre']
    labels = {
        'name':'Game Name',
        'description':'Description',
        'source_link':'Source URL',
        'play_link':'Play URL',
        'genre':'Game Genre'
    }
    template_name_suffix = '_update_form'


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('games:game-list')
