import os

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from .models import Pokemon
from .forms import PokemonForm
from .Model.PokemonModel import PokemonModel
from .Model.PokemonData import Pokedex
from .Utils.DataTools import DataSaver
        
def predict_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
        # predicting the pokemon from the image
        prediction_model = PokemonModel()
        prediction = prediction_model.computePrediction(os.path.join(settings.MEDIA_ROOT, "images", "pokemon.jpg"))
        
        pokedex = Pokedex()
        pokedex.autoInitialize()
        
        pokemonData = pokedex.m_data[f"{prediction[0]}"]
        
        context = pokemonData
        
        # Delete all pokemon object from table
        Pokemon.objects.all().delete()
        
        return render(request, 'pokemon.html', context)
    else:
        form = PokemonForm()
        context = {
            'form':form,
        }
        
    return render(request, 'upload.html', context)
    