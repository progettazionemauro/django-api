from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# from .models import Nation

@receiver(post_save, sender=Nation)
def handle_nation_save(sender, instance, created, **kwargs):
    """
    This function will be called whenever a Nation object is saved.
    """
    if created:
        # Handle logic for newly created Nation objects
        print(f"New Nation added: {instance.name}")
    else:
        # Handle logic for existing Nation objects being updated
        print(f"Nation updated: {instance.name}")

@receiver(post_delete, sender=Nation)
def handle_nation_delete(sender, instance, **kwargs):
    """
    This function will be called whenever a Nation object is deleted.
    """
    print(f"Nation deleted: {instance.name}")
