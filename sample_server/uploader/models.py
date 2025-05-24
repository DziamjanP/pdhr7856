from django.db import models

class DataPiece(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateTimeField()