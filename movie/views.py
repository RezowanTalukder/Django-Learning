from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieList(ListView):
    model  = Movie
    #template_name = ''
    
class MovieDetails(DetailView):
    model = Movie
    #template_name = ''