from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_Length=10)
    introduction = models.TextField()
    area = models.CharField(max_Length=15)
    party_number = models.IntegerField(default=1)