from django.db import models
from django_facebook.models import FacebookProfileModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


