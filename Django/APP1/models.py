from django.db import models


# Create your models here.
class APP1(models.Model):
    title = models.CharField(max_length=300)
