from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    release = models.DateField()
    series_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + '(' + self.description + ')'


class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    season_nr = models.IntegerField(default=None)
    episode_nr = models.IntegerField(default=None)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, null=True, blank=True)
    release = models.DateField()
    file_type = models.CharField(max_length=10)


class Genre(models.Model):
    name = models.CharField(max_length=50)


class ShowGenre(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Link(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)


