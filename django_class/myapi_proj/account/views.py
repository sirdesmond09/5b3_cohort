from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAdminOrSignUp
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

User = get_user_model()
# Create your views here.


class UserListCreateView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrSignUp]
    
    
    def get(self, request, format=None):
        """Allows only admin users to get a list of all users
        """
        
        all_data = User.objects.filter(is_active=True)
        serializer = UserSerializer(all_data, many=True)
        
        data = {
            "message" : "success",
            "data_count": len(all_data),
            "data": serializer.data
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(method="post", request_body=UserSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """API View to create new users"""
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data["password"] = make_password(serializer.validated_data.get("password"))
            
            
            user = User.objects.create(**serializer.validated_data)
            
            Token.objects.create(user=user)
            
            
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
        
    
    

# class EmployeeDetailView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get_object(self, employee_id):
#         try:
#             return Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#             raise NotFound(detail={"message":"Employee not found"}, code=status.HTTP_404_NOT_FOUND)
        
        
#     def get(self, request, employee_id, format=None ):
#         """Api view to get the details of an employee"""
#         obj  =  self.get_object(employee_id)
#         serializer = EmployeeSerializer(obj)
#         data = {
#             "message" : "success",
#             "data": serializer.data
#         }
        
#         return Response(data, status=status.HTTP_200_OK)
    
    
#     @swagger_auto_schema(method="put", request_body=EmployeeSerializer())
#     @action(methods=["put"], detail=True)
#     def put(self, request, employee_id, format=None):
#         """API View to edit employees"""
        
#         obj  =  self.get_object(employee_id)
#         serializer = EmployeeSerializer(obj, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             if "employee_num" in serializer.validated_data.keys():
#                 raise PermissionDenied(detail={"message":"you cannot edit your employee number"}, code=status.HTTP_403_FORBIDDEN)
            
#             serializer.save()
            
#             data = {
#                 "message":"success",
#             }
#             return Response(data, status=status.HTTP_202_ACCEPTED)
            

#         else:
#             data = {
#                 "message":"failed",
#                 "error":serializer.errors
#             }
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, employee_id, format=None):
#         """Delete an employee"""
        
#         obj  =  self.get_object(employee_id)
#         obj.delete()
#         return Response({}, status=status.HTTP_204_NO_CONTENT)