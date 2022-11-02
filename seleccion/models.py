from django.db import models


class Team(models.Model):
    country = models.CharField(max_length=40)
    rank = models.IntegerField()
  

    def __str__(self):
        return f"Seleccion: {self.country} | rank: {self.rank}"


class MatchGame(models.Model):
    t_local = models.CharField(max_length=40)
    t_away = models.CharField(max_length=40)
    stadium = models.CharField(max_length=40)
    date = models.DateField()
    

    def __str__(self):
        return f"{self.t_local} VS {self.t_away} {self.date}"
