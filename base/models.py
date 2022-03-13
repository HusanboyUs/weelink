from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=10)
    bio=models.CharField(max_length=20)
    #avatar=models.FieldFile()
    instagram=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    telegram=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    #slug field for users
    
    def __str__(self):
        return self.name
    
    #for creating userprofile for every registered user after registtration
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profile'        


class ProfileLink(models.Model):
    user=models.ForeignKey(Profile, default=1, on_delete=models.CASCADE, db_constraint=False, related_name='linkowner')
    link_name=models.CharField(max_length=12, null=True, default='Link Name')
    link=models.CharField(max_length=200, null=True, default='My link')

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name='Profile Link'
        verbose_name_plural='Profile Link'