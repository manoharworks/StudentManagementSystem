from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import AuditLog
from .context import get_current_user

AUDITED_MODELS = (
    "students.Student",
    "departments.Department",
    "courses.Course",
    "enrollments.Enrollment",
    "attendance.Attendance",
    "grades.Grade",
)


def should_audit(instance):
    model_label = f"{instance._meta.app_label}{instance.__class__.__name__}"

    return model_label in AUDITED_MODELS


def create_audit_log(instance, action):
    AuditLog.objects.create(
        user=get_current_user(),
        action=action,
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.pk,
        object_repr=str(instance),
    )


@receiver(post_save)
def audit_save(sender, instance, created, raw, **kwargs):

    if raw:
        return

    if not should_audit(instance):
        return

    action = AuditLog.Action.CREATE if created else AuditLog.Action.UPDATE

    create_audit_log(instance, action)



@receiver(post_delete)
def audit_delete(sender, instance, **kwargs,):

    if not should_audit(instance):
        return

    create_audit_log(instance, AuditLog.Action.DELETE,)
