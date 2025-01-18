# files/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:  # Check if this is a new user
        group, created = Group.objects.get_or_create(name='Viewers')  
        instance.groups.add(group)
