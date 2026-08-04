from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    def active(self):

        return self.filter(is_active=True)

    def inactive(self):

        return self.filter(is_active=False)

    def staff_members(self):

        return self.filter(is_staff=True)

    def superusers(self):

        return self.filter(is_superuser=True)

    def students(self):

        return self.filter(groups__name="Student")

    def teachers(self):

        return self.filter(groups__name="Teacher")

    def search(self, query):

        if not query:
            return self

        return self.filter(
            models.Q(username__icontains=query)
            | models.Q(first_name__icontains=query)
            | models.Q(last_name__icontains=query)
            | models.Q(email__icontains=query)
        ).distinct()


class UserManager(DjangoUserManager.from_queryset(UserQuerySet)):
    pass
