from django.db import models

# Create your models here.
class Tournament(models.Model):
    date_of_event = models.DateField()
    tournament_owner = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    decklist = models.URLField()
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tournament_owner
