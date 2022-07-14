from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from .models import Employee


@api_view(["GET", "POST"])
def employee(request):
    
    if request.method == "GET":
        all_data = Employee.objects.all()
        
        serializer = EmployeeSerializer(all_data, many=True)
        
        data = {
            "message" : "success",
            "data_count": len(all_data),
            "data": serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)
        
    