from django.db.models.signals import post_save
from .models import CustomUser
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def Create_events(sender, instance, created, **kwargs):
    print("*" * 100)
    print(sender)
    print(instance)
    print(created)
    print("*" * 100)
