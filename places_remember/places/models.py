from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"