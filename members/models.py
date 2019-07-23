from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birthdate = models.DateField(auto_now = True)
    nickname = models.CharField(max_length = 30, primary_key = True)
    GENDER = [('female', 'Female'), ('male', 'Male')]
    gender = models.CharField(max_length = 10, choices = GENDER, default = 'male')
    email = models.EmailField(max_length = 100, blank = True)
    facebook = models.URLField(max_length = 1000, blank = True)
    twitter = models.URLField(max_length = 1000, blank = True)
    instagram = models.URLField(max_length = 1000, blank = True)
    profile = models.ImageField(upload_to = 'static/members', blank = True)
    bio = models.TextField(default = 'Apparently, this user prefers to keep an air of mystery about them')

    def __str__(self):
        return self.nickname + f' ({self.first_name} {self.last_name})'

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length = 70)
    text = models.TextField(max_length = 500)

    def __str__(self):
        return str(self.subject) + ' / sent by ' + str(self.user)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
