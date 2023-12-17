"""
URL configuration for pokemon_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pokemon_app.views import HomePageView, TrainerList, CollectionList, PokemonCardList, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, PokemonCardCreateView, PokemonCardUpdateView, PokemonCardDeleteView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView
from pokemon_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('pokemoncard_list/', PokemonCardList.as_view(), name='pokemoncard-list'),
    path('trainer_list/', TrainerList.as_view(), name='trainer-list'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemoncard_list/add', PokemonCardCreateView.as_view(), name='pokemoncard-add'),
    path('pokemoncard_list/<pk>', PokemonCardUpdateView.as_view(), name='pokemoncard-update'),
    path('pokemoncard_list/<pk>/delete', PokemonCardDeleteView.as_view(), name='pokemoncard-delete'),
    path('collections/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collections/<pk>', CollectionUpdateView.as_view(), name='collection-update'),
    path('collections/<pk>/delete', CollectionDeleteView.as_view(), name='collection-delete'),
]
