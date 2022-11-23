from django.db import models

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    image_arr = []
    ans_arr = []

#class AiModel(models.Model):
#    ai_file = models.FieldFile(blank=True)
#    version = models.CharField(max_length=100)
#    is_selected = models.BooleanField(max_length=10)
#    pub_date = models.DateTimeField('date published')