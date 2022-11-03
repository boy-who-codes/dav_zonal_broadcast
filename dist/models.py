from django.db import models

# Create your models here.
class Edit(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    
class Sport(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100 , default="")
    def __str__(self):
        return f"{self.name} | ({self.school})"

class Match(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner', default=None, null=True, blank=True)
    result = models.CharField(max_length=100, default="")
    def __str__(self):
        return f"{self.id} | {self.team1} vs {self.team2} | {self.result}"
    
class Cluster(models.Model):
    name = models.CharField(max_length=100)
    total_score = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
    
class Score (models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    Score = models.IntegerField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cluster} | {self.team.name} | {self.Score}"