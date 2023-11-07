from django.db import models

# Create your models here.
class Personifika(models.Model):
    first_name = models.CharField(max_length=252)