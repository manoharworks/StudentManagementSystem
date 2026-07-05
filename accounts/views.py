"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def custom_login_view(request):
    # 1. If the user is already logged in, send them straight to the student list
    if request.user.is_authenticated:
        return redirect('students:student_list')

    if request.method == "POST":
        # 2. Bind the submitted POST data to Django's built-in login form
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # 3. Extract the cleaned username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # 4. Check if the credentials match a record in the database
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # 5. Create the login session cookie in the user's browser
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('students:student_list')
        
        # If form is invalid or authentication fails
        messages.error(request, "Invalid username or password.")
    else:
        # 6. If it's a GET request, initialize a blank form
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
"""


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Account created Successfully")
            
            return redirect("accounts:login")
        
    else:
        form = CustomUserCreationForm()
        
    context = {"form" : form}    
    
    return render(request, "accounts/signup.html", context )         

@login_required
def profile(request): 
    return render(request, "accounts/profile.html")

