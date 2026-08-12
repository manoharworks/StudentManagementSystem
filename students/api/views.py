from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from students.models import Student

class StudentListCreateAPIView(ListCreateAPIView):
    
    queryset = Student.objects.all()
    
    serializer_class = StudentSerializer
    
class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    
    serializer_class = StudentSerializer