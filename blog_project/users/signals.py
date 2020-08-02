# this signal fired after an object save
from django.db.models.signals import post_save
# it will be sender
from django.contrib.auth.models import User
# reciever grab this signal and do everything(decorator)
from django.dispatch import receiver
from .models import Profile


# whenever user create
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# instance is User
# everytime user profile save
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


# have call this function inside the app.py
