from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie

# Create your views here.


class MovieView(ListView):
    model = Movie
    template_name = 'movie/movies.html'
    context_object_name = 'movies'
    queryset = Movie.objects.prefetch_related('cast').all()


