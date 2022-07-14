from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee, name="employee_list" ),
]
