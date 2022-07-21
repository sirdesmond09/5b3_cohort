from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserListCreateView().as_view(), name="user_list" ),
    # path("users/<int:employee_id>/", views.EmployeeDetailView().as_view(), name="employee_detail" ),
]
