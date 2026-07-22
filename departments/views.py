from django.shortcuts import (render,  get_object_or_404, redirect)
from django.contrib.auth.decorators import login_required
from .models import Department
from .forms import DepartmentForm
from django.contrib import messages


@login_required
def department_list(request):
    
    departments = Department.objects.all()
    
    context = {
        "departments": departments,
    }
    
    return render(request, "departments/department_list.html", context)

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    
    context = {
        "department" : department,
    }
    
    return render(request, "departments/department_detail.html", context)

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Department created sucessfully")
            
            return redirect("departments:department_list")   
        
    else:
            form = DepartmentForm()
            
    context = {
        "form": form,
        "title": "Add Department",
    }        
            
    return render(request, "departments/department_form.html", context)
            
             

def department_update(request, pk):
    
    department = get_object_or_404(Department, pk = pk)
    
    if request.method == "POST":
        
        form = DepartmentForm(request.POST, instance=department)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Department updated successfully")
            
            return redirect("departments:department_list")
        
    else:
        form = DepartmentForm(instance=department)
        
    context = {
        "form" : form,
        "department" : department,
        "title": "Update Department",
    }    
    
    return render(request, "departments/department_form.html", context)
            

def department_delete(request, pk):
    
    department = get_object_or_404(Department, pk = pk)
    
    if request.method == "POST":
        
        department.delete()
        
        messages.success(request, "Department deleted successfully")
        
        return redirect("departments:department_list")
    
    context = {
        "department": department
    }
    
    return render(request, "departments/departement_confirm_delete", context)


    
    
    