from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)


def save_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile(user=kwargs['instance'])
        user_profile.save(force_insert=True)


post_save.connect(save_user_profile, sender=User)
