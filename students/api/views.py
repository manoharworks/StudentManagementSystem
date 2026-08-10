from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from students.models import Student

class StudentListAPIView(APIView):
    
    def get(self, request):
        
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )    