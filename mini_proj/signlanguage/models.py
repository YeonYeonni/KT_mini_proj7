from django.db import models
from django.conf import settings
# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')
    image_arr = []
    ans_arr = []

<<<<<<< HEAD
class AiModel(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=30)
    prediction_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    is_using = models.BooleanField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
=======
#class AiModel(models.Model):
#    ai_file = models.FieldFile(blank=True)
#    version = models.CharField(max_length=100)
#    is_selected = models.BooleanField(max_length=10)
#    pub_date = models.DateTimeField('date published')
>>>>>>> c9bf3411f4d6275950c3dbe3a02154790e65af7e
