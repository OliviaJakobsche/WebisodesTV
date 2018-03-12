from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from .models import Show, Episode


def index(request):
    all_shows = Show.objects.all()
    context = {'all_shows': all_shows, }
    return render(request, 'shows/index.html', context)


def detail(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    episodes = Episode.objects.filter(show=show_id).order_by('season_nr', 'episode_nr')
    seasons = episodes.aggregate(max_season=Max('season_nr'))
    season_nr = seasons['max_season']

    context = {'show': show, 'episodes': episodes, 'max_season': range(1, season_nr+1), }
    return render(request, 'shows/detail.html', context)
