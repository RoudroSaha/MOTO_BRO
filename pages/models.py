from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.TextField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

   
