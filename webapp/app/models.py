from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    twitter_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
    user1 = models.ForeignKey(User, related_name='team_user1', on_delete=models.SET_NULL, null=True)
    user2 = models.ForeignKey(User, related_name='team_user2', on_delete=models.SET_NULL, null=True)
    user3 = models.ForeignKey(User, related_name='team_user3', on_delete=models.SET_NULL, null=True)
    user4 = models.ForeignKey(User, related_name='team_user4', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
