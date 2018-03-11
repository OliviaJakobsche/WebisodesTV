from django.http import HttpResponse
from .models import Show


def index(request):
    all_shows = Show.objects.all()
    html='<h1>Lista seriali</h1>'

    for show in all_shows:
        url = '/shows/' + str(show.id) + '/'
        html += '<a href="' + url + '">' + show.title + '(' + show.release + ')</a><br>'
    return HttpResponse(html)


def detail(request, show_id):
    return HttpResponse("<h2>Serial o id: " + str(show_id) + '</h2>')


