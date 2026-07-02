from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    
    context = {
        "students": students
    }
    
    return render(request, "/Users/manoharjha/django_Projects/StudentManagementSystem/templates/students/student_list.html", context)

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            from.save()
            
            return redirect("students:student_list")    

    else:
        form = StudentForm()
        
    context = {
        "form" : form,
    }    
    
    return render(request, "/Users/manoharjha/django_Projects/StudentManagementSystem/templates/students/student_form.html", context)
