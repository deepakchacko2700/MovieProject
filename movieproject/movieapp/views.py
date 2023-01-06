from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.models import Movie
from . forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    print(movie_id, movie)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method=='POST':
        name = request.POST.get('movie_name')
        year = request.POST.get('movie_year')
        desc = request.POST.get('movie_desc')
        image = request.FILES['movie_img']
        movie = Movie(name=name, year=year, description=desc, img=image)
        movie.save()

    return render(request, 'add_movie.html')


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie':movie,
                                         'form':form})


def delete(request, movie_id):
    if request.method=='POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
