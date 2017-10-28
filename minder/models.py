from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    pic = models.ImageField(blank=True, upload_to='profile_img')

    def __str__(self):
        return self.user.username


class Mind(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.now)
    mind = models.TextField()
    mind_img = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.pub_date)
