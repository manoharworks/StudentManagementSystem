from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import StudentSerializer
from students.models import Student
from .permissions import ERPModelPermissions


class StudentViewSet(ModelViewSet):
    
    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    permission_classes = [
        IsAuthenticated,
        ERPModelPermissions,
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "department",
        "gender",
    ]

    search_fields = [
        "name",
        "email",
        "phone",
    ]

    ordering_fields = [
        "name",
        "email",
        "date_of_birth",
    ]
    
    # Making default order
    ordering = [
        "name"
    ]


