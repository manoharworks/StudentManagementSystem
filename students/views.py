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
    
    student = get_object_or_404(Student, pk=pk)
    
    context = {
        "student" : student
    }
    
    return render(request, "students/student_detail.html", context)


def student_update(request, pk):
    
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance = student)
        
        if form.is_valid():
            form.save()
            
            return redirect("students:student_detail",
                            pk = student.pk)
            
            
    else:
        form = StudentForm(instance = student)
        
    context = {
        "form" : form,
        "student": student,
    }    
                    
    return render(request, "students/student_form.html", context)
                