import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView; 
from drf_yasg.utils import swagger_auto_schema


class EmployeeListView(APIView):
    

    def get(self, request, format=None):
        """Allows the user to get a list of all employees
        """
        
        all_data = Employee.objects.all()
        serializer = EmployeeSerializer(all_data, many=True)
        
        data = {
            "message" : "success",
            "data_count": len(all_data),
            "data": serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(method="post", request_body=EmployeeSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """API View to create new employees"""
        
        serializer = EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data["employee_num"] = "".join([str(random.choice(range(10))) for _ in range(6)])
            serializer.save()
            
            
            data = {
                "message":"success",
            }
            return Response(data, status=status.HTTP_201_CREATED)
            

        else:
            data = {
                "message":"failed",
                "error":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    