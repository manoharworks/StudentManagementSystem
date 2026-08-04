from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Create ERP roles and permissions"
    
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
    
    def handle(self, *args, **options):

        for role_name, permission_specs in self.ROLE_PERMISSIONS.items():

            group, created = Group.objects.get_or_create(
                name=role_name
            )

            permissions = []

            for app_label, codename in permission_specs:

                permission = Permission.objects.filter(
                    content_type__app_label=app_label,
                    codename=codename,
                ).first()

                if permission is None:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Permission not found: "
                            f"{app_label}.{codename}"
                        )
                    )
                    continue

                permissions.append(permission)

            group.permissions.set(permissions)

            action = "Created" if created else "Updated"

            self.stdout.write(
                self.style.SUCCESS(
                    f"{action} role: {role_name}"
                )
            )