from django.db import models
from django.utils import timezone


class RankingUser(models.Model):
    name = models.CharField(null=False, max_length=256)
    
class Score(models.Model):
    score = models.PositiveIntegerField()
    user = models.ForeignKey(RankingUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, default=timezone.now)
