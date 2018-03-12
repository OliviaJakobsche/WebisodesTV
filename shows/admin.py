from django.contrib import admin
from .models import Show, Episode, Genre, ShowGenre, Link

# Register your models here.
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(ShowGenre)
admin.site.register(Link)
