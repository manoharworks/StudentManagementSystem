from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm, LoginForm, ProfileUpdateForm
from .services import AccountService
from .models import User


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    # Overrriding the form_valid to use the services
    def form_valid(self, form):

        self.object = AccountService.register_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )

        messages.success(
            self.request,
            "Account created successfully.",
        )

        return redirect(self.get_success_url())
class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return str(reverse_lazy("dashboard:dashboard"))


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")

class ProfileView(
    LoginRequiredMixin,
    DetailView,
):

    model = User

    template_name = "accounts/profile.html"

    context_object_name = "user_object"

    def get_object(self):
        return self.request.user
    
class ProfileUpdateView(
    LoginRequiredMixin,
    UpdateView,
):

    model = User

    form_class = ProfileUpdateForm

    template_name = "accounts/profile_update.html"

    success_url = reverse_lazy(
        "accounts:profile"
    )

    def get_object(self):
        return self.request.user

    def form_valid(self, form):

        messages.success(
            self.request,
            "Profile updated successfully."
        )

        return super().form_valid(form)