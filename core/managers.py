from django.db import models
from django.db.models import Q

class StudentQuerySet(models.QuerySet):
    
    def with_department(self):
        return self.select_related("department")
    
    def search(self, query):
        if not query:
            return self
        
        return self.filter(
            Q(roll_number__icontains=query)
            |
            Q(name__icontains=query)
            |
            Q(email__icontains=query)
        )
        
    def filter_by_department(self, department_id):
        
        if not department_id:
            return self
        
        return self.filter(department_id=department_id)
    
    
class StudentManager(models.Manager.from_queryset(StudentQuerySet)):
    pass
                