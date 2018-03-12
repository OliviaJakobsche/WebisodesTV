from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    release = models.CharField(max_length=4)
    series_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    season_nr = models.IntegerField(default=None)
    episode_nr = models.IntegerField(default=None)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    release = models.DateField()
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.show.title + ' S' + str(self.season_nr) + 'E' + str(self.episode_nr) + ' - ' + self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ShowGenre(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.show.title + ', ' +  self.genre.name


class Link(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url



