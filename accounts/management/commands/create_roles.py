# This is the code to create groups and assign permssions to each.
# This entire operation can be done manually in the Django Admin interface
# without writing or running this management command. But due to some major cons this way is preferred.

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

ROLE_PERMISSIONS = {
    "Admin": [
        ("students", "view_student"),
        ("students", "add_student"),
        ("students", "change_student"),
        ("students", "delete_student"),

        ("departments", "view_department"),
        ("departments", "add_department"),
        ("departments", "change_department"),
        ("departments", "delete_department"),

        ("courses", "view_course"),
        ("courses", "add_course"),
        ("courses", "change_course"),
        ("courses", "delete_course"),

        ("enrollments", "view_enrollment"),
        ("enrollments", "add_enrollment"),
        ("enrollments", "change_enrollment"),
        ("enrollments", "delete_enrollment"),

        ("attendance", "view_attendance"),
        ("attendance", "add_attendance"),
        ("attendance", "change_attendance"),
        ("attendance", "delete_attendance"),

        ("grades", "view_grade"),
        ("grades", "add_grade"),
        ("grades", "change_grade"),
        ("grades", "delete_grade"),
    ],

    "Teacher": [
        ("students", "view_student"),

        ("departments", "view_department"),

        ("courses", "view_course"),

        ("enrollments", "view_enrollment"),

        ("attendance", "view_attendance"),
        ("attendance", "add_attendance"),
        ("attendance", "change_attendance"),

        ("grades", "view_grade"),
        ("grades", "add_grade"),
        ("grades", "change_grade"),
    ],

    "Staff": [
        ("students", "view_student"),
        ("students", "add_student"),
        ("students", "change_student"),

        ("departments", "view_department"),

        ("courses", "view_course"),

        ("enrollments", "view_enrollment"),
        ("enrollments", "add_enrollment"),
        ("enrollments", "change_enrollment"),

        ("attendance", "view_attendance"),

        ("grades", "view_grade"),
    ],

    "Student": [
        ("students", "view_student"),
        ("courses", "view_course"),
        ("enrollments", "view_enrollment"),
        ("attendance", "view_attendance"),
        ("grades", "view_grade"),
    ],
}


class Command(BaseCommand):
    help = "Create and update ERP groups with permissions."

    def handle(self, *args, **options):
        total_created = 0
        total_updated = 0
        missing_permissions = []

        for role_name, permission_specs in ROLE_PERMISSIONS.items():

            group, created = Group.objects.get_or_create(
                name=role_name
            )

            permissions = []

            for app_label, codename in permission_specs:

                permission = Permission.objects.filter(
                    content_type__app_label=app_label,
                    codename=codename,
                ).first()

                if permission:
                    permissions.append(permission)
                else:
                    missing_permissions.append(
                        f"{app_label}.{codename}"
                    )

            group.permissions.set(permissions)

            if created:
                total_created += 1
                action = "Created"
            else:
                total_updated += 1
                action = "Updated"

            self.stdout.write(
                self.style.SUCCESS(
                    f"{action:<7} {role_name:<10}"
                    f" ({len(permissions)} permissions)"
                )
            )

        if missing_permissions:
            self.stdout.write("")
            self.stdout.write(
                self.style.WARNING(
                    "Missing Permissions:"
                )
            )

            for permission in sorted(missing_permissions):
                self.stdout.write(
                    f"  • {permission}"
                )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Summary"
            )
        )
        self.stdout.write(
            f"Created Groups : {total_created}"
        )
        self.stdout.write(
            f"Updated Groups : {total_updated}"
        )