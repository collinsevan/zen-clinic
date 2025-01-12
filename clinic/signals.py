from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create a UserProfile when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    """
    Signal to automatically delete a UserProfile when a User is deleted.
    """
    if hasattr(instance, 'profile'):
        instance.profile.delete()
