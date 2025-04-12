# Fire this signal after a post is saved.
from django.db.models.signals import post_save
# User is the sender, user sends a signal
from django.contrib.auth.models import User
# Create a receiver, receives signal
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


