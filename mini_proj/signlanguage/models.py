from django.db import models

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    
class ai_admin(models.Model) :
    file = models.FileField()
    input_count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    checkbox = models.BooleanField(default=0)