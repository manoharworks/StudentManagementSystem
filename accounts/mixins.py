from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages import error
from django.shortcuts import redirect


class ERPPermissionRequiredMixin(PermissionRequiredMixin):
    
    raise_exception = False

    permission_denied_message = (
        "You do not have permission to perform this action."
    )

    def handle_no_permission(self):
        error(
            self.request,
            self.get_permission_denied_message(),
        )

        return redirect("dashboard:dashboard")