from django.db import models
from django_facebook.models import FacebookProfileModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class LinkedInProfile(models.Model):
    user = models.OneToOneField(User, related_name='liProfile')
    request_token = models.CharField(max_length=200, null=True, blank=True)
    request_token_secret = models.CharField(max_length=200, null=True, blank=True)
