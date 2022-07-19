from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.EmployeeListView().as_view(), name="employee_list" ),
    path("employees/<int:employee_id>/", views.EmployeeDetailView().as_view(), name="employee_detail" ),
]
