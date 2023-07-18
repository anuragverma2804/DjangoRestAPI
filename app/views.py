from rest_framework import viewsets
from .models import Company,Employee
from .serializer import CompanySerializer,EmployeeSerializer
# Create your views here.



# Serializers define the API representation.
# ViewSets define the view behavior.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



# ViewSets define the view behavior.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


