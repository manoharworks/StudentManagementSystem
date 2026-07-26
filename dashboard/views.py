from django.shortcuts import render
from .services import DashboardService

def dashboard(request):
    
    context = DashboardService.get_dashboard_data()
    
    return render(request, "dashboard/dashboard.html", context)