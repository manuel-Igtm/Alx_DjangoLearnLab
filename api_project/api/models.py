from django.db import models

# Create your models here.
#In api/models.py, define a Book model with basic fields such as title (a CharField) and author (a CharField).

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)