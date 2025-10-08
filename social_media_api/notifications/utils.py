from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    target_ct = None
    target_id = None
    if target is not None:
        target_ct = ContentType.objects.get_for_model(target.__class__)
        target_id = target.pk
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=target_ct,
        target_object_id=target_id
    )

def create_notification_for_like(actor, recipient, target):
    # Don't notify yourself
    if actor == recipient:
        return
    create_notification(recipient=recipient, actor=actor, verb='liked your post', target=target)

def create_notification_for_follow(actor, recipient):
    if actor == recipient:
        return
    create_notification(recipient=recipient, actor=actor, verb='followed you', target=None)

def create_notification_for_comment(actor, recipient, target):
    if actor == recipient:
        return
    create_notification(recipient=recipient, actor=actor, verb='commented on your post', target=target)
