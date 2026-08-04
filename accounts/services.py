"""
Business services for user accounts.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction

User = get_user_model()


class AccountService:
    """
    Service class containing business logic related to user accounts.
    """

    DEFAULT_GROUP = "Student"

    @classmethod
    @transaction.atomic
    def register_user(
        cls,
        *,
        username: str,
        password: str,
        email: str,
        first_name: str = "",
        last_name: str = "",
    ) -> User:
        """
        Register a new user.

        Responsibilities
        ----------------
        - Create the user.
        - Assign the default Student group.
        - Return the created user.

        Raises
        ------
        Group.DoesNotExist
            If the default group has not been created.
        """

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        student_group = Group.objects.get(
            name=cls.DEFAULT_GROUP,
        )

        user.groups.add(student_group)

        return user