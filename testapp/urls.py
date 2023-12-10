from django.urls import path
from .views import EmployeeAPIView

urlpatterns = [
    path('employees/', EmployeeAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeAPIView.as_view(), name='employee-detail'),
]
