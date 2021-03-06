from django.shortcuts import render
from django.core.paginator import Paginator
from player.models import Films


def index(request):
    return render(request, 'Player/playerPage.html')


def films(request, page_number=1):
    search = request.GET.get("search", "")
    if search:
        all_films = Films.objects.filter(normalized_title__icontains=search.upper())
    else:
        all_films = Films.objects.all()
    current_page = Paginator(all_films, 10)
    return render(request, "Player/films.html", {"films": current_page.page(page_number)})


def film(request, film_id):
    current_film = Films.objects.get(pk=film_id)
    return render(request, "Player/film.html", {"film": current_film})
