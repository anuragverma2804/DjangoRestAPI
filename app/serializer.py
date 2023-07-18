from rest_framework import routers, serializers, viewsets
from .models import Company,Employee




class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ["id","name","location","type"]




class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "company"]



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
