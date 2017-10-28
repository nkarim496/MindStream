from django.db import models
from django.utils import timezone


class SiteSetting(models.Model):
    ava = models.ImageField(blank=True, upload_to='user_ava')

    def __str__(self):
        return self.ava.name


class Wimm(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    img = models.ImageField(blank=True, upload_to='wimm_img')
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.text[:20]


class DayState(models.Model):
    state = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now, unique=True)

    def __str__(self):
        return self.state[:20]
