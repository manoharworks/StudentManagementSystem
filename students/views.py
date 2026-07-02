from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
    
    
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    
    context = {
        "students": students
    }
    
    return render(request, "students/student_list.html", context)

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect("students:student_list")    

    else:
        form = StudentForm()
        
    context = {
        "form" : form,
    }    
    
    return render(request, "students/student_form.html", context)

def student_detail(request, pk):
    
    student = get_object_or_404(Student, pk)
    
    context = {
        "student" : student
    }
    
    return render(request, "students/student_detail.html", context)


