from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from pokemon_app.models import PokemonCard, Trainer, Collection
from pokemon_app.forms import TrainerForm, PokemonCardForm, CollectionForm
import json


from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer_list'
    template_name = 'trainers.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection_list'
    template_name = 'collections.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = 'pokemon-card.html'
    json_file_path = '/home/MelJoseph/django-pokemon/pokemon_project/pokemon_app/data/pokemon_data.json'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context

    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])

# trainer crud
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')

# pokemon-card crud
class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_add.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_edit.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon-card_del.html'
    success_url = reverse_lazy('pokemoncard-list')

# collection crud

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_add.html'
    success_url = reverse_lazy('collection-list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_edit.html'
    success_url = reverse_lazy('collection-list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collections_del.html'
    success_url = reverse_lazy('collection-list')
