from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.TextField(max_length=200)
    image = models.ImageField(upload_to='teams/%Y/%m/%d/', default='teams/default-profile.jpg')
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def photo_url(self):
        try:
            url = self.image.url
        except:
            url = '/static/img/team/default-profile.jpg'
        return url

   
